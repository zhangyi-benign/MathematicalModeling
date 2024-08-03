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

def func13():
    A = np.array([[0, 56, 21, 35],
                  [56, 0, 49, 39],
                  [21, 49, 0, 77],
                  [35, 39, 77, 0]])

    L = A.shape[0]
    c = [0, 1, 2, 3, 0]  # 初始圈

    for k in range(L):
        flag = 0  # 修改标志
        for i in range(L - 2):  # i是第一条弧的起点
            for j in range(i + 2, L):  # j是第二条弧的起点
                if A[c[i], c[j]] + A[c[i + 1], c[j + 1]] < A[c[i], c[i + 1]] + A[c[j], c[j + 1]]:
                    c[i + 1:j + 1] = c[j:i:-1]  # 翻转中间的路径，注意索引的范围
                    flag += 1
        if flag == 0:  # 本轮没有找到更短的弧
            long = 0  # 圈长
            for i in range(L):
                long += A[c[i], c[i + 1]]
            print("最短路径：", c, "路径长度：", long)
            break
if __name__ == '__main__':
    func13 ()