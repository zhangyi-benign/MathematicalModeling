%% 绘制数字标号的图
s = [1 2 3]; %注意要从1开始标号，不能从0开始
t = [4 1 2]
w = [5 2 6] %第1个点和第4个点直接相连，权重是5。第2个点和第1个点直接相连，权重是2.第3个点和第2个点直接相连，权重是6
%绘制带权重的图
G = graph(s, t, w);
plot(G, 'EdgeLabel', G.Edges.Weight, 'linewidth', 2); %调用plot绘制带权重的图
%绘制不带权重的图
G2 = graph(s, t);
plot(G2, 'linewidth', 2) %绘制不带权重的图
set( gca, 'XTick', [], 'YTick', [] ); %去掉坐标轴上的数字



%% 绘制字符串标号的图
s = {'A', 'C', 'B', 'D', 'E', 'C'}; %定义字符串元胞数组
t = {'B', 'A', 'C', 'B', 'D', 'D'}
w = [3 5 2 6 4 1];
G = graph(s, t, w);
plot(G, 'EdgeLabel', G.Edges.Weight, 'linewidth', 2)
set(gca, 'XTick', [], 'YTick', []);


%% 重点：绘制邻接矩阵表示的图——有向图
c = [0 15 10 20 0 0 0 0;
     0 0 0 0 7 10 0 0;
     0 0 0 0 0 8 2 0;
     0 0 0 0 0 0 18 0;
     0 0 0 0 0 0 0 6;
     0 0 0 0 0 0 0 16;
     0 0 0 0 0 0 0 20;
     0 0 0 0 0 0 0 0;]
 view(biograph(c, [], 'ShowWeights', 'on'));