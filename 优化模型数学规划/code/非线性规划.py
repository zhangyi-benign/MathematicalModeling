def func6():
    '''
    整数规划示例：最大化目标函数
    这个函数定义并解决了一个简单的整数规划问题。
    '''
    # 创建一个LP问题，目标是最大化
    problem = LpProblem("Integer_Optimization_Problem", LpMaximize)

    # 定义整数变量
    x = LpVariable("x", lowBound=0, cat='Integer')  # 整数变量 x，取值范围是 0 到正无穷
    y = LpVariable("y", lowBound=0, cat='Integer')  # 整数变量 y，取值范围是 0 到正无穷

    # 定义目标函数
    problem += 2 * x + 3 * y, "Objective Function"
    # 目标函数是 2x + 3y，我们希望最大化这个目标函数

    # 添加约束条件
    problem += x + 2 * y <= 7
    # 约束条件1：x + 2y <= 7


    problem += 3 * x - y <= 9
    # 约束条件2：3x - y <= 9

    # 解决问题
    problem.solve()

    # 打印结果
    print("最优解:")
    print("x =", x.varValue)
    # 打印变量 x 的最优值

    print("y =", y.varValue)
    # 打印变量 y 的最优值

    print("最优值:", problem.objective.value())
    # 打印目标函数的最优值