import numpy as np

# Fuel efficiency of two car models (miles per gallon)
fuel_efficiency = np.array([25, 30])

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Calculate percentage improvement from Model 1 to Model 2
percentage_improvement = (
    (fuel_efficiency[1] - fuel_efficiency[0])
    / fuel_efficiency[0]
) * 100

print("Average fuel efficiency:", average_efficiency, "miles per gallon")
print("Percentage improvement:", percentage_improvement, "%")
