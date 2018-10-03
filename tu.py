# -*- coding: utf-8 -*-
import sys
import math
reload(sys)
sys.setdefaultencoding('utf8')
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate
import matplotlib.gridspec as gridspec

# num = 20
# k = 2
# b = 3
# noise = np.random.rand(num) * 3
# x = np.arange(num)
# y = -4.44*x*x*x+20*x*x+15
#
# c_linspl = interpolate.splrep(x, y, k=1)
# x_linspl = np.arange(0, num, 0.1)
# y_linspl = interpolate.splev(x_linspl, c_linspl, der=0)
#
# c_quadratic_spl = interpolate.splrep(x, y, k=2)
# x_quadratic_spl = np.arange(0, num, 0.1)
# y_quadratic_spl = interpolate.splev(x_quadratic_spl, c_quadratic_spl, der=0)
#
# c_cubic_spl = interpolate.splrep(x, y, k=3)
# x_cubic_spl = np.arange(0, num, 0.1)
# y_cubic_spl = interpolate.splev(x_quadratic_spl, c_quadratic_spl, der=0)
#
# gs = gridspec.GridSpec(2, 2)
# fig = plt.figure()
# plt.title(u"Matplotlib 样条差值比较", fontsize=20)
# p1 = fig.add_subplot(gs[0, 0])
# p2 = fig.add_subplot(gs[0, 1])
# p3 = fig.add_subplot(gs[1, 0])
# p4 = fig.add_subplot(gs[1, 1])
#
# p1.plot(x, y)
# p2.plot(x_linspl, y_linspl)
# p3.plot(x_quadratic_spl, y_quadratic_spl)
# p4.plot(x_cubic_spl, y_cubic_spl)
#
# # p1.set_title(u"原图")
# # p2.set_title(u"一次样条差值（直线）")
# # p3.set_title(u"二次样条差值")
# # p4.set_title(u"三次样条差值")
#
# plt.show()

pList =[]
qList =[]
for x in np.arange(0,3,0.05):
    y = -4.44*x*x*x+20*x*x+15
    pList.append(y)
    qList.append(x)
    #print size(pList)
    print pList
    print qList
plt.plot(qList,pList,x,marker='o')
plt.show()