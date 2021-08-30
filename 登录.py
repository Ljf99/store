# root   admin
a=0
user='root'
code='admin'
print('请输入用户名')
user=input()
while user=='root' and a<3:
    print('请输入密码')
    code=input()
    if code!='admin':
        a=a+1
        b=3-a
        print('您输入了错误的密码，您还有',b,'次机会')
    else:
        print('输入正确，正在进入系统')
        break







    #     print('输入用户名错误')
    #     break
    # print('请输入密码')
    # code=input()
    # if code!='admin':
    #     a=a+1
    #     print('数入错误，您还有',a,'次机会')