%%  定义floyd算法：
function [path, dis] = Floyd(gra)
    n = size(gra);
    dis = gra;
    path = zeros(n);
    for k  = 1 : n %这是跳板节点
        for i = 1 : n
            for j = 1 :n
                if (dis(i,k) + dis(k,j) < dis(i,j)) % 通过跳板发现了更短的路径，更新最短路径
                    dis(i,j) = dis(i,k) + dis(k,j);
                    path(i,j) = k;
                end
        end
    end
end


%% 求解最小费用最大流问题
% 图的邻接矩阵，即每段弧能承受的最大流量.如一行表示，节点1到节点2弧长能承受的最大流量为15，节点1到节点3弧长能承受的最大流量是10，节点1到节点4能承受的最大流量是20
c = [0 15 10 20 0 0 0 0;
     0 0 0 0 7 10 0 0;
     0 0 0 0 0 8 2 0;
     0 0 0 0 0 0 18 0;
     0 0 0 0 0 0 0 6;
     0 0 0 0 0 0 0 16;
     0 0 0 0 0 0 0 20;
     0 0 0 0 0 0 0 0;]

x = zeros(8); 

 cost = [+inf 8 10 15 +inf +inf +inf +inf;  %每段弧需要花费的体力（代价），定义方式与c是一样的。
 +inf +inf +inf +inf 9 11 +inf +inf;
 +inf +inf +inf +inf +inf 8 6 +inf;
 +inf +inf +inf +inf +inf +inf 14 +inf;
 +inf +inf +inf +inf +inf +inf +inf 8;
 +inf +inf +inf +inf +inf +inf +inf 9;
 +inf +inf +inf +inf +inf +inf +inf 10;
 +inf +inf +inf +inf +inf +inf +inf +inf;]
 
cost_all = 0;

 %% 因为有负权值，不能用Dijkstra，我们这里用Floyd算法求解
 vec = input('请输入发点和终点（例如[1,8]）：');
 while (1)    
     [path, dis] = Floyd(cost); % 求最短路径
     mypath = [8];
     i = vec(1);  %起点
     j = vec(2);  %终点
     % 筛选出从发点到终点的路径
     while(path(i,j) ~= 0)
        j = path(i,j);
        mypath = [mypath j];%在原数组后追加元素
     end
     mypath = [1 fliplr(mypath)];% 翻转路径方便求解
     if(size(mypath,2) == 2) %此时再也找不到最短路径
         break;
     end
     % 求最短路上的增广链
     max_x = [+inf];
     for i = 2 : size(mypath,2) %计算增广链的delta
          max_x = [max_x min(max_x(i-1), c(mypath(i-1),mypath(i)) - x(mypath(i-1),mypath(i)))];
     end
     delta = min(max_x);
     for i = 2 : size(mypath,2)
          x(mypath(i-1),mypath(i)) = x(mypath(i-1),mypath(i)) + delta;% 对路径上的弧加流量
          cost_all = cost_all + delta*cost(mypath(i-1),mypath(i));% 计算总耗费
     end
     % 检查是否有反向弧
     for i = 2 : size(mypath,2)
          if(c(mypath(i-1),mypath(i)) == x(mypath(i-1),mypath(i))) % 弧上的流量已满
                cost(mypath(i),mypath(i-1)) = -1*cost(mypath(i-1),mypath(i)); % 增加一条反向弧
                % 取消原弧
                c(mypath(i-1),mypath(i)) = 0; 
                cost(mypath(i-1),mypath(i)) = +Inf;
          end
          if(x(mypath(i-1),mypath(i)) < c(mypath(i-1),mypath(i)) && 0 < x(mypath(i-1),mypath(i))) % 弧上的流量未满,且大于0
                cost(mypath(i),mypath(i-1)) = -1*cost(mypath(i-1),mypath(i)); % 增加一条反向弧
          end
     end
 end
 myplot(cost);