import networkx as nx
import networkx as nx
def func8():
    '''
    最短路径
    :return:
    '''
    # 创建无向图
    G = nx.Graph()  # 使用无向图

    # 添加带权边
    G.add_edge(1, 2, weight=4)
    G.add_edge(1, 8, weight=8)
    G.add_edge(2, 8, weight=3)
    G.add_edge(2, 3, weight=8)
    G.add_edge(8, 9, weight=1)
    G.add_edge(8, 7, weight=6)
    G.add_edge(3, 9, weight=2)
    G.add_edge(3, 4, weight=7)
    G.add_edge(3, 5, weight=4)
    G.add_edge(9, 7, weight=6)
    G.add_edge(7, 5, weight=2)
    G.add_edge(4, 5, weight=10)
    G.add_edge(4, 6, weight=9)
    G.add_edge(6, 5, weight=10)

    # 求解最短路径
    shortest_path = nx.shortest_path(G, 1, 6, weight='weight')  # 起点 1 到 终点 6
    shortest_path_length = nx.shortest_path_length(G, 1, 6, weight='weight')  # 起点 1 到 终点 6

    # 打印结果
    print("最短路径:", shortest_path)
    print("最短路径长度:", shortest_path_length)

if __name__ == '__main__':
    func8()