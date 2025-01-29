import pandas as pd
import matplotlib.pyplot as plt


class TransactionAnalysis:
    def __init__(self, df):
        """
        Initialize with a dataframe containing transaction data.
        """
        self.df = df.copy()
        self.df["TransactionStartTime"] = pd.to_datetime(
            self.df["TransactionStartTime"]
        )

    def total_transactions_revenue(self):
        """Calculate total transactions and total revenue."""
        total_transactions = len(self.df)
        total_revenue = self.df["Amount"].sum()
        print(f"Total Transactions: {total_transactions}")
        print(f"Total Revenue: {total_revenue}")

    def revenue_trends(self):
        """Plot revenue trends over time."""
        self.df.set_index("TransactionStartTime", inplace=True)
        revenue_over_time = self.df["Amount"].resample("D").sum()
        plt.figure(figsize=(10, 4))
        plt.plot(revenue_over_time, marker="o", linestyle="-")
        plt.title("Revenue Trends Over Time")
        plt.xlabel("Date")
        plt.ylabel("Revenue")
        plt.grid()
        plt.show()
        self.df.reset_index(inplace=True)

    def revenue_breakdown(self):
        """Show and visualize revenue breakdown by provider and product category"""
        fig, axes = plt.subplots(1, 2, figsize=(11, 3))

        for i, col in enumerate(["ProviderId", "ProductCategory"]):
            revenue_by_col = (
                self.df.groupby(col)["Amount"].sum().sort_values(ascending=False)
            )

            # Visualization
            top_revenue = revenue_by_col.head(10)[::-1]
            colors = plt.cm.magma(np.linspace(0.2, 0.8, 10))

            ax = axes[i]
            bars = top_revenue.plot(kind="barh", color=colors, ax=ax)

            ax.set_title(f"Revenue Breakdown by {col}")
            ax.set_xlabel("Total Revenue")
            ax.set_ylabel(col)

            # Remove grid, x-ticks, and spines
            ax.grid(False)
            ax.set_xticks([])
            for spine in ["top", "right", "bottom"]:
                ax.spines[spine].set_visible(False)

            # Add value labels on bars
            for bar in bars.patches:
                ax.text(
                    bar.get_width(),
                    bar.get_y() + bar.get_height() / 2,
                    f"{bar.get_width():,.0f}",
                    ha="left",
                    va="center",
                    fontsize=9,
                    color="black",
                )

        plt.tight_layout()
        plt.show()

    def preferred_transaction_channels(self):
        """Analyze and visualize preferred transaction channels."""
        channel_counts = self.df["ChannelId"].value_counts()

        # Visualization
        plt.figure(figsize=(4.5, 2.5))
        colors = plt.cm.magma(
            np.linspace(0.2, 0.8, len(channel_counts))
        )  # Magma color palette
        ax = channel_counts[::-1].plot(kind="barh", color=colors)  # Reverse the order

        # Adding value labels on bars
        for bar in ax.patches:
            ax.text(
                bar.get_width(),
                bar.get_y() + bar.get_height() / 2,
                f"{bar.get_width():,.0f}",
                ha="left",
                va="center",
                fontsize=9,
                color="black",
            )

        # Remove x-ticks
        ax.set_xticks([])
        for spine in ["top", "right", "bottom"]:
            ax.spines[spine].set_visible(False)

        plt.title("Preferred Transaction Channels")
        plt.xlabel("Transaction Count")
        plt.ylabel("Channel")
        plt.grid(False)  # Remove grid
        plt.tight_layout()
        plt.show()
