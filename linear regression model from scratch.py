#model linear regression 
import matplotlib.pyplot as plt 
from scipy.linalg import solve
import numpy 

y=[]
x=[]
x1=[]
y2=[]
for i in range (100):
    x.append(i)
    x1.append(i**2)
    y.append(2*i+numpy.random.randint(20,50))
    y2.append(x[i]*y[i])
plt.figure(figsize=(10,6))
plt.scatter(x,y,color="r")





#model coding
matric=[[len(x),sum(x)],
        [sum(x),sum(x1)]]

b=[sum(y),sum(y2)]
s=solve(matric,b)


def prediction(x,s):
    return s[1]*x+s[0]
x_predict=[]
y_predict=[]
for i in range (150):
    x_predict.append(i)
    y_predict.append(prediction(i,s))


plt.plot(x_predict,y_predict,color="green")
