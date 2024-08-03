import numpy as np
from scipy.integrate import quad


def func16():
    # 定义被积函数
    def integrand(x):
        return x ** 2

    # 定义积分区间
    a = 0  # 下限
    b = 1  # 上限

    # 进行积分计算
    result, error = quad(integrand, a, b) # 要先导入这个包：from scipy.integrate import quad   ； quad是python计算一维积分的函数，会返回两个值，一个是计算结果，另一个是计算误差

    # 显示结果
    print("积分结果:", result)
    print("估计误差:", error)