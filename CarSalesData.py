import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


#car_sales_data= [brand, model, year, sales_quantity, price]

car_sales_data = np.array([
    ["Toyota", "Camry", 2022, 100, 25000],                  
    ["Honda", "Civic", 2023, 120, 23000],
    ["Toyota", "Corolla", 2022, 150, 22000],
    ["Ford", "Fusion", 2024, 80, 27000],
    ["Honda", "Accord", 2023, 110, 28000],
])

sales_column = car_sales_data[:, 3].astype(int)
total_sales = sales_column.sum()

price_column = car_sales_data[:, 4].astype(int)
average_price = price_column.mean()

most_common_brand = Counter(car_sales_data[:, 0]).most_common(1)[0][0]

print("Summary Statistics:")
print(f"Total Sales: {total_sales}")
print(f"Average Price: {average_price}")
print(f"Most Common Brand: {most_common_brand}")

brand_sales = Counter(car_sales_data[:, 0])
most_common_brand_sales = brand_sales.most_common(1)[0]
print(f"\nMost Common Brand: {most_common_brand_sales[0]} (Sales: {most_common_brand_sales[1]})")

brands = list(brand_sales.keys())
sales = list(brand_sales.values())

plt.figure(figsize=(10, 6))
plt.bar(brands, sales, color='skyblue')
plt.xlabel('Brand')
plt.ylabel('Sales')
plt.title('Sales by Brand')
plt.xticks(rotation=45)
plt.show()




