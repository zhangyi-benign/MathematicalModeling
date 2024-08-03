import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
#以上是导入必须的算法库


plt.rcParams['font.sans-serif'] = ['Simhei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

# 例题2
def func22():
    # 导数函数，求 Y=[u,v] 点的导数 dY/dt
    def deriv(Y, t, a, w): # a，w都是微分方程的常系数
        u, v = Y  # Y=[u,v]
        dY_dt = [v, -2 * a * v - w * w * u]  # 因为是缺x形的二阶微分方程，因此使用降阶，可化为两个1阶方程
        return dY_dt

    t = np.arange(0, 20, 0.01)  # 创建时间点 (start,stop,step)
    # 设置导数函数中的参数 (a, w)，题目背景会告诉什么是过阻尼，欠阻尼，临界阻尼
    paras1 = (1, 0.6)  # 过阻尼：a^2 - w^2 > 0
    paras2 = (1, 1)  # 临界阻尼：a^2 - w^2 = 0
    paras3 = (0.3, 1)  # 欠阻尼：a^2 - w^2 < 0

    # 调用ode对进行求解, 用两个不同的初始值 W1、W2 分别求解
    Y0 = (1.0, 0.0)  # 定义初值为 Y0=[u0,v0]
    Y1 = odeint(deriv, Y0, t, args=paras1)  # args 设置导数函数的参数
    Y2 = odeint(deriv, Y0, t, args=paras2)  # args 设置导数函数的参数
    Y3 = odeint(deriv, Y0, t, args=paras3)  # args 设置导数函数的参数
    # W2 = (0.0, 1.01, 0.0)  # 定义初值为 W2
    # track2 = odeint(lorenz, W2, t, args=paras)  # 通过 paras 传递导数函数的参数

    # 绘图
    plt.plot(t, Y1[:, 0], 'r-', label='u1(t)')
    plt.plot(t, Y2[:, 0], 'b-', label='u2(t)')
    plt.plot(t, Y3[:, 0], 'g-', label='u3(t)')
    plt.plot(t, Y1[:, 1], 'r:', label='v1(t)')
    plt.plot(t, Y2[:, 1], 'b:', label='v2(t)')
    plt.plot(t, Y3[:, 1], 'g:', label='v3(t)')
    plt.axis([0, 20, -0.8, 1.2])
    plt.legend(loc='best')
    plt.title("Second ODE by scipy.integrate.odeint")
    plt.show()


# 例题3
# 定义微分方程组
def system(variables, x):
    """
    定义微分方程组
    :param variables: 包含 y 和 v 的列表
    :param x: 自变量
    :return: 微分方程的解
    """
    y, v = variables  # 从输入的变量中解包 y 和 v
    dydx = v  # y 关于 x 的导数等于 v
    dvdx = np.sqrt(1 + v**2) / (2 * x)  # v 关于 x 的导数，基于给定的微分方程
    return [dydx, dvdx]

# 初始条件
y0 = 0  # x=16 时 y 的初始值
v0 = 0  # x=16 时 v 的初始值
initial_conditions = [y0, v0]  # 初始条件的列表

# 定义x的范围
x_values = np.arange(16, 0.1, -0.04)  # 从 16 到 0.1，步长为 -0.04 的 x 值数组

# 求解微分方程组
solution = odeint(system, initial_conditions, x_values)
# odeint 函数用于求解微分方程组，返回的 solution 包含 y 和 v 的解

# 提取解
y_solution = solution[:, 0]  # 从 solution 中提取 y 的解
v_solution = solution[:, 1]  # 从 solution 中提取 v 的解

# 绘图
plt.figure()  # 创建一个新的绘图窗口
plt.plot(x_values, y_solution, label='y(x)')  # 绘制 y 关于 x 的图像
plt.xlabel('x')  # x 轴标签
plt.ylabel('y')  # y 轴标签
plt.title('y(x) 关系图')  # 图形标题
plt.legend()  # 显示图例
plt.grid()  # 显示网格
plt.show()  # 显示图形