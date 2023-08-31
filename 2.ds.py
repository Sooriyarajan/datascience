import numpy as np
import pandas as pd
data = pd.read_csv("D:/company.csv")
products = pd.DataFrame(data)
products.index = ['jan', 'feb', 'mar']
print(products)
mean_columns = np.mean(products, axis=1)
print(mean_columns)
allprod = np.mean(mean_columns)
print(allprod)

arr = products.to_numpy()
arr.shape = (3, 3)
print(arr)
