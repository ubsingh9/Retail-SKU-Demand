import os
import pandas as pd
import matplotlib.pyplot as plt
from typing import Union
from langchain_core.tools import tool

# Load CSV once globally
df_path = "data/retail_store_inventory.csv"
try:
    df = pd.read_csv(df_path)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
except Exception as e:
    df = pd.DataFrame()  # Fallback in case of error

@tool
def plot_sales_trend(product_id: str, region: str = None, months: int = 3) -> Union[str, None]:
    """
    Plots the sales trend for a given Product ID (SKU).
    Returns the filepath of the saved plot image (can be displayed by the UI).
    Gracefully handles invalid input and missing data.
    """
    try:
        # Basic checks
        if df.empty:
            return "Sales data is unavailable or could not be loaded."

        if not product_id or not isinstance(product_id, str):
            return "Invalid product ID provided. Please specify a valid SKU (Product ID)."

        # Required columns check
        required_columns = ['Date', 'Product ID', 'Units Sold', 'Region']
        for col in required_columns:
            if col not in df.columns:
                return f"Missing required column: {col}"

        # Filter data
        filtered_df = df[df['Product ID'] == product_id]
        if region:
            filtered_df = filtered_df[filtered_df['Region'] == region]

        if filtered_df.empty:
            return f"No sales data found for Product ID '{product_id}' in Region '{region or 'ALL'}'."

        # Filter last N months
        latest_date = filtered_df['Date'].max()
        start_date = latest_date - pd.DateOffset(months=months)
        filtered_df = filtered_df[filtered_df['Date'] >= start_date]

        if filtered_df.empty:
            return f"No recent sales data (last {months} months) available for '{product_id}'."

        # Prepare trend data
        trend = filtered_df.groupby('Date')['Units Sold'].sum().reset_index()

        # Plotting
        plt.figure(figsize=(10, 5))
        plt.plot(trend['Date'], trend['Units Sold'], marker='o', color='blue')
        plt.title(f"Sales Trend: {product_id} ({region or 'All Regions'})")
        plt.xlabel("Date")
        plt.ylabel("Units Sold")
        plt.grid(True)
        plt.tight_layout()

        # Save image
        plot_path = "temp_plot.png"
        plt.savefig(plot_path)
        plt.close()

        return plot_path

    except Exception as e:
        return f"Failed to generate sales trend chart due to: {str(e)}"
