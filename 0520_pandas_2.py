import pandas as pd

data_dict = {
    'Product': ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava'],
    'Price': [30, 20, 25, 60, 45, 35],
    'Sales': [100, 150, 80, 60, 90, 54]
}
df_dict = pd.DataFrame(data_dict)

data_list = [
    ['Apple', 30, 100],
    ['Banana', 20, 150],
    ['Orange', 25, 80],
    ['Mango', 60, 60],
    ['Grape', 45, 90],
    ['Guava', 35, 54]
]
df_list = pd.DataFrame(data_list, columns=['Product', 'Price', 'Sales'])

df = df_dict

print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.count())

stats = df.describe().round(2)
print(stats)

stats.to_csv('0520_stock2.csv')