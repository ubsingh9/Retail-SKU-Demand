from pandas import to_datetime
from matplotlib.pyplot import subplots, xticks, tight_layout

def plot_sales_trend(sku_id, df):
    df['date']=to_datetime(df['date'])
    sku_df= df[df['SKU']==sku_id]
    sales_series= sku_df.groupby('Date')['Sale'].sum()

    fig, ax = subplots()
    sales_series.plot(ax=ax, marker='o')
    ax.set_title(f"Sales Trend for SKU {sku_id}")
    ax.set_ylabel("Sales")
    ax.set_xlabel("Date")
    xticks(rotation=45)
    tight_layout()
    
    return fig