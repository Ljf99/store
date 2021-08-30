print('该程序可以求出青蛙爬井')
print('可以自定义每日爬的距离、下滑的距离、井的高度')
print('请输入井的高度')
h=input()
h=int(h)
print('请输入青蛙每日爬的距离')
j=input()
j=int(j)
print('请输入每日下滑的距离')
x=input()
x=int(x)
# time=h/(j-x)
# time=round(time,0)
# print('一只青蛙掉在井里了，井高',h,'米，青蛙白天网上爬',j,'米，晚上下滑',x,'米，问第几天能出来？')
# print('答：青蛙',time,'天可以爬出来')













h%j>x
y=h%j
y=int(y)
if y>x:
    time=h/(j-x)
    time=round(time,0)
    print('一只青蛙掉在井里了，井高', h, '米，青蛙白天网上爬', j, '米，晚上下滑', x, '米，问第几天能出来？')
    print('答：青蛙', time, '天可以爬出来')
else:
    time=h/(j-x)
    print('一只青蛙掉在井里了，井高',h,'米，青蛙白天网上爬',j,'米，晚上下滑',x,'米，问第几天能出来？')
    print('答：青蛙',time,'天可以爬出来')
