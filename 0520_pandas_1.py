import pandas as pd

data = [120, 80, None, 60, 95, None, 110]
stock1 = pd.Series(data)

indices = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Peach', 'Melon']
stock2 = pd.Series(data, index=indices)

stock3 = stock2.to_dict()

print("stock1")
print(stock1)
print()

print("stock2")
print(stock2)
print()

print("stock3")
print(stock3)
print()

print(f"Banana 庫存： {stock2['Banana']}")
print()

print("缺失值檢查：")
print(stock2.isna())
print()

print(f"缺失值數量： {stock2.isna().sum()}")

stock2.to_csv('0520_stock.csv')