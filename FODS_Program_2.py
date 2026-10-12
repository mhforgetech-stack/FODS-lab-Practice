python

import numpy as np

sales = np.array([
  [100,200,300]
  [150,250,350]
  [200,300,400]
])

average_price  = np.mean(sales)

print("average price of all products:",average_price)
