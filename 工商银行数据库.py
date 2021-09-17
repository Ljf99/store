import pymysql
import random
import re
bank_name = '天地银行中国分行'

#-----------欢迎-------------
def welcome():
    print('*********************************')
    print('*         天地银行中国分行         *')
    print('* 1.开户                         *')
    print('* 2.存钱                         *')
    print('* 3.取钱                         *')
    print('* 4.转账                         *')
    print('* 5.查询                         *')
    print('* 6.退出                         *')
    print('*********************************')

#-----------开户-------------
def blossom():
    con = pymysql.connect(host='localhost',user='root',password='',database='工商数据库')
    cursor = con.cursor()
    sql = 'insert into supporter values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    account = random.randint(10000000,99999999)
    username=input('请输入您的用户名''\n')
    password = input('请输入您的密码''\n')
    while not re.findall('^[0-9]+$', password):
        print('请输入纯数字密码')
        password = input()
    country = input('请输入您的国籍''\n')
    province = input('请输入您居住的省市''\n')
    street = input('请输入您居住的街道''\n')
    gate = input('请输入您的门牌号''\n')
    print('请选择余额的获取方式')
    print('输入1为手动输入')
    print('输入其他为自动获取')
    picking=input()
    picking=int(picking)
    if picking == 1:
        money = input('请输入你的金钱')
    else:
        money = random.randint(8000,15000)
    param = [account,username,password,country,province,street,gate,money,bank_name]
    cursor.execute(sql,param)
    cursor.fetchone()
    con.commit()
    cursor.close()
    con.close()
    print('开户成功，以下是您的个人开户信息')
    info = '''
       -----------------个人信息-----------------
       用户名：%s
       密码：%s
       账号：%s
       地址信息
           国家：%s
           省份：%s
           街道：%s
           门牌号：%s
       余额：%s
       开户行地址：%s
       ----------------------------------------
       '''
    print(info % (username, password, account, country, province, street, gate, money, bank_name))

#-----------存款-------------
def access():
    con = pymysql.connect(host='localhost',user='root',password='',database='工商数据库')
    cursor = con.cursor()
    username = input('请输入您的账号')
    sql = 'select supporter.账号 from supporter where 账号 = %s'
    username=[username]
    cursor.execute(sql,username)
    p=input('请输入充值金额')
    sql = 'update supporter set 存款余额 = 存款余额+%s where 账号=%s'
    change = [p,username]
    cursor.execute(sql,change)
    print('')
    con.commit()
    cursor.close()
    con.close()

#-----------取款-------------
def take():
    con = pymysql.connect(host='localhost',user='root',password='',database='工商数据库')
    cursor = con.cursor()
    username =input('请输入您的账号')
    sql = 'select supporter.账号 from supporter where 账号 = %s'
    username = [username]
    a=cursor.execute(sql, username)
    if a>0:
        password = input('请输入您的密码')
        sql1 ='select supporter.密码 from supporter where 密码=%s and 账号=%s'
        password=[password,username]
        a=cursor.execute(sql1,password)
        if a>0:
            money=input('请输入您的取款金额')
            sql2='update supporter set 存款余额 = 存款余额-%s where 账号=%s'
            c = [money,username]
            cursor.execute(sql2,c)
            con.commit()
            cursor.close()
            con.close()

#-----------转账-------------
def debit():
    con = pymysql.connect(host='localhost',user='root',password='',database='工商数据库')
    cursor = con.cursor()
    username =input('请输入您的账号')
    sql = 'select supporter.账号 from supporter where 账号 = %s'
    username = [username]
    a=cursor.execute(sql, username)
    if a>0:
        password = input('请输入您的密码')
        sql1 ='select supporter.密码 from supporter where 密码=%s and 账号 =%s'
        password=[password,username]
        a=cursor.execute(sql1,password)
        if a > 0:
            opposite=input('收款人账号')
            sql2 = 'select supporter.账号 from supporter where 账号 = %s'
            opposite=[opposite]
            a =cursor.execute(sql2,opposite)
            if a > 0 :
                copies = input('转账金额')
                sql3 = 'update supporter set 存款余额 = 存款余额-%s where 账号=%s'
                e=[copies,username]
                cursor.execute(sql3, e)
                sql4 = 'update supporter set 存款余额 = 存款余额+%s where 账号=%s'
                f=[copies,opposite]
                cursor.execute(sql4,f)
                con.commit()
                cursor.close()
                con.close()

#-----------查询-------------
def inquire():
    con = pymysql.connect(host='localhost',user='root',password='',database='工商数据库')
    cursor = con.cursor()
    account = input('请输入您要查询的账号')
    sql = 'select supporter.账号 from supporter where 账号 = %s'
    account=[account]
    a=cursor.execute(sql, account)
    if a>0:
        password = input('请输入您的密码')
        sql1 ='select supporter.密码 from supporter where 密码=%s and 账号 =%s'
        password=[password,account]
        a=cursor.execute(sql1,password)
        if a>0:
            sql2='select * from supporter where 账号=%s'
            c =[account]
            cursor.execute(sql2,c)
            s=cursor.fetchone()
            print(s)
            con.commit()

            print('查询成功，以下是您的个人信息')
            info = '''
                -----------------个人信息-----------------
                用户名：%s
                密码：%s
                账号：%s
                地址信息
                    国家：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                余额：%s
                开户行地址：%s
                ----------------------------------------
                '''
            print(info % (s[0], s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8]))
            cursor.close()
            con.close()

#-----------业务选择-------------
while True:
    welcome()
    chose=input('请输入您的业务')
    if chose =='1':
        blossom()
    elif chose=='2':
        access()
    elif chose=='3':
        take ()
    elif chose=='4':
        debit()
    elif chose=='5':
        inquire()
    elif chose=='6':
        print('beybey')
        break
    else:
        print('错误')


