import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Simhei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

def func10():
    # 创建有向图
    G = nx.DiGraph()

    # 添加带容量的边
    G.add_edge('Vs', '1', capacity=4, flow=3) # Vs到1这条弧，容量为4，目前流为3
    G.add_edge('Vs', '3', capacity=3, flow=2)
    G.add_edge('Vs', '4', capacity=10, flow=4)
    G.add_edge('1', '2', capacity=1, flow=1)
    G.add_edge('1', '3', capacity=3, flow=2)
    G.add_edge('4', '3', capacity=3, flow=2)
    G.add_edge('4', '5', capacity=4, flow=2)
    G.add_edge('3', '2', capacity=4, flow=3)
    G.add_edge('3', '5', capacity=5, flow=3)
    G.add_edge('5', '2', capacity=2, flow=2)
    G.add_edge('5', 'Vt', capacity=8, flow=3)
    G.add_edge('2', 'Vt', capacity=7, flow=6)


    # 使用最大流算法求解最大流
    max_flow_value, max_flow_dict = nx.maximum_flow(G, 'Vs', 'Vt')

    # 打印结果
    print("最大流值:", max_flow_value)
    print("最大流分配:", max_flow_dict)

if __name__ == '__main__':
    func10()