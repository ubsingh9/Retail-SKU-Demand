import pandas as pd
import matplotlib.pyplot as plt
from typing import Union
from langchain_core.tools import tool

df = pd.read_csv("data/retail_store_inventory.csv")  # load once globally
df['Date'] = pd.to_datetime(df['Date'])

@tool
def plot_sales_trend_tool(sku_id:str)-> Union[str, None]:
    """
    Plots the sales trend for a given SKU ID.
    Returns the filepath of the saved plot image (can be displayed by the UI).
    """
    sku_df=df[df['SKU']==sku_id]
    if sku_id.empty:
        return f'No data found for {sku_id}'
    
    sales_series=sku_df.groupby('Date')['Sales'].sum()
    fig, ax = plt.subplots()
    sales_series.plot(ax=ax, marker='o')
    ax.set_title(f"Sales Trend for {sku_id}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()

    file_path=f'charts/{sku_id}_sales_trend.png'
    fig.savefig(file_path)
    plt.close(fig)
    return file_path
