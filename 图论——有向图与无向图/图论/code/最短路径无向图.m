%% Dijkstra
% 注意Matlab中的图节点要从1开始编号
s = [1 1 2 2 8 8 3 9 3 3 7  4  4 6];
t = [2 8 8 3 9 7 9 7 4 6 6  6  5 5];
w = [4 8 3 8 1 6 2 6 7 4 2 14 9 10];
G = graph(s,t,w);
plot(G, 'EdgeLabel', G.Edges.Weight, 'linewidth', 2) 
set( gca, 'XTick', [], 'YTick', [] ); %去掉坐标轴上的数字
[P,d] = shortestpath(G, 1, 5)  %计算从1到9的最短路径