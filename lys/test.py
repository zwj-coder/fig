###最小二乘法试验###
import numpy as np
from scipy.optimize import leastsq

###采样点(Xi,Yi)###
Xi = np.array([0, 1, 2, 3, -1, -2, -3])
Yi = np.array([-1.21, 1.9, 3.2, 10.3, 2.2, 3.71, 8.7])


###需要拟合的函数func及误差error###
def func(p, x):
    a, b, c = p
    return a * x ** 2 + b * x + c


def error(p, x, y):
    return func(p, x) - y  # x、y都是列表，故返回值也是个列表


# TEST
p0 = [5, 2, 10]
# print( error(p0,Xi,Yi) )

###主函数从此开始###
s = "Test the number of iteration"  # 试验最小二乘法函数leastsq得调用几次error函数才能找到使得均方误差之和最小的a~c
Para = leastsq(error, p0, args=(Xi, Yi))  # 把error函数中除了p以外的参数打包到args中
a, b, c = Para[0]

###绘图，看拟合效果###
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(Xi, Yi, color="red", label="Sample Point", linewidth=3)  # 画样本点
x = np.linspace(-5, 5, 1000)
y = a * x ** 2 + b * x + c
plt.plot(x, y, color="orange", label="Fitting Curve", linewidth=2)  # 画拟合曲线
plt.legend()
plt.show()
