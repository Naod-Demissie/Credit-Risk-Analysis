import pandas as pd
import matplotlib.pyplot as plt


class PricingProviderAnalysis:
    def __init__(self, df):
        """
        Initialize with a dataframe containing transaction data.
        """
        self.df = df.copy()

    def provider_performance(self):
        """Analyze provider-wise transaction volume and fraud rates."""
        provider_transaction_counts = self.df["ProviderId"].value_counts()
        provider_fraud_counts = self.df.groupby("ProviderId")["FraudResult"].sum()

        provider_fraud_rates = (
            provider_fraud_counts / provider_transaction_counts
        ).fillna(0)

        # Visualization
        fig, ax1 = plt.subplots(figsize=(7, 5))

        # Transaction Volume (Bar plot)
        ax1.set_xlabel("ProviderId", fontsize=12)
        ax1.set_ylabel("Transaction Volume", color="dodgerblue", fontsize=12)
        bars = provider_transaction_counts.head(10).plot(
            kind="bar", ax=ax1, color="#C4AD9D", alpha=0.9, width=0.7
        )

        # Adding value labels on top of bars
        for bar in bars.patches:
            ax1.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 500,  # Adjust position of value labels
                f"{bar.get_height():,.0f}",
                ha="center",
                va="bottom",
                fontsize=10,
                color="black",
            )

        # Fraud Rate (Line plot)
        ax2 = ax1.twinx()
        ax2.set_ylabel("Fraud Rate", color="tomato", fontsize=12)
        provider_fraud_rates.head(10).plot(
            kind="line", ax=ax2, marker="o", color="tomato", linewidth=2, markersize=8
        )

        # Title and labels
        plt.title(
            "Provider Performance: Transactions & Fraud Rates",
            fontsize=14,
            weight="bold",
        )
        ax1.set_xticklabels(
            provider_transaction_counts.head(10).index, rotation=45, ha="right"
        )

        # Improve layout and styling
        ax1.tick_params(axis="x", labelsize=10)
        ax1.tick_params(axis="y", labelsize=10)
        ax2.tick_params(axis="y", labelsize=10)

        # Remove gridlines and spines for a cleaner look
        ax1.grid(False)
        ax2.grid(False)
        for spine in ax1.spines.values():
            spine.set_visible(False)
        for spine in ax2.spines.values():
            spine.set_visible(False)

        plt.tight_layout()
        plt.show()

    def revenue_and_engagement_by_pricing_strategy(self):
        """Analyze and visualize revenue impact and customer engagement of different pricing strategies."""
        # Group data for revenue
        revenue_by_pricing = (
            self.df.groupby("PricingStrategy")["Amount"]
            .sum()
            .sort_values(ascending=False)
        )

        # Group data for customer engagement
        pricing_engagement = (
            self.df.groupby("PricingStrategy")["CustomerId"]
            .nunique()
            .sort_values(ascending=False)
        )

        fig, axes = plt.subplots(1, 2, figsize=(8, 4))

        color_revenue = "#B1AA81"
        color_engagement = "#8F7A6E"

        ax1 = revenue_by_pricing.plot(kind="bar", color=color_revenue, ax=axes[0])

        for bar in ax1.patches:
            ax1.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.05,
                f"{bar.get_height():,.0f}",
                ha="center",
                va="bottom",
                fontsize=9,
                color="black",
            )

        axes[0].set_title("Revenue by Pricing Strategy", fontsize=12)
        axes[0].set_xlabel("Pricing Strategy", fontsize=10)
        axes[0].set_ylabel("Total Revenue", fontsize=10)
        axes[0].tick_params(axis="x", rotation=0)
        axes[0].spines["top"].set_visible(False)
        axes[0].spines["right"].set_visible(False)
        axes[0].spines["left"].set_visible(False)
        axes[0].grid(False)
        axes[0].set_yticks([])

        ax2 = pricing_engagement.plot(kind="bar", color=color_engagement, ax=axes[1])

        for bar in ax2.patches:
            ax2.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.05,
                f"{bar.get_height():,.0f}",
                ha="center",
                va="bottom",
                fontsize=9,
                color="black",
            )

        axes[1].set_title("Customer Engagement by Pricing Strategy", fontsize=12)
        axes[1].set_xlabel("Pricing Strategy", fontsize=10)
        axes[1].set_ylabel("Unique Customers", fontsize=10)
        axes[1].tick_params(axis="x", rotation=0)
        axes[1].spines["top"].set_visible(False)
        axes[1].spines["right"].set_visible(False)
        axes[1].spines["left"].set_visible(False)
        axes[1].grid(False)
        axes[1].set_yticks([])

        plt.tight_layout()
        plt.show()
