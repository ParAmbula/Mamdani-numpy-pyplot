import matplotlib.pyplot as plt
import numpy as np
out=[0,0,0]
y1=[]
y2=[]
y3=[]
rules=[[0,0,0],[0,0,0],[0,0,0]]
with open('In1.txt') as f:
    data1 =[]
    for eachLine in f:
        numbers=eachLine.strip().split()
        number=[float(x) for x in numbers[0].strip('[]').split(',')]
        data1.append(number)
for i in data1:
    y1.append([0,1,1,0])
with open('In2.txt') as f:
    data2 =[]
    for eachLine in f:
        numbers=eachLine.strip().split()
        number=[float(x) for x in numbers[0].strip('[]').split(',')]
        data2.append(number)
for i in data2:
    y2.append([0,1,1,0])
with open('SinTone.txt') as f:
    data3 =[]
    for eachLine in f:
        numbers=eachLine.strip().split()
        number=[float(x) for x in numbers[0].strip('[]').split(',')]
        data3.append(number)
for i in data3:
    y3.append([0,0,0,0])
fig=plt.figure()
ax_1=fig.add_subplot(3,1,1)
ax_2=fig.add_subplot(3,1,2)
ax_3=fig.add_subplot(3,1,3)
xzad1=input('Введите точку на линии абсцисс для входа 1 \n')
xzad2=input('Введите точку на линии абсцисс для входа 2 \n')
print('Вход №1')
u1=[]
for i, item in enumerate(data1):
    μ1=np.interp(xzad1, data1[i],y1[i])
    u1.append(μ1)
print('Принадлежность слабому множеству №',1,' - ',u1[0])
print('Принадлежность среднему множеству №',2,' - ',u1[1])
print('Принадлежность сильному множеству №',3,' - ',u1[2])
print('=================================')
print('Вход №2')
u2=[]
for i, item in enumerate(data2):
    μ2=np.interp(xzad2, data2[i],y2[i])
    u2.append(μ2)
print('Принадлежность слабому множеству №',1,' - ',u2[0])
print('Принадлежность среднему множеству №',2,' - ',u2[1])
print('Принадлежность сильному множеству №',3,' - ',u2[2])
if u1[0] and u2[0] !=0:
    dis1 = min(u1[0], u2[0])
elif u1[0]==0:
    dis1=u2[0]
else:
    dis1=u1[0]
if u1[1] and u2[1] !=0:
    dis2 = min(u1[1], u2[1])
elif u1[1] == 0:
    dis2 = u2[1]
else:
    dis2 = u1[1]
if u1[2] and u2[2] !=0:
    dis3 = min(u1[2], u2[2])
elif u1[2] == 0:
    dis3=u2[2]
else:
    dis3 = u1[2]
print('=================================')
print('Конъюнкция слабых множеств 1 = '+str(dis1))
print('Конъюнкция средних множеств 2 = '+str(dis2))
print('Конъюнкция сильных множеста 3 = '+str(dis3))
rules[0][0]=min(u1[0],u2[0])
rules[0][1]=min(u1[1],u2[0])
rules[0][2]=min(u1[2],u2[0])
rules[1][0]=min(u1[0],u2[1])
rules[1][1]=min(u1[1],u2[1])
rules[1][2]=min(u1[2],u2[1])
rules[2][0]=min(u1[0],u2[2])
rules[2][1]=min(u1[1],u2[2])
rules[2][2]=min(u1[2],u2[2])
out[0]=max(max(rules[0][0],rules[1][0]),rules[2][0])
out[1]=max(max(rules[0][1],rules[2][1]),rules[0][2])
out[2]=max(max(rules[1][1],rules[1][2]),rules[2][2])
y3[0][1]=out[0]
y3[1][1]=out[1]
y3[2][1]=out[2]
for i, item in enumerate(data1):
   ax_1.plot(data1[i],y1[i])
for i, item in enumerate(data2):
   ax_2.plot(data2[i],y2[i])
for i, item in enumerate(data3):
    ax_3.plot(data3[i],y3[i])
ax_1.grid(1)
ax_2.grid(1)
ax_3.grid(1)
print(out)
print('Tаблица правил\n B\S L M H\n   L l m m\n   M l h h\n   H l m h')
print(rules[0])
print(rules[1])
print(rules[2])
Out1=(out[0]*(-1)+out[1]*0+out[2]*1)/(out[0]+out[1]+out[2])
print("Выходная, полученный методом центра тяжести для single-tone = "+str(Out1))
plt.show()
