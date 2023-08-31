import numpy as np
import pandas as pd
data=pd.read_csv("D:\student_score.csv")
print(data)
b=data.select_dtypes(include=[np.number])
x=b.mean()
print(x)
print(max(x))
data1 = {
    'Maths': [95, 87, 89, 64],
    'Science': [99, 88, 77, 66],
    'English': [87, 76, 65, 98],
    'History': [56, 67, 78, 89]
}
df = pd.DataFrame(data1)
print(df)
