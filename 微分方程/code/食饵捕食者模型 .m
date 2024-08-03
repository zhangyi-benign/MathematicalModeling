%自己定义好的函数，储存为odefun1
function dy = pre_war(t,y)   %定义了系数、初值、具体微分方程。
    r = 1;d = 0.5; a = 0.1; b = 0.02;
    dy=zeros(2,1); 
    dy(1) = (r-a*y(2))*y(1);
    dy(2) = -1*(d-b*y(1))*y(2);
end


%主执行脚本
%% 先试试用符号解
r = 1;d = 0.5; a = 0.1; b = 0.02;
syms x(t) y(t) % 定义符号变量，x(t)和y(t)都是关于t的函数
%微分方程：x'(t) = (r-a*y)*x, y'(t) = -(d-b*x)*y
eq1 = diff(x,t) == (r-a*y)*x;
eq2 = diff(y,t) == -(d-b*x)*y;
eqs = [eq1, eq2];
conds = [x(0) == 25, y(0) == 2];
[xSol(t), ySol(t)] = dsolve(eqs, conds)   %执行后发现没有符号解，只能用数值解


%% 用数值解
[t,val]=ode45('odefun1',[0 15],[25 2]);  %[0,15]指求解的时间范围，[25,2]指初值条件；ode45将返回两种类型，第一种是对应的时间，第二种是对应时间的函数值（向量），这里返回的是食饵和捕食者的数量
prey=val(:,1); Predator=val(:,2);  %因为返回的val是一个向量，因此可以用这种方法分别提取出食饵和捕食者
figure(1)
plot(prey,Predator,'-')% 绘制相轨线
title('捕食者和食饵数量变化的相轨线图')
xlabel('食饵数量');   
ylabel('捕食者数量')

figure(2);
plot(t,prey,'--',t,Predator,'-')
legend('食饵数量','鲨鱼数量')
xlabel('时间');   ylabel('数量')
```

