import pandas as pd

df = pd.read_csv('Grocery_Inventory_and_Sales_Dataset.csv')

# 先強迫轉文字，清掉 $ 和 , 後，再轉為浮點數
df['Unit_Price'] = df['Unit_Price'].astype(str).str.replace('[\$,]', '', regex=True).astype(float)

print("=== (1) 每個商品的總庫存價值 ===")
df['Inventory_Value'] = df['Stock_Quantity'] * df['Unit_Price']
inventory_value_by_product = df.groupby('Product_Name')['Inventory_Value'].sum().reset_index()
inventory_value_by_product = inventory_value_by_product.sort_values(by='Inventory_Value', ascending=False)
print(inventory_value_by_product)
print("\n")

print("=== (2) 最暢銷商品 ===")
sales_by_product = df.groupby('Product_Name')['Sales_Volume'].sum().reset_index()
best_selling_product = sales_by_product.loc[sales_by_product['Sales_Volume'].idxmax()]
print(best_selling_product)
print("\n")

print("=== (3) 9折後的收入 ===")
df['Revenue'] = df['Sales_Volume'] * df['Unit_Price']
total_revenue_after_discount = df['Revenue'].sum() * 0.9
print(total_revenue_after_discount)