# 使用大量随机数进行估算
import random
import math
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体，以确保中文标签能够正确显示
font = FontProperties(fname='C:/Windows/Fonts/simhei.ttf')  # 使用黑体，确保路径正确


def buffon_needle_simulation_plot(a, L, n):
    """
    蒲丰投针实验模拟函数，通过模拟抛掷针计算圆周率，并生成图形。

    参数：
    a - 平行线之间的距离
    L - 针的长度
    n - 抛掷次数

    返回值：
    estimated_pi - 估算的圆周率
    """
    # 生成 n 个随机角度，范围在 [0, pi] 之间
    angles = [random.uniform(0, math.pi) for _ in range(n)]

    # 生成 n 个随机距离，范围在 [0, a / 2] 之间
    distances = [random.uniform(0, a / 2) for _ in range(n)]

    # 计算每个角度对应的边界值，边界值公式为 (L / 2) * sin(角度)
    y = [(L / 2) * math.sin(angle) for angle in angles]

    # 初始化相交次数计数器
    intersections = 0

    # 设置绘图窗口的大小
    plt.figure(figsize=(10, 5))

    # 遍历每一个随机生成的角度和距离
    for i in range(n):
        # 如果距离小于等于计算出的边界值，则表示针与平行线相交
        if distances[i] <= y[i]:
            intersections += 1
            # 绘制每次相交的点，颜色为蓝色，点的大小为1
            plt.plot(angles[i], distances[i], 'b.', markersize=1)

    # 计算相交的概率 P
    P = intersections / n
    # 使用公式 2 * L / (P * a) 估算圆周率 π 的值
    estimated_pi = 2 * L / (P * a)

    # 绘制相交边界线，这里绘制底部的水平线
    plt.axhline(y=0, color='r', linestyle='-', label='相交边界')  # 红色直线表示相交边界

    # 设置图表的 x 轴标签
    plt.xlabel('角度（弧度）', fontproperties=font)
    # 设置图表的 y 轴标签
    plt.ylabel('距离最近线的距离', fontproperties=font)
    # 设置图表的标题
    plt.title('蒲丰投针实验模拟', fontproperties=font)
    # 显示图例
    plt.legend(prop=font)
    # 显示网格线
    plt.grid(True)
    # 设置坐标轴的范围
    plt.axis([0, math.pi, 0, a / 2])

    # 绘制图像
    plt.draw()
    # 暂停以确保图表可以显示
    plt.pause(0.1)

    # 返回估算的圆周率值
    return estimated_pi


# 参数设置
a = 10  # 平行线之间的距离
L = 5  # 针的长度
n = 10000  # 抛掷次数

# 运行模拟并绘制结果
estimated_pi = buffon_needle_simulation_plot(a, L, n)

# 输出估算的圆周率
print(f"通过蒲丰投针实验估计的圆周率: {estimated_pi:.4f}")

# 保持图形窗口打开，直到用户手动关闭
plt.show()