import pandas as pd

# Load file
df = pd.read_excel("Customer_Purchase_History.xlsx")

# Ensure Total column exists
df["Total"] = df["Quantity"] * df["UnitPrice"]
print(df)

# Product-wise summary
product_summary = df.groupby("Product")["Total"].sum().reset_index()
print(product_summary)

# Rename columns correctly
product_summary.columns = ["Product", "Total_Sales"]
print(product_summary)

# Sort for better readability
product_summary = product_summary.sort_values(by="Total_Sales", ascending=False)


# Export to Excel (CLIENT DELIVERABLE)
product_summary.to_excel("Sales_Summary.xlsx", index=False)

print("✅ sales_summary.xlsx created successfully")

