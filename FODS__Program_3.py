import numpy as np

# Columns: bedrooms, bathrooms, square feet, sale price
house_data = np.array([
    [3, 2, 1500, 200000],
    [5, 3, 2500, 350000],
    [4, 2, 2000, 280000],
    [6, 4, 3000, 450000],
    [5, 2, 2200, 400000]
])

# Select houses with more than 4 bedrooms
selected_houses = house_data[house_data[:, 0] > 4]

# Calculate average sale price
average_price = np.mean(selected_houses[:, 3])

print("Average sale price of houses with more than 4 bedrooms:", average_price)
