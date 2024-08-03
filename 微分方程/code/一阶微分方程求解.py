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


plt.rcParams['font.sans-serif'] = ['Simhei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

# 例题1
# 定义微分方程
def model(y, x):
    return np.exp(x)  # y' = e^x

# 定义初始条件
y0 = 1  # 初始条件 y(0) = 1

# 定义自变量范围
x = np.linspace(0, 2, 10)  # 从0到2之间取101个点

# 使用 odeint 求解微分方程
y_numerical = odeint(model, y0, x)

# 输出数值解（x, y）的形式
print("x, y values:")
for xi, yi in zip(x, y_numerical.flatten()):
    print(f"({xi:.4f}, {yi:.4f})")



# 例题2
def func19():
    # 定义微分方程
    def model(y, x):
        dydx = -y  # 这里的微分方程是 y' = -y
        return dydx

    # 定义初始条件
    y0 = 1

    # 定义时间点
    x = np.linspace(0, 5, 101) # x的取值范围是从0到5，一共101个点

    # 求解微分方程
    y = odeint(model, y0, x)   #调用odeint函数

    # 绘制结果
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Solution of the Differential Equation y' = -y")
    plt.show()

# 例题3
def func20():
    def dy_dt(y, t):  # 定义函数 f(y,t)
        return np.sin(t ** 2)  # 明确了这个微分方程为dy/dt=sin(t^2)
    y0 = [1]  # y0 = 1 也可以, 这明确了初值
    t = np.arange(-10, 10, 0.01)  # (start,stop,step)
    y = odeint(dy_dt, y0, t)  # 求解微分方程初值问题

    # 绘图
    plt.plot(t, y)
    plt.title("scipy.integrate.odeint")
    plt.show()

# 例题4（多元方程求解）
def func21():
    # 定义洛伦兹吸引子的微分方程
    def lorenz_system(state, t, sigma, rho, beta):
        x, y, z = state
        dxdt = sigma * (y - x)
        dydt = x * (rho - z) - y
        dzdt = x * y - beta * z
        return [dxdt, dydt, dzdt]

    # 定义参数值
    sigma = 10
    rho = 28
    beta = 8 / 3

    # 定义初始条件
    initial_state = [1.0, 0.0, 0.0]

    # 定义时间点
    t = np.linspace(0, 50, 10000)

    # 求解微分方程
    solution = odeint(lorenz_system, initial_state, t, args=(sigma, rho, beta))  
    # args这个参数指的是将参数传入我们自己定义好的函数中，这里是将sigma, rho, beta传入lorenz_system

    # 提取解的分量,进行转置
    x, y, z = solution.T

    # 绘制轨迹
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, lw=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Lorenz Attractor')
    plt.show()

if __name__ == '__main__':
    func21  ()