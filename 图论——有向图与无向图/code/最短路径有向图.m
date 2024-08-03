% 用1表示A，2表示B，3表示C，4表示D，5表示E
c = [0 3 5 0 0 ;
     0 0 2 6 0 ;
     0 0 0 1 0 ;
     0 0 0 0 4 ;
     0 0 0 0 0;]
 view(biograph(c, [], 'ShowWeights', 'on'));
 G=digraph(c)  %只有这样转换才可以把有向图转化为图对象，进而能够使用plot函数
 plot(G, 'EdgeLabel', G.Edges.Weight, 'linewidth', 2) 
 set( gca, 'XTick', [], 'YTick', [] ); %去掉坐标轴上的数字
[P,d] = shortestpath(G, 1, 5)  %计算从1(A)到5(E）的最短路径