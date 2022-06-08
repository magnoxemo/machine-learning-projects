#model linear regression 
from scipy.linalg import solve
import matplotlib.pyplot as plt

import math
#dataset
y=[]
x=[]
x1=[]
y2=[]
for i in range (1000):
    x.append(i)
    x1.append(i**2)
    y.append(12*i-50)
    y2.append(x[i]*y[i])
plt.figure(figsize=(10,6))
plt.plot(x,y,color="r")





#model coding
matric=[[len(x),sum(x)],
        [sum(x),sum(x1)]]

b=[sum(y),sum(y2)]
s=solve(matric,b)


def prediction(x,s):
    return s[1]*x+s[0]
x_predict=[]
y_predict=[]
for i in range (1000):
    x_predict.append(i)
    y_predict.append(prediction(i,s))


plt.scatter(x_predict,y_predict,color="green")
