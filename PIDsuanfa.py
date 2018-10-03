# -*- coding: utf-8 -*-
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

P=0.6
I=0.00001
D=1000
jifenpiancha=0
pwm=0
a=0
b=500
c=0

def pid(qishi,mubiao,lastpiancha):
    #pid(qishi,mubiao,lastpiancha)
    global jifenpiancha
    global pwm
    piancha=b-qishi
    jifenpiancha+=piancha
    bili=P * piancha / 100
    jifen=I * jifenpiancha / 100
    weifen=(piancha - lastpiancha) / 100
    if jifen>=2*b:
        print "积分太大"
    else:
        pwm+=bili+jifen+weifen
        lastpiancha=piancha
    return pwm
def pid1(qishi,mubiao,lastpiancha):
    global jifenpiancha
    global pwm
    piancha = b - qishi
    jifenpiancha += piancha
    bili = P * piancha / 100
    jifen = I * jifenpiancha / 100
    weifen=(piancha - lastpiancha) / 100
    if jifen >= 2 * b:
        print "积分太大"
    else:
        pwm += bili + jifen + weifen
        lastpiancha = piancha
    return lastpiancha


d=pid(a,b,c)
lastpiancha=pid1(a,b,c)
i=0
q=0
pList =[]
qList=[]
for i in range(0,500,1):
#while True:
    print pid(d,b,lastpiancha),pid1(d,b,lastpiancha)
    # plt.plot(d,lastpiancha,marker='o')
    # plt.show()

    pList.append(pid(d,500,lastpiancha))
    qList.append(i)
    if d==b:
        break
    d=pid(d,500,lastpiancha)
    time.sleep(0.001)
    lastpiancha=pid1(d,500,lastpiancha)
    i+=1
plt.plot(qList,pList,marker='o')
plt.show()

