import pandas as pd
import matplotlib.pyplot as plt


class CustomerBehaviorAnalysis:
    def __init__(self, df):
        """
        Initialize with a dataframe containing transaction data.
        """
        self.df = df.copy()

    def top_customers_analysis(self, top_n=10):
        """Analyze and visualize the top customers based on total spending and transaction frequency."""

        # Analyze spending patterns
        spending = (
            self.df.groupby("CustomerId")["Amount"].sum().sort_values(ascending=False)
        )

        # Analyze frequency of transactions
        buyer_counts = self.df["CustomerId"].value_counts()

        # Visualization: Create side-by-side plots
        fig, axes = plt.subplots(1, 2, figsize=(11, 3.5))  # Side-by-side plots

        # Plot for top customers by spending
        colors_spending = plt.cm.magma(
            np.linspace(0.2, 0.8, top_n)
        )  # Magma color palette
        spending.head(top_n)[::-1].plot(kind="barh", color=colors_spending, ax=axes[0])
        axes[0].set_title("Top Customers by Total Spending")
        axes[0].set_xlabel("Total Spending")
        axes[0].set_ylabel("CustomerId")
        axes[0].grid(False)  # Remove grid
        axes[0].set_xticks([])  # Remove x-ticks

        # Add value labels on bars for spending
        for bar in axes[0].patches:
            axes[0].text(
                bar.get_width(),
                bar.get_y() + bar.get_height() / 2,
                f"{bar.get_width():,.0f}",
                ha="left",
                va="center",
                fontsize=9,
                color="black",
            )

        # Plot for top frequent buyers (styled like the first plot)
        colors_frequent = plt.cm.magma(
            np.linspace(0.2, 0.8, top_n)
        )  # Magma color palette
        buyer_counts.head(top_n)[::-1].plot(
            kind="barh", color=colors_frequent, ax=axes[1]
        )
        axes[1].set_title("Top Frequent Buyers")
        axes[1].set_xlabel("Number of Transactions")
        axes[1].set_ylabel("CustomerId")
        axes[1].grid(False)  # Remove grid
        axes[1].set_xticks([])  # Remove x-ticks

        # Add value labels on bars for frequent buyers
        for bar in axes[1].patches:
            axes[1].text(
                bar.get_width(),
                bar.get_y() + bar.get_height() / 2,
                f"{bar.get_width():,.0f}",
                ha="left",
                va="center",
                fontsize=9,
                color="black",
            )

        # Remove spines
        for ax in axes:
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["bottom"].set_visible(False)

        plt.tight_layout()
        plt.show()

    def repeat_vs_one_time_customers(self):
        """Analyze and visualize repeat vs. one-time customers."""
        customer_transaction_counts = self.df["CustomerId"].value_counts()
        repeat_customers = (customer_transaction_counts > 1).sum()
        one_time_customers = (customer_transaction_counts == 1).sum()

        print(f"Repeat Customers: {repeat_customers}")
        print(f"One-Time Customers: {one_time_customers}")

        # Visualization
        labels = ["Repeat Customers", "One-Time Customers"]
        sizes = [repeat_customers, one_time_customers]
        colors = plt.cm.magma(np.linspace(0.2, 0.8, 2))  # Apply magma colormap
        plt.figure(figsize=(5, 5))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140)
        plt.title("Repeat vs One-Time Customers")
        plt.show()

    def subscription_patterns(self):
        """Analyze and visualize customer subscription patterns."""
        subscription_counts = self.df["SubscriptionId"].value_counts()

        # Visualization
        plt.figure(figsize=(6, 4))
        colors = plt.cm.magma(np.linspace(0.2, 0.8, 10))  # Magma color palette
        ax = subscription_counts.head(10)[::-1].plot(
            kind="barh", color=colors
        )  # Reverse the order

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

        # Remove spines (borders)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)

        # Remove x-ticks
        ax.set_xticks([])

        plt.title("Top Subscription Patterns")
        plt.xlabel("Number of Customers")
        plt.ylabel("SubscriptionId")
        plt.grid(False)  # Remove grid
        plt.tight_layout()
        plt.show()
