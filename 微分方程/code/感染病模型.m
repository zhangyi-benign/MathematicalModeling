%% SI模型
lamda = 0.1; %感染强度为0.1
syms i(t)  % 定义一个符号变量 i(t)，表示时间 t 时刻感染者的比例
% 定义微分方程：i'(t) = lamda * i(t) * (1 - i(t))
% 这个方程表示感染者比例随时间的变化
%微分方程：i'= lamda*i*(1-i)
eq = diff(i,t) == lamda * i * (1-i);
dsolve(eq) %求通解，不考虑初始条件
% 设定初始条件并求解特解
% 这里假设 t = 0 时，初始感染者比例为 0.1（即疫情刚开始时有 10% 的人患病）
iSol(t) = dsolve(eq, i(0) == 0.1) 
t = [1:100];  % 定义时间序列，t 从 1 增加到 100
i = iSol(t);  % 时间从 1 到 100，共 100 个时间点
plot(t,i,'-'); % 通过特解函数 iSol(t) 计算 t 时刻的感染者比例
title('SI模型-患病比例随时间变化图')
xlabel('时间');   
ylabel('患病比例')







%% SIS模型
lamda = 0.1;
%sigma = 2;% 通过调整接触数可改变传染趋势
sigma = 1;
syms i(t) 
%微分方程：i'= lamda*i*(1-1/sigma-i)
eq = diff(i,t) == lamda*i*(1-1/sigma-i);
dsolve(eq) %求通解
iSol(t) = dsolve(eq, i(0) == 0.1) %设疫情刚开始有10%人患病
iSol_1(t) = dsolve(eq, i(0) == 0.6)%设疫情刚开始有60%人患病
t = [1:100];
i = iSol(t);
i_1 = iSol_1(t);
plot(t,i,'-r',t,i_1,'-b');
legend('i0 < 1-1/sigma', 'i0 > 1-1/sigma');
title('SIS模型-患病比例随时间变化图')
xlabel('时间');   
ylabel('患病比例');







%% SIR
% 定义函数
function dydt = odefun_SIR(t,y)
    %lamda = 0.6;%传染强度
    %miu = 0.3;%治愈率
    lamda = 0.5;
    miu = 0.4;
    dydt = zeros(2,1); % y(1)表示S  y(2)表示I
    dydt(1) = -1*lamda*y(1)*y(2);
    dydt(2) = lamda*y(1)*y(2)-miu*y(2);   
end
% 主脚本
%% SIR模型
[t,y] = ode45('odefun_SIR',[0,50],[0.99,0.01]);% s0=0.99，i0=0.01
plot(t,y(:,1),'-g',t,y(:,2),'-r',t, 1-y (:,1)-y(:,2),'-b')  %减掉前两者，自然得到第三者
legend('易感染人S', '患者I', '移除者R');
title('SIR模型-SIR三类人所占比例随时间变化图')
xlabel('时间');   
ylabel('比例');
grid on %可以打开背景网格，方便观察，默认关闭






%% SIRS
% 定义函数
function dydt = odefun_SIRS(t,y)
    lamda = 0.6;%传染强度
    miu = 0.3;%治愈率
    alpha = 0.1; %疫苗失效率（抗体削弱度）
    dydt = zeros(2,1); % y(1)表示S  y(2)表示I
    dydt(1) = -1*lamda*y(1)*y(2) + alpha*(1-y(1)-y(2));
    dydt(2) = lamda*y(1)*y(2)-miu*y(2);   
end
% 主执行窗口
%% SIRS模型
[t,y] = ode45('odefun_SIRS',[0,50],[0.99,0.01]);% s0=0.99，i0=0.01
plot(t,y(:,1),'-g',t,y(:,2),'-r',t, 1-y (:,1)-y(:,2),'-b')
legend('易感染人S', '患者I', '移除者R');
title('SIRS模型-SIR三类人所占比例随时间变化图')
xlabel('时间');   
ylabel('比例');
grid on;






%%% 实战
%% 1.潜伏者+死亡者
% 定义函数
function dydt = odefun_Covid_19_SERID(t,y)
    lamda = 0.6;%传染强度
    i = 0.125;% 转病率
    r = 0.1; %康复率 
    k = 0.05;%感染者死亡率
    dydt = zeros(5,1); % y(1)表示S  y(2)表示I   y(3)表示e   y(4)表示r   y(5)表示d
    dydt(1) = -1*lamda*y(1)*y(2); 
    dydt(2) = i*y(3) - r*y(2) - k*y(2) ;
    dydt(3) = lamda*y(1)*y(2) - i*y(3);
    dydt(4) = r*y(2);
    dydt(5) = k*y(2);
end
%% 引入潜伏者和死亡者的SERID模型
[t,y] = ode45('odefun_Covid_19_SERID',[0,500],[0.99 0.005 0.005 0 0]);%S=0.99 I=0.005 E = 0.005 R=0  D=0
plot(t,y(:,1),'-g',t,y(:,2),'-r',t, y(:,3),'-b', t, y(:,4),'-', t, y(:,5),'-')
legend('易感染人S', '患者I', '潜伏者E', '移除者R', '死亡者D');
title('新冠SERID模型-SERID五类人所占比例随时间变化图')
xlabel('时间');   
ylabel('比例');
grid on;

