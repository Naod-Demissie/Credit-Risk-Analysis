import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class CorrelationAnalysis:
    def __init__(self, data):
        self.data = data

    def compute_correlation_matrix(self):
        return self.data[["Amount", "Value"]].corr()

    def plot_correlation_heatmap(self, figsize=(4, 4), cmap="coolwarm", annot=True):
        corr_matrix = self.compute_correlation_matrix()
        plt.figure(figsize=figsize)
        sns.heatmap(corr_matrix, cmap=cmap, annot=annot, fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()

    def plot_pairwise_correlation(
        self, features=["Amount", "Value"], hue=None, palette="viridis"
    ):
        sns.pairplot(self.data, vars=features, hue=hue, palette=palette)
        plt.suptitle("Pairwise Correlation Analysis", y=1.02)
        plt.show()
