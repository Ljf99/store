print('查看什么三角形')
print('请输入三角形的第一条边长')
a=input()
a=int(a)
print('请输入三角形的第二条边长')
b=input()
b=int(b)
print('请输入三角形的第三条边长')
c=input()
c=int(c)
if a+b>c or a+c>b or b+c>a:
    if a==b and b==c :
        print('这是一个全等三角形')
    elif a==b or b==c or c==a :
        print('这是一个等腰三角形')
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print('这是一个直角三角形')
    else:
        print('构不成三角形呢')
