from scipy.optimize import linprog
from scipy.optimize import minimize
from pulp import LpMaximize, LpProblem, LpVariable
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import quad
from scipy.optimize import curve_fit
from scipy.integrate import odeint
import seaborn as sns
import numpy as np   #以上是导入必须的算法库

def func17():
    # 定义要拟合的函数形式
    def func(x, a, b, c):
        return a * np.exp(-b * x) + c

    # 生成一些带有噪声的示例数据
    x_data = np.linspace(0, 4, 50)
    y_data = func(x_data, 2.5, 1.3, 0.5) + 0.2 * np.random.normal(size=len(x_data))

    # 使用 curve_fit 进行拟合
    popt, pcov = curve_fit(func, x_data, y_data) # 先导入这个包：from scipy.optimize import curve_fit

    # 绘制原始数据和拟合结果
    plt.scatter(x_data, y_data, label='Original Data')
    plt.plot(x_data, func(x_data, *popt), 'r-', label='Fitted Curve')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Curve Fitting Example')
    plt.show()

    # 输出拟合参数
    print('拟合参数:', popt)