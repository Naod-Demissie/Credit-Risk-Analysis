import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class FraudRiskAnalysis:
    def __init__(self, data):
        """
        Initialize the FraudRiskAssessment class.
        :param data: DataFrame containing the transaction data.
        """
        self.data = data

    def plot_fraud_rate_by_product(self):
        """Plot the fraud rate by product."""
        fraud_rate = (
            self.data.groupby("ProductId")["FraudResult"]
            .mean()
            .reset_index()
            .sort_values(by="FraudResult", ascending=False)
        )

        plt.figure(figsize=(10, 6))
        sns.barplot(x="FraudResult", y="ProductId", data=fraud_rate, palette="magma")

        # Add values on the side of the bars
        for index, value in enumerate(fraud_rate["FraudResult"]):
            plt.text(
                value + 0.001,
                index,
                f"{value:.4f}",
                va="center",
                fontsize=9,
                color="black",
            )

        plt.title("Fraud Rate by Product")
        plt.xlabel("Fraud Rate")
        plt.ylabel("ProductId")
        plt.tight_layout()
        plt.show()

    def plot_fraud_rates(self):
        """Plot fraud rates by provider and channel side by side and print the values."""

        # Fraud rate by provider
        fraud_rate_provider = (
            self.data.groupby("ProviderId")["FraudResult"]
            .mean()
            .reset_index()
            .sort_values(by="FraudResult", ascending=False)
        )

        # Fraud rate by channel
        fraud_rate_channel = (
            self.data.groupby("ChannelId")["FraudResult"]
            .mean()
            .reset_index()
            .sort_values(by="FraudResult", ascending=False)
        )

        # Create side by side subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

        # Provider plot
        sns.barplot(
            x="ProviderId",
            y="FraudResult",
            data=fraud_rate_provider,
            ax=ax1,
            palette=["#B1AA81", "#8F7A6E"],
        )
        ax1.set_title("Fraud Rate by Provider")
        ax1.set_xlabel("ProviderId")
        ax1.set_ylabel("Fraud Rate")
        ax1.set_xticklabels(fraud_rate_provider["ProviderId"], rotation=45)

        # Channel plot
        sns.barplot(
            x="ChannelId",
            y="FraudResult",
            data=fraud_rate_channel,
            ax=ax2,
            palette=["#B1AA81", "#8F7A6E"],
        )
        ax2.set_title("Fraud Rate by Channel")
        ax2.set_xlabel("ChannelId")
        ax2.set_ylabel("Fraud Rate")
        ax2.set_xticklabels(fraud_rate_channel["ChannelId"], rotation=45)

        # Remove spines except the bottom
        for ax in [ax1, ax2]:
            for spine in ax.spines.values():
                if spine != ax.spines["bottom"]:
                    spine.set_visible(False)

        plt.tight_layout()
        plt.show()

    def plot_anomalies(self):
        """
        Detect and plot anomalies in transaction amounts.
        """
        plt.figure(figsize=(4, 3))
        sns.boxplot(x="FraudResult", y="Amount", data=self.data, palette="coolwarm")
        plt.title("Transaction Amount Distribution by Fraud Result")
        plt.xlabel("FraudResult")
        plt.ylabel("Transaction Amount")
        plt.tight_layout()
        plt.show()
