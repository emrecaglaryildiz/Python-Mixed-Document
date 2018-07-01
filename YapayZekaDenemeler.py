import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data=pd.read_csv("m2vefiyat.csv")
print(data)

x=data["metrekare"]
y=data["fiyat"]

x=pd.DataFrame.as_matrix(x)
x=pd.DataFrame.as_matrix(y)

print(x)
print(y)

plt.scatter(x,y)
