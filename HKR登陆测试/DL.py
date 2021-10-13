#导入包
import xlrd
#获取表格地址并将它赋给一个变量
wd = xlrd.open_workbook(filename=r'D:\Training\Python\homework\自动化\day03\log.xlsx', encoding_override=True)
#获取成功的用例表地址赋值给一个变量
st1 = wd.sheet_by_index(0)
#获取行
rows1 = st1.nrows
#获取列
cols1 = st1.ncols
#获取失败的用例表的地址赋值给一个变量
st2 = wd.sheet_by_index(1)
#获取失败表的行
rows2 = st2.nrows
#获取失败表的列
cols2 = st2.ncols
#创建一个空的成功列表
login_success_data = []
#开始循环读取差
for i in range(1,rows1):
    #将数据遍历到空的列表中
    ctype = st1.cell(i, 0).ctype
    #判断字符类型
    no = st1.cell(i, 0).value
    #如果字符类型是浮点型
    if ctype == 2 :
        #转成整形后转成字符串
        no = str(int(no))

    ctype = st1.cell(i , 1).ctype
    no1 = st1.cell(i, 1).value
    if ctype == 2 :
        no1 = str(int(no1))

    ctype = st1.cell(i, 2).ctype
    no2 = st1.cell(i, 2).value
    if ctype == 2:
        no2 = str(int(no2))

    data1 = {'username': no,
            'password': no1,
            'expect': no2}
    login_success_data.append(data1)

login_error_data = []
for i in range(1, rows2):
    ctype = st2.cell(i, 0).ctype
    no = st2.cell(i, 0).value
    if ctype == 2:
        no = str(int(no))

    ctype = st2.cell(i, 1).ctype
    no12 = st2.cell(i, 1).value
    if ctype == 2:
        no12 = str(int(no12))

    ctype = st2.cell(i, 2).ctype
    no22 = st2.cell(i, 2).value
    if ctype == 2:
        no22 = str(int(no22))

    data2 = {'username': no,
             'password': no12,
             'expect': no22}
    login_error_data.append(data2)


class InitPage:
    #将成功的数据列表赋给成功的变量
    login_success_data = login_success_data  # 数据来自Excel表
    # 将失败的数据列表赋给失败的变量
    login_error_data = login_error_data


#-------------------报错
'''
import xlrd

wd = xlrd.open_workbook(filename=r'/自动化/day03/log.xlsx', encoding_override=True)
st = wd.sheet_by_index(0)
cols = st.ncols
rows = st.nrows
st1 = wd.sheet_by_index(1)
rows1 = st1.nrows
cols1 = st1.ncols

class demo:
    def testlogin(self):
        for i in range(1, 2):
            l = st.row_values(i)
        loginok = [
            {'password':l[1]},
            {'username':l[0]},
            {'exexpect':l[2]}
        ]

    for a in range(1, 3):
        l = st1.row_values(a)
        loginerror = [
            {'username': l[0]},
            {'password': l[1]},
            {'exexpect': l[2]}
        ]







'''

'''
st = wd.sheet_by_index(0)
# 获取行
rows = st.nrows
# 获取列
cols = st.ncols
for i in range(1, rows):
    l = st.row_values(i)
    # print(l[0])
    login_success_data = [
        {'username': l[0],
         'password': l[1],
         'exexpect': l[2]}
    ]
#获取sheet名并赋值一个变量
#创建一个对象
class cable:        #数据类
    #

    login_success_data = login_success_data
    print(login_success_data)
cable

# class cable1:
#     st1 = wd.sheet_by_index(1)
#     # 获取行
#     rows1 = st1.nrows
#     # 获取列
#     cols1 = st1.ncols
#     for a in range(1,3):
#         l = st1.row_values(a)
#         # print(l[0])
#         login_error_data = [
#             {'username':l[0],
#             'password':l[1],
#             'exexpect':l[2]}
#         ]
#     print(login_error_data)
# cable1
'''
#-------------------报错
