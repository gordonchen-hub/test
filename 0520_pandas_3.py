import pandas as pd

df = pd.read_csv('SuperMarket Analysis.csv')

branch_income = df.groupby('Branch')['gross income'].sum().round().astype(int).reset_index()
print("各分店的利潤(gross income)總和:")
for index, row in branch_income.iterrows():
    print(f"Branch {row['Branch']}: {row['gross income']}")
print("\n")

gender_product = df.groupby(['Gender', 'Product line'])['Quantity'].sum().reset_index()
top3_female = gender_product[gender_product['Gender'] == 'Female'].nlargest(3, 'Quantity')
top3_male = gender_product[gender_product['Gender'] == 'Male'].nlargest(3, 'Quantity')

print("各性別(Gender)喜歡購買的商品種類(Product line)前三名:")
print("Female")
for i, row in enumerate(top3_female.itertuples(), 1):
    print(f"{i}. {row._2} ({row.Quantity})")

print("Male")
for i, row in enumerate(top3_male.itertuples(), 1):
    print(f"{i}. {row._2} ({row.Quantity})")
print("\n")

product_rating = df.groupby('Product line')['Rating'].mean().round(2).reset_index()
worst_3 = product_rating.nsmallest(3, 'Rating')
print("評價(Rating)最差的3個商品種類:")
for i, row in enumerate(worst_3.itertuples(), 1):
    print(f"{i}. {row._1} ({row.Rating})")