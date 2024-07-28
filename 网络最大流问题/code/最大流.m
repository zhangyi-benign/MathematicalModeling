%% 用标号法求解网络最大流问题
a = zeros(7);   %构造7*7矩阵，因为从0到6，一共有7个节点
a(1,2) = 4; a(1,4) = 3; a(1,5) = 10;  %输入每个直接相连节点之间能流的最大承载量
a(2,3) = 1; a(2,4) = 3; a(4,3) = 4;
a(5,4) = 3; a(4,6) = 5; a(5,6) = 4;
a(6,3) = 2; a(3,7) = 7; a(6,7) = 8;
b = sparse(a);%通过挤出任何零元素将满矩阵转换为稀疏格式
[MaxFlow FlowMatrix Cut] = graphmaxflow(b,1,7); % 计算网络最大流
view(biograph(a, [], 'ShowWeights', 'on')); % 绘制原图
view(biograph(FlowMatrix, [], 'ShowWeights', 'on')); % 绘制最大流图

