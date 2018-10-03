# -*- coding: utf-8 -*-
import numpy as np
import sys
import time

reload(sys)
sys.setdefaultencoding('utf8')
import matplotlib.pyplot as plt
list=[]
list1=[]
def gh(qishi,zhongzhi,miao):
    a0=qishi
    a2=(3./(miao*miao))*(zhongzhi-qishi)
    a3=(-2./(miao*miao*miao))*(zhongzhi-qishi)
    theta=a0+a2*t*t+a3*t*t*t
    list.append(theta)
    return theta
for t in np.arange(0,5,0.01):#时间范围和间隔
    list1.append(t)
    #print gh(2,8,5)
    time.sleep(0.001)
    print gh(1500,2000,5)
plt.plot(list1,list,marker='o')
plt.show()
