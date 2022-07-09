#polynomial fitting curve 
from ctypes import sizeof
import pandas as pd 
from scipy.linalg import solve 
import matplotlib.pyplot as plt 
import numpy 

""" now creating a matrix of size (N+1)x(N+1) where n is the degree of the polynomial fitting curve """
#N=int(input("degree of the fitting: "))
N=5
matrix=np.zeros(shape=(N+1,N+1))

"""preloaded data """
data_file=pd.read_csv('/home/walid/Desktop/diabetes.csv')
data_file.head()
x=data_file["Insulin"]
x=np.array(x)
y=np.array(data_file["Glucose"])

"""data is preloaded """
for i in range (N+1):
    for j in range(N+1):
        
        x1=[]
        if i==0 and j==0:
            matrix[i][j]=len(x)
        else: 
            for k in range (len(x)):
                x1.append((x[k])**(i+j))
                
            matrix[i][j]=sum(x1)
            

"""  matrix formation is done now.I have to code the constant vector   """

constant_vactor=[]
for i in range(N+1):
    if i==0:
        constant_vactor.append(sum(y))
    else:
        constant_vactor.append(sum(x**i*y))
s=[]
s=solve(matrix,constant_vactor)

def prediction(s,x,N):
    s=np.array(s)
    values=[]
    for i in range ( N+1):
        values.append(x**i)
    values=np.array(values)

    return sum(s*values)
    

x_predict=[]
y_predict=[]

for i in range (1000):
    x_predict.append(i)
    y_predict.append(prediction(s,i,N))



plt.figure(figsize=(10,6))
plt.scatter(x,y,color="r")
plt.plot(x_predict,y_predict,color="green")