%% 2.潜伏者自愈
%定义函数
function dydt = odefun_Covid_19_SERID_1(t,y)
    lamda = 0.6;%传染强度
    lamda1 = 0.6;%潜伏者的传染强度
    i = 0.125;% 转病率
    r = 0.1; %康复率 
    k = 0.05;%感染者死亡率
    c = 0.05;%转阴率
    dydt = zeros(5,1); % y(1)表示S  y(2)表示I   y(3)表示e   y(4)表示r   y(5)表示d
    dydt(1) = -1*lamda*y(1)*y(2) - lamda1*y(3)*y(1) + c*y(3); 
    dydt(2) = i*y(3) - r*y(2) - k*y(2) ;
    dydt(3) = lamda*y(1)*y(2) +lamda1*y(3)*y(1) - i*y(3) - c*y(3);
    dydt(4) = r*y(2);
    dydt(5) = k*y(2);
end
%% 修正潜伏者传染率和转阴率
[t,y] = ode45('odefun_Covid_19_SERID_1',[0,150],[0.99 0.005 0.005 0 0]);%S=0.99 I=0.005 E = 0.005 R=0  D=0
plot(t,y(:,1),'-g',t,y(:,2),'-r',t, y(:,3),'-b', t, y(:,4),'-', t, y(:,5),'-')
legend('易感染人S', '患者I', '潜伏者E', '移除者R', '死亡者D');
title('新冠SE_1RID模型-SERID五类人所占比例随时间变化图')
xlabel('时间');   
ylabel('比例');
grid on;

%% 3.隔离者
% 定义函数
function dydt = odefun_Covid_19_SERIDQ(t,y)
    lamda = 0.6;%传染强度
    lamda1 = 0.6;%潜伏者的传染强度
    i = 0.125;% 转病率
    r = 0.1; %康复率 
    k = 0.05;%感染者死亡率
    c = 0.05;%转阴率
    q = 0.9; %收治速率
    k1 = 0.05*k %隔离者死亡率
    r1 = 1.2*r %隔离者康复率
    dydt = zeros(6,1); % y(1)表示S  y(2)表示I   y(3)表示e   y(4)表示r   y(5)表示d  y(6)表示q
    dydt(1) = -1*lamda*y(1)*y(2) - lamda1*y(3)*y(1) + c*y(3); 
    dydt(2) = i*y(3) - r*y(2) - k*y(2) - q*y(2);
    dydt(3) = lamda*y(1)*y(2) + lamda1*y(3)*y(1) - i*y(3) - c*y(3);
    dydt(4) = r*y(2) + r1*y(6);
    dydt(5) = k*y(2) + k1*y(6);
    dydt(6) = q*y(2) - r1*y(6) - k1*y(6);
end
%%  主执行脚本
%% 引入隔离者的SERIDQ模型
[t,y] = ode45('odefun_Covid_19_SERIDQ',[0,150],[0.99 0.005 0.005 0 0 0]);%S=0.99 I=0.005 E = 0.005 R=0  D=0  Q=0
plot(t,y(:,1),'-g',t,y(:,2),'-r',t, y(:,3),'-b', t, y(:,4),'-', t, y(:,5),'-', t, y(:,6),'-')
legend('易感染人S', '患者I', '潜伏者E', '移除者R', '死亡者D', '隔离者Q');
title('新冠SERIDQ模型-SERIDQ六类人所占比例随时间变化图')
xlabel('时间');   
ylabel('比例');
grid on;

%% 4.自我隔离
% 定义函数
function dydt = odefun_Covid_19_SERIDQF(t,y)
    lamda = 0.3;%要降低传染强度
    lamda1 = 0.3;%潜伏者的传染强度
    i = 0.125;% 转病率
    r = 0.1; %康复率 
    k = 0.05;%感染者死亡率
    c = 0.05;%转阴率
    q = 0.9; %收治速率
    k1 = 0.05*k %隔离者死亡率
    r1 = 1.2*r %隔离者康复率
    f = 0.3; %自我隔离率
    dydt = zeros(6,1); % y(1)表示S  y(2)表示I   y(3)表示e   y(4)表示r   y(5)表示d  y(6)表示q
    dydt(1) = -1*lamda*y(1)*y(2) - lamda1*y(3)*y(1) + c*y(3) - f*y(1); 
    dydt(2) = i*y(3) - r*y(2) - k*y(2) - q*y(2);
    dydt(3) = lamda*y(1)*y(2) + lamda1*y(3)*y(1) - i*y(3) - c*y(3);
    dydt(4) = r*y(2) + r1*y(6);
    dydt(5) = k*y(2) + k1*y(6);
    dydt(6) = q*y(2) - r1*y(6) - k1*y(6);
end
%% 主执行程序
%% 引入自我隔离者的SERIDQF模型
[t,y] = ode45('odefun_Covid_19_SERIDQ',[0,30],[0.99 0.005 0.005 0 0 0]);%S=0.99 I=0.005 E = 0.005 R=0  D=0  Q=0
plot(t, y(:,1), '-g', t,y(:,2),'-r',t, y(:,3),'-b', t, y(:,4),'-c', t, y(:,5),'-m', t, y(:,6),'-y')
hold on;

% 30天后政府开始干预
n = size(y,1);
[t1,y1] = ode45('odefun_Covid_19_SERIDQF',[30,150],[y(n,1), y(n,2), y(n,3), y(n,4), y(n,5), y(n,6)]);
plot(t1, y1(:,1), '-g',t1,y1(:,2),'-r',t1, y1(:,3),'-b', t1, y1(:,4),'-c', t1, y1(:,5),'-m', t1, y1(:,6),'-y')
legend('易感染人S', '患者I', '潜伏者E', '移除者R', '死亡者D', '隔离者Q');
title('新冠SERIDQF模型-政府在30天干预后SERIDQ六类人所占比例随时间变化图')
xlabel('时间');   
ylabel('比例');
grid on;


