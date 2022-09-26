import numpy as np 
import matplotlib.pyplot as plt
x=[]
y=[]
i=-20
while i<20:
    x.append(i)
    y.append(3+i*4)
    i=i+0.01
##################### data is done ##################
#################################################################################################
learning_rate=0.000001
initial_guess=[0,0]

def hypothesis(value):

    return initial_guess[0]*value+initial_guess[1]

epocs=1000
iteration_num=0
while epocs>iteration_num:
    iteration_num=iteration_num+1
    for i in range(len(initial_guess)):
        delta=0

        for j in range(len(y)):
            delta=delta+(y[j]-hypothesis(x[j]))*x[j]
        initial_guess[i]=initial_guess[i]+learning_rate*delta

initial_guess=np.array(initial_guess)
x=np.array(x)
y_new=x*initial_guess[0]+initial_guess[1]

plt.figure(figsize=(10,6))
plt.plot(x,y_new,color="red")
plt.plot(x,y)
plt.show()
