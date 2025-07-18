from pandas import read_csv

def row_to_text(row):
    return(
        f"On {row['Date']}, Store {row['Store ID']} in the {row['Region']} region sold product {row['Product ID']} "
        f"from the {row['Category']} category. The inventory level was {row['Inventory Level']} units, "
        f"with {row['Units Sold']} units sold and {row['Units Ordered']} units ordered. "
        f"The demand forecast predicted {row['Demand Forecast']} units. The product was priced at ₹{row['Price']} "
        f"with a discount of {row['Discount']}%. The weather was {row['Weather Condition']} and it was "
        f"{'a promotion or holiday' if row['Holiday/Promotion'] == 1 else 'a regular day'}. "
        f"Competitor pricing for similar products was ₹{row['Competitor Pricing']}. "
        f"The season was {row['Seasonality']}."
    )

def load_and_chunk_csv(filepath):
    df= read_csv(filepath)
    df=df.dropna()
    chunks = [row_to_text(row) for _,row in df.iterrows()]
    return chunks

if __name__ == "__main__":
    chunks = load_and_chunk_csv("data/retail_store_inventory.csv")
    print(chunks[:3])