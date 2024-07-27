# 01背包模型
from pulp import LpMinimize, LpProblem, LpVariable, lpSum


def func6():
    '''
    整数规划示例：最小化目标函数
    这个函数定义并解决了一个0-1背包问题。
    '''
    # 创建一个LP问题，目标是最小化
    problem = LpProblem("Knapsack_Problem", LpMinimize)

    # 定义0-1整数变量
    x = [LpVariable(f'x{i}', cat='Binary') for i in range(6)]  # 6个0-1变量 x0 到 x5

    # 定义目标函数
    problem += lpSum(x), "Objective Function"
    # 目标函数是 x0 + x1 + x2 + x3 + x4 + x5，我们希望最小化这个目标函数

    # 添加约束条件
    problem += x[0] + x[1] + x[2] >= 1
    # 约束条件1：x0 + x1 + x2 >= 1

    problem += x[2] + x[4] >= 1
    # 约束条件2：x2 + x4 >= 1

    problem += x[3] + x[5] >= 1
    # 约束条件3：x3 + x5 >= 1

    problem += x[4] + x[5] >= 1
    # 约束条件4：x4 + x5 >= 1

    problem += x[0] >= 1
    # 约束条件5：x0 >= 1

    problem += x[1] + x[3] + x[5] >= 1
    # 约束条件6：x1 + x3 + x5 >= 1

    problem += lpSum(x) <= 6
    # 约束条件7：x0 + x1 + x2 + x3 + x4 + x5 <= 6

    # 解决问题
    problem.solve()

    # 打印结果
    print("最优解:")
    for i in range(6):
        print(f"x{i} =", x[i].varValue)
    # 打印每个变量的最优值

    print("最优值:", problem.objective.value())
    # 打印目标函数的最优值






# 指派问题模型
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value, LpStatus

# 利润矩阵
profits = [
    [4, 2, 3, 4],  # 1号设备的利润
    [6, 4, 5, 5],  # 2号设备的利润
    [7, 6, 7, 6],  # 3号设备的利润
    [7, 8, 8, 6],  # 4号设备的利润
    [7, 9, 8, 6],  # 5号设备的利润
    [7, 10, 8, 6]  # 6号设备的利润
]

# 定义模型
model = LpProblem("Maximize_Profit", LpMaximize)

# 企业和设备编号
enterprises = ["甲", "乙", "丙", "丁"]
devices = [1, 2, 3, 4, 5, 6]

# 创建决策变量
x = LpVariable.dicts("x", (devices, enterprises), cat='Binary')

# 将企业编号映射到整数索引
enterprise_index = {enterprise: i for i, enterprise in enumerate(enterprises)}

# 目标函数：最大化总利润
model += lpSum(profits[device-1][enterprise_index[enterprise]] * x[device][enterprise] for device in devices for enterprise in enterprises)

# 约束条件：每个设备只能分配给一个企业
for device in devices:
    model += lpSum(x[device][enterprise] for enterprise in enterprises) == 1

# 约束条件：每个企业至少分配1台设备
for enterprise in enterprises:
    model += lpSum(x[device][enterprise] for device in devices) >= 1

# 求解模型
model.solve()

# 输出结果
print(f"最大利润: {value(model.objective)}")
print(f"模型状态: {LpStatus[model.status]}")
for device in devices:
    for enterprise in enterprises:
        if value(x[device][enterprise]) == 1:
            print(f"设备{device} 分配给 企业{enterprise}")

