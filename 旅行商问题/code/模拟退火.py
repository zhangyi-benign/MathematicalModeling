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

def func14():   # 模拟退火解决二元函数问题
    # 定义目标函数
    def fun(x):
        return x[0] * np.sin(np.pi * x[0]) + x[1] * np.cos(4 * np.pi * x[1])

    # 参数初始化
    narvs = 2  # 变量个数为2个，因为式子中，一个变量是x，一个变量是y
    T0 = 1000  # 初始温度
    T = T0  # 迭代中温度会发生改变，第一次迭代时温度就是T0
    maxgen = 1000  # 最大迭代次数
    Lk = 300  # 每个温度下的迭代次数
    alfa = 0.95  # 温度衰减系数
    x_lb = np.array([-3, 4])  # x的下界，即（-3，4）
    x_ub = np.array([3, 5])  # x的上界，即，（3，5）

    # 随机生成一个初始解
    x0 = np.random.rand(narvs) * (x_ub - x_lb) + x_lb  # 取值范围是x_ub到x_lb
    y0 = fun(x0)  # 计算当前解的函数值

    # 定义一些保存中间过程的量
    max_y = y0  # 初始化找到的最佳的解对应的函数值为y0

    # 模拟退火过程
    for iter in range(maxgen):  # 外循环, 指定最大迭代次数
        for i in range(Lk):  # 内循环，在每个温度下开始迭代
            y = np.random.randn(narvs)  # 生成N(0,1)随机数
            z = y / np.sqrt(np.sum(y ** 2))  # 为了方便计算，进行标准化z
            x_new = x0 + z * T  # 跳到随机产生的x附近的x_new

            # 调整新解的位置，使其在定义域内
            for j in range(narvs):
                if x_new[j] < x_lb[j]:
                    r = np.random.rand()
                    x_new[j] = r * x_lb[j] + (1 - r) * x0[j]
                elif x_new[j] > x_ub[j]:
                    r = np.random.rand()
                    x_new[j] = r * x_ub[j] + (1 - r) * x0[j]

            x1 = x_new.copy()  # 将调整后的x_new赋值给新解x1
            y1 = fun(x1)  # 计算新解的函数值
            if y1 > y0:  # 如果新解函数值大于当前解的函数值
                x0 = x1.copy()  # 更新当前解为新解
                y0 = y1
            else:
                p = np.exp(-(y0 - y1) / T)  # 计算一个概率
                if np.random.rand() < p:  # 生成一个随机数和这个概率比较，如果该随机数小于这个概率
                    x0 = x1.copy()  # 更新当前解为新解。这在一定程度上优化了贪心遇到的难题。因为对于不优秀的解，也有概率被选择。
                    y0 = y1

            # 判断是否要更新找到的最佳的解
            if y0 > max_y:  # 如果当前解更好，则对其进行更新
                max_y = y0  # 更新最大的y
                best_x = x0.copy()  # 更新找到的最好的x

    print('取最大值时的根是：', best_x)
    print('此时对应的最大值是：', max_y)



def func15(): 
    '''
    模拟退火解决旅行商问题
    :return:
    '''
    # 从 Excel 加载数据
    coord = pd.read_excel('distance.xlsx', header=None).values
    print("加载的数据：\n", coord)
    print("数据的形状：", coord.shape)

    n = coord.shape[0]  # 城市数目
    print(n)
    # 计算任意两个城市的距离矩阵
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            dist[i, j] = coord[i, j]
    dist = dist + dist.T  # 生成距离矩阵的上三角部分

    # 模拟退火参数设置
    T0 = 1000  # 初始温度
    T = T0  # 当前温度
    maxgen = 1000  # 最大迭代次数
    Lk = 20  # 每个温度下的迭代次数
    alfa = 0.95  # 温度衰减系数

    # 随机生成一个初始解
    path0 = np.arange(2, n + 1)  # 从城市2开始
    np.random.shuffle(path0)  # 随机打乱路径
    path0 = np.concatenate(([1], path0, [1]))  # 起点和终点均为城市1

    def calculate_tsp(path):
        result = 0  # 初始化该路径走的距离为0
        for i in range(len(path) - 1):
            result += dist[path[i] - 1, path[i + 1] - 1]  # 计算给定路径的代价
        return result

    result0 = calculate_tsp(path0)
    print("初始路径：", path0)
    print("初始路径长度：", result0)

    # 定义保存中间结果的变量
    min_result = result0
    RESULT = np.zeros(maxgen)
    best_path = np.copy(path0)  # 初始化 best_path

    # 模拟退火过程
    for iter in range(maxgen):
        for i in range(Lk):
            # 生成新的路径，避免重复城市
            path1 = np.copy(path0[1:-1])
            np.random.shuffle(path1)
            path1 = np.concatenate(([1], path1, [1]))  # 加上起点和终点
            result1 = calculate_tsp(path1)  # 计算新路径的距离
            if result1 < result0 or np.random.rand() < np.exp(-(result1 - result0) / T):
                path0 = np.copy(path1)
                result0 = result1
            if result0 < min_result:
                min_result = result0
                best_path = np.copy(path0)
        RESULT[iter] = min_result
        T = alfa * T

    # 打印最佳方案和最优值
    print("最佳路径是：", best_path)
    print("对应最优值是：", min_result)

    # 绘制最优路径
    plt.figure()
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    for i in range(n):
        x[i] = coord[best_path[i] - 1, 0]
        y[i] = coord[best_path[i] - 1, 1]
    x[-1] = coord[best_path[0] - 1, 0]
    y[-1] = coord[best_path[0] - 1, 1]

    plt.plot(x, y, 'o-')
    plt.title('最佳路径')
    plt.xlabel('X坐标')
    plt.ylabel('Y坐标')
    plt.grid(True)

    plt.show()  # 显示图形
    print("图形已显示")
    plt.close()  # 关闭当前图形，释放资源

if __name__ == '__main__':
    func14 ()
