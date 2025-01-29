import numpy as np
import pandas as pd
from sklearn.preprocessing import (
    OneHotEncoder,
    LabelEncoder,
    StandardScaler,
    MinMaxScaler,
)
from IPython.display import display


class FeatureEngineering:
    def __init__(self, df, target_column):
        self.df = df.copy()
        self.target_column = target_column
        self.label_encoder = LabelEncoder()
        self.one_hot_encoder = OneHotEncoder(drop="first", sparse_output=False)
        self.scaler = StandardScaler()
        self.normalizer = MinMaxScaler()
        self.transformed_df = None  # Store transformed features separately

    def create_aggregate_features(self):
        print("\nCreating aggregate features...")
        total_amount = (
            self.df.groupby("CustomerId")["Amount"]
            .sum()
            .reset_index(name="TotalTransactionAmount")
        )
        avg_amount = (
            self.df.groupby("CustomerId")["Amount"]
            .mean()
            .reset_index(name="AverageTransactionAmount")
        )
        transaction_count = (
            self.df.groupby("CustomerId")["TransactionId"]
            .count()
            .reset_index(name="TransactionCount")
        )
        std_amount = (
            self.df.groupby("CustomerId")["Amount"]
            .std()
            .reset_index(name="StdTransactionAmount")
        )

        aggregated_features = (
            total_amount.merge(avg_amount, on="CustomerId", how="left")
            .merge(transaction_count, on="CustomerId", how="left")
            .merge(std_amount, on="CustomerId", how="left")
        )
        aggregated_columns = aggregated_features.columns.tolist()
        self.df = self.df.merge(aggregated_features, on="CustomerId", how="left")
        print("New columns added:", aggregated_columns)
        print("DataFrame shape after aggregation:", self.df.shape)
        display(self.df[["Amount", *aggregated_columns]].head())

    def extract_features(self):
        print("\nExtracting time-based features...")
        self.df["TransactionStartTime"] = pd.to_datetime(
            self.df["TransactionStartTime"]
        )
        self.df["TransactionHour"] = self.df["TransactionStartTime"].dt.hour
        self.df["TransactionDay"] = self.df["TransactionStartTime"].dt.day
        self.df["TransactionMonth"] = self.df["TransactionStartTime"].dt.month
        self.df["TransactionYear"] = self.df["TransactionStartTime"].dt.year
        extracted_columns = [
            "TransactionHour",
            "TransactionDay",
            "TransactionMonth",
            "TransactionYear",
        ]
        print("Extracted columns:", extracted_columns)
        display(self.df[["TransactionStartTime", *extracted_columns]].head())

    def encode_categorical_variables(self):
        print("\nEncoding categorical variables...")
        categorical_columns = [
            "ProviderId",
            "ProductId",
            "ProductCategory",
            "ChannelId",
            "PricingStrategy",
            "TransactionHour",
            "TransactionDay",
            "TransactionMonth",
            "TransactionYear",
        ]

        one_hot_encoded = self.one_hot_encoder.fit_transform(
            self.df[categorical_columns]
        )
        one_hot_encoded_df = pd.DataFrame(
            one_hot_encoded,
            columns=self.one_hot_encoder.get_feature_names_out(categorical_columns),
        )
        print("One-hot encoded shape:", one_hot_encoded_df.shape)

        self.df = pd.concat([self.df, one_hot_encoded_df], axis=1)
        self.df.drop(columns=categorical_columns, inplace=True)
        print("DataFrame shape after encoding:", self.df.shape)
        display(self.df.head())

    def normalize_standardize_numerical_features(self):
        print("\nNormalizing and standardizing numerical features...")
        numerical_columns = [
            "Amount",
            "Value",
            "TotalTransactionAmount",
            "AverageTransactionAmount",
            "TransactionCount",
            "StdTransactionAmount",
        ]
        self.df[numerical_columns] = self.normalizer.fit_transform(
            self.df[numerical_columns]
        )
        # self.df[numerical_columns] = self.scaler.fit_transform(self.df[numerical_columns])
        display(self.df[numerical_columns].head())

    def get_transformed_dataframe(self):
        columns_to_drop = [
            "TransactionId",
            "BatchId",
            "AccountId",
            "SubscriptionId",
            "CustomerId",
            "CurrencyCode",
            "CountryCode",
            "TransactionStartTime",
        ]
        X = self.df.drop(columns=[self.target_column, *columns_to_drop])
        y = self.df[self.target_column]

        # Store transformed features separately
        self.transformed_df = X.copy()

        # Save as .npy format
        np.save("../data/processed/X_features.npy", X.values)
        np.save("../data/processed/y_labels.npy", y.values)

        print("Final Transformed DataFrame:")
        display(self.transformed_df.head())

        return X, y
