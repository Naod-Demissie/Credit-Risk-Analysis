import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from scipy.stats import norm


class DefaultEstimator:
    def __init__(self, threshold=0.5, max_bins=5):
        self.threshold = threshold  # Decision boundary for good/bad classification
        self.max_bins = max_bins  # Number of bins for WoE binning
        self.model = DecisionTreeClassifier(max_depth=3)  # Proxy estimator

    def fit_rfms(self, X):
        """Fit a decision tree classifier to estimate default risk based on RFMS variables."""
        self.model.fit(X, (X.mean(axis=1) < self.threshold).astype(int))

    def predict_risk(self, X):
        """Predict the default risk category based on RFMS scores."""
        return self.model.predict(X)

    def assign_labels(self, X):
        """Assign labels to users based on RFMS scores."""
        return ["Bad" if score < self.threshold else "Good" for score in X.mean(axis=1)]

    def compute_woe(self, X, y):
        """Compute Weight of Evidence (WoE) for binning."""
        df = pd.DataFrame({"score": X.mean(axis=1), "default": y})
        df["bin"] = pd.qcut(df["score"], self.max_bins, duplicates="drop")

        # Compute WoE for each bin
        bin_stats = df.groupby("bin")["default"].agg(["count", "sum"])
        bin_stats["non_default"] = bin_stats["count"] - bin_stats["sum"]
        bin_stats["bad_rate"] = bin_stats["sum"] / bin_stats["count"]
        bin_stats["good_rate"] = bin_stats["non_default"] / bin_stats["count"]
        bin_stats["woe"] = np.log(
            (bin_stats["good_rate"] + 1e-5) / (bin_stats["bad_rate"] + 1e-5)
        )

        return bin_stats[["woe"]]

    def transform(self, X):
        """Transform RFMS scores into WoE bins."""
        labels = self.assign_labels(X)
        y = [1 if label == "Bad" else 0 for label in labels]
        woe_bins = self.compute_woe(X, y)
        return woe_bins
