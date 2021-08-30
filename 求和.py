print('该程序可以打印10个输入的数字的和')
s=0
a=1
while a<=10:
    print('请输入第', a, '个数')
    shuru=input()
    shuru=int(shuru)
    s+=shuru
    a=a+1

print(s)