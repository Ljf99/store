max=0       #最大值
a=1      #次数
b=0     #输入的数值
print('该程序可以自己设置几个数字的运算')
print('您要对多少个数字进行计算')
cs=input()
cs=int(cs)
print('该程序可以算',cs,'个数的最大值、和、平均值')
while a<=cs:
    print('请输入',a,'个数')
    shuru=input()
    shuru=int(shuru)
    b+=shuru
    a=a+1
    pj=b/10
    if shuru>max:
        max=shuru
print('您输入的',cs,'个数，它们的最大值是',max)
print('您输入的',cs,'个数，它们的输入的数和为',b)
print('您输入的',cs,'个数，它们的它们的平均值为',pj)



