from scipy.optimize import minimize

def func4():
    '''
    使用 minimize 函数进行线性规划
    :return: None
    '''
    # 定义目标函数的系数
    # 目标函数形式为: -40*x0 - 30*x1
    c = [-40, -30]

    # 定义等式约束条件的函数
    # 等式约束形式为: x0 + x1 = 6
    def eq_constraint(x):
        return x[0] + x[1] - 6

    # 定义不等式约束条件的函数
    # 不等式约束形式为: 240*x0 + 120*x1 <= 1200
    def ineq_constraints(x):
        return [1200 - 240*x[0] - 120*x[1]]  # 确保该值非负

    # 定义变量的边界
    # x0 和 x1 的取值范围均在 [1, 6] 之间
    bounds = [(1, 6), (1, 6)]

    # 初始猜测值
    # 从 [1, 1] 开始优化，初始值应在边界范围内
    x0 = [1, 1]

    # 使用 minimize 函数进行线性规划
    # lambda x: c[0] * x[0] + c[1] * x[1] 定义了目标函数: -40*x0 - 30*x1
    # constraints 指定了约束条件，其中 type 为 'eq' 表示等式约束，
    # 'ineq' 表示不等式约束
    # bounds 限制了变量的取值范围
    # method='SLSQP' 选择了 Sequential Least Squares Quadratic Programming 方法
    res = minimize(lambda x: c[0] * x[0] + c[1] * x[1], x0,
                   constraints=[{'type': 'eq', 'fun': eq_constraint},
                                {'type': 'ineq', 'fun': ineq_constraints}],
                   bounds=bounds,
                   method='SLSQP')  # 可选方法: highs, COBYLA, L-BFGS-B

    # 打印结果
    print('最小值:', res.fun)  # 打印最小值，即目标函数的最优值
    print('最优解:', res.x)    # 打印最优解，即变量 x0 和 x1 的最优值



def func5():
    '''
    用minimize函数做线性规划,更强
    :return:
    '''
    # 定义目标函数的系数
    c = [-2, -3, 5]

    # 定义等式约束条件的函数
    def eq_constraint(x):
        return x[0] + x[1] + x[2] - 7

    # 定义不等式约束条件的函数
    def ineq_constraints(x):
        return [-10 + 2*x[0] - 5*x[1] + x[2],  # -2*x1 + 5*x2 - x3 <= -10
                12-x[0] - 3*x[1] - x[2]]  # x1 + 3*x2 + x3 <= 12

    # 定义变量的边界
    bounds = [(0, None), (0, None), (0, None)]  # 对 x1 x2 x3 的边界，它们都大于等于0，但是没有上界

    # 初始猜测值
    x0 = [0, 0, 0]


    # 使用 minimize 函数进行线性规划
    #lambda x: c[0] * x[0] + c[1] * x[1] + c[2] * x[2]实际就是目标函数：−2X0−3X1+5X2
    res = minimize(lambda x: c[0] * x[0] + c[1] * x[1] + c[2] * x[2], x0,
                   constraints=[{'type': 'eq', 'fun': eq_constraint},
                                {'type': 'ineq', 'fun': ineq_constraints}],
                   bounds=bounds,
                   method='SLSQP') #它提供了多种求解算法，如highs、SLSQP、COBYLA、L-BFGS-B等，你可以试试有什么效果

    # 打印结果
    print('最小值:', res.fun)
    print('最优解:', res.x)



