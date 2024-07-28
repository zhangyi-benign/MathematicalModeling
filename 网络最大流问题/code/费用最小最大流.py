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


def func12():
    # 容量矩阵
    c = [
        [0, 15, 10, 20, 0, 0, 0, 0],
        [0, 0, 0, 0, 7, 10, 0, 0],
        [0, 0, 0, 0, 0, 8, 2, 0],
        [0, 0, 0, 0, 0, 0, 18, 0],
        [0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 16],
        [0, 0, 0, 0, 0, 0, 0, 20],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # 费用矩阵
    cost = [
        [float('inf'), 8, 10, 15, float('inf'), float('inf'), float('inf'), float('inf')],
        [float('inf'), float('inf'), float('inf'), float('inf'), 9, 11, float('inf'), float('inf')],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 8, 6, float('inf')],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 14, float('inf')],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 8],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 9],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 10],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
    ]

    # 创建空的有向图
    G = nx.DiGraph()

    # 遍历容量矩阵和费用矩阵，将非零元素作为边添加到图中
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] != 0:
                # 添加边并设置容量和费用属性
                G.add_edge(i, j, capacity=c[i][j], weight=cost[i][j])

    # 打印图的节点和边
    print("节点:", G.nodes())
    print("边:", G.edges(data=True))

    # 使用最小费用最大流算法求解
    flow_dict = nx.max_flow_min_cost(G, 0, 7)

    # 计算最小费用
    min_cost = nx.cost_of_flow(G, flow_dict)

    # 打印结果
    print("最小费用:", min_cost)
    print("最大流分配:", flow_dict)

    # 绘制有向网络图
    pos = {'s': (0, 5), 'v1': (2, 8), 'v2': (2, 6), 'v3': (2, 4), 'v4': (4, 8), 'v5': (4, 6), 'v6': (4, 4), 't': (6, 5)}  # 指定顶点绘图位置
    # 设置节点布局 https://networkx.org/documentation/stable/reference/generated/networkx.drawing.layout.spring_layout.html

    max_flow = {
        0: {1: 14, 2: 10, 3: 18},  # 最终：0和1相连，流量为14；0和2相连，流量为10；0和3相连，流量为18。
        1: {4: 6, 5: 8},   # 其他节点的表示方法和0节点一样，都是看和哪个节点相连，流量是多少。（有方向要求）
        2: {5: 8, 6: 2},
        3: {6: 18},
        4: {7: 6},
        5: {7: 16},
        6: {7: 20},
        7: {}
    }

    # 创建有向图
    G = nx.DiGraph()

    # 添加边和流量属性
    for u, neighbors in max_flow.items():    # u和neighbors是max_flow.items()的两个项。用items打开max_flow，发现有两种数据，第一种是0到7，第二种是大括号里面的数据。用u和neighbors分别去接收这些数据
        for v, flow in neighbors.items():    # 用items打开neighbors。即出现 1：4，2：10，3：18 这样类型的数据。用v记录下1，2，3···这些节点，用flow记录下14，10，18···这些流量
            G.add_edge(u, v, flow=flow, capacity=c[u][v])    # 用flow记录下每段弧的流量。用capacity记录下每段弧的最大容量

    # 成功分别存储好这些不同的数据包后，就可以开始绘制图形
    pos = nx.spring_layout(G)  # 设置节点布局
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)  # 绘制节点和边，定义了节点和边的类型

    # 绘制权重标签
    edge_labels = {(u, v): f"最大容量: {d['capacity']}\n流量: {d['flow']}"
                   for u, v, d in G.edges(data=True)}  # 把每段弧的起点u、终点v、最大容量和流量d作为一个数据结构，存储到G.edge中。d的数据是这样产生的：使用capacity和flow作为指引，查找数据
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=4)

    plt.title('Max Flow Allocation')  # 设置标题
    plt.show()  # 显示图形