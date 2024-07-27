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
import numpy as np   # 以上是导入必须的算法库
def func8():
    '''
    最短路径
    :return:
    '''
    # 创建有向图
    G = nx.DiGraph() # 要注意导入networkx包

    # 添加带权边
    G.add_edge('A', 'B', weight=3)
    G.add_edge('A', 'C', weight=5)
    G.add_edge('B', 'C', weight=2)
    G.add_edge('B', 'D', weight=6)
    G.add_edge('C', 'D', weight=1)
    G.add_edge('D', 'E', weight=4)

    # 求解最短路径
    shortest_path = nx.shortest_path(G, 'A', 'E', weight='weight')  # 第一个位置是图，第二个位置是起点，第三个位置是终点，weight是权重, 默认是使用迪杰斯特拉算法, 如果想用贝尔曼福特，做如下修改：shortest_path = nx.shortest_path(G, 'A', 'E', weight='weight',method"bellman-ford")
    shortest_path_length = nx.shortest_path_length(G, 'A', 'E', weight='weight')

    # 打印结果
    print("最短路径:", shortest_path)
    print("最短路径长度:", shortest_path_length)

if __name__ == '__main__':
    func8()
