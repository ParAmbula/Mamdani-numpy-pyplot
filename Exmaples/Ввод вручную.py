import matplotlib.pyplot as plt
import numpy as np
import itertools as it
y=[]
data=[]
print("Введите количество множеств")
kolvo=int(input())
for i in range(kolvo):
    y.append([0,1,1,0])
    data.append([0,0,0,0])
for z in range(kolvo):
    for i in range(4):
        data[z][i]=(float(input()))
plt.xlabel('x')
plt.ylabel('μ(x)')
plt.grid(True)
for i, item in enumerate(data):
    plt.plot(data[i],y[i])
print('Вывести полученные результаты в отдельном окне?')
show=input('Да Нет \n')
xzad=input('Введите точку на линии абсцисс \n')
for i, item in enumerate(data):
    μ=np.interp(xzad, data[i],y[i])
    print('Принадлежность множеству №',i,' - ',μ)
if show=='Да':
    plt.show()