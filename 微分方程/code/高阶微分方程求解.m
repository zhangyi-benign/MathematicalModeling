%% 例题1

% 定义二阶微分方程的函数句柄
% y'' + 2*y' + 5*y = sin(t)
% 降阶为一阶微分方程组：
% 设 v = y'
% 那么 y'' = v'
% 所以 v' = sin(t) - 2*v - 5*y

% 定义微分方程的函数句柄 f(t, y)
% y 是一个包含两个元素的向量，其中
% y(1) 代表 y(t)，
% y(2) 代表 y'(t) 即 v(t)
f = @(t, y) [y(2); sin(t) - 2*y(2) - 5*y(1)];

% 定义时间范围和初始条件
tspan = [-2 2]; % 时间范围 t 从 -2 到 2
y0 = [1; 1]; % 初始条件 [y(0), y'(0)]，即 [1, 1]

% 使用 ode45 求解一阶微分方程组
% ode45 是 MATLAB 中的一个求解常微分方程的函数
% [t, y] 是求解的时间向量和解矩阵
[t, y] = ode45(f, tspan, y0);

% 解析解计算（假设已知解析解函数 y_analytical）
% 如果有解析解函数，可以计算解析解并进行比较
% 例如，假设解析解函数为：
% y_analytical = @(t) (1/26) * (5 * sin(t) + 6 * cos(t) - 2 * sin(t) - 6 * cos(t));
% 计算解析解的值
% y_analytical_values = y_analytical(t);

% 计算残差
% 计算残差以评估数值解的准确性
% 残差 = 实际右侧 - 数值解右侧
residual = y(:,2) - (sin(t) - 2 * y(:,2) - 5 * y(:,1));
max_residual = max(abs(residual)); % 计算最大残差

% 输出初始条件
% 显示在时间 t=0 时的 y(0) 和 y'(0) 的值
disp(['Initial condition y(0): ', num2str(y(1,1))]);
disp(['Initial condition y''(0): ', num2str(y(1,2))]);

% 输出最大残差
% 显示计算出的最大残差值
disp(['Maximum residual: ', num2str(max_residual)]);

% 绘制结果
% 使用 plot 函数绘制 y(t) 和 y'(t) 的图像
figure;
plot(t, y(:,1), '-o', t, y(:,2), '-x'); % 绘制 y(t) 和 y'(t)
xlabel('Time t'); % x 轴标签
ylabel('Solutions y and y'''); % y 轴标签
legend('y(t)', 'y''(t)'); % 图例
title('Solution of the ODEs'); % 图标题