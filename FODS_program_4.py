import numpy as np

# Sales for the four quarters
sales_data = np.array([10000, 12000, 15000, 18000])

# Calculate total annual sales
total_sales = np.sum(sales_data)

# Calculate percentage increase from Q1 to Q4
percentage_increase = (
    (sales_data[3] - sales_data[0]) / sales_data[0]
) * 100

print("Total annual sales:", total_sales)
print("Percentage increase from Q1 to Q4:", percentage_increase, "%")
