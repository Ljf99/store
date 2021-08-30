import random
suiji=random.randint(0,100)                 #生成一个随机数
zengjia=random.randint(0,5)                 #生成一个随机数
xx=random.randint(0,2)
#print(suiji)                                #打印随机数
jinqian=1000                                #金钱：1000金币
huafei=50                                       #每次猜数花费50
cishu=0
help=150
xiangxi=300
print('------猜------字------游------戏------')
print('输入与  提示数字  不同的 数字 可以跳过选择')
while jinqian!=0 and cishu<=9:                             #如果金钱不为0和次数为10
    print('现有金钱      ', jinqian)
    shuru = input('猜的啥')                    #输入一个猜的数
    shuru = int(shuru)                       #将数值设置为整数
    if shuru!=suiji :                       #如果输入的数不等于随机数
        chazhi=suiji-shuru                  #随机数减输入的数的差值
        chazhi=abs(chazhi)                  #将差值设置为正数
        cha=(chazhi+zengjia)                #差值加随机数
        cha2=(cha*2)                        #浮动差值  两边
        jinqian=jinqian-huafei              #金钱-花费
        cishu=cishu+1
        jihui=10-cishu
        print('对不起，您猜错了，正确结果与您的猜想在',cha2,'的范围之间','机会：',jihui,'金钱',jinqian)
        print('花费100获取提示信息，是否获取？                  当前余额',jinqian)
        tishi = input('请选择，输入1获取提示，输入其他跳过')
        tishi = int(tishi)
        while tishi==1:
            jinqian = jinqian - help
            if shuru>suiji:
                print('您猜的数大了    当前余额',jinqian)
                print('是否花费150金币继续获取提示  输入2(提示信息与正确结果有0-5的误差)')
                tishi = input()
                tishi =int(tishi)
                if tishi==2:
                    da = shuru - suiji+zengjia
                    print('您猜的数字比随机数大',da,'是否花费300金币获取详细提示（上下差2）')
                    tishi=input()
                    tishi=int(tishi)
                    if tishi==3:
                        jinqian=jinqian-xiangxi
                        print('马上就可以获取结果了，现在只需要在花200金币就可以直接获取正确答案')
                        jinqian = jinqian - 200
                        print('心动不如行动，现在就下单输入4',jinqian)
                        tishi=input()
                        tishi=int(tishi)
                        if tishi==4:
                            da=shuru-suiji+xx
                            print('想屁吃呢，自己猜   比正确结果大（上下差2）',da)
                        elif tishi!=4:
                            print('耍我呢，扣钱')
                            jinqian=jinqian-500
                            print('你现在还有',jinqian)
                    break
                break
            elif shuru<suiji:
                print('您猜的数小了    当前余额',jinqian)
                print('是否花费150金币继续获取提示  输入2(提示信息与正确结果有0-5的误差)')
                tishi = input()
                tishi =int(tishi)
                if tishi==2:
                    jinqian=jinqian-help
                    xiao=suiji-shuru+zengjia
                    print('您猜的数字比随机数小',xiao,'是否花费300金币获取详细提示（上下差2）')
                    tishi=input()
                    tishi=int(tishi)
                    if tishi == 3:
                        jinqian = jinqian - xiangxi
                        print('马上就可以获取结果了，现在只需要在花200金币就可以直接获取正确答案')
                        jinqian = jinqian - 200
                        print('心动不如行动，现在就下单输入4', jinqian)
                        tishi = input()
                        tishi = int(tishi)
                        if tishi == 4:
                            da = shuru - suiji + xx
                            print('想屁吃呢，自己猜   比正确结果大（上下差2）', da)
                        elif tishi != 4:
                            print('耍我呢，扣钱')
                            jinqian = jinqian - 500
                            print('你现在还有', jinqian)
                    break
                break
    else:
        print('恭喜您猜对了,您还有',jinqian,'金币')
        break


'''
                tishi = input('是否花费100金币继续获取提示')
                break
            elif jinqian<100:
                print('No monry to a fart tips')

        if jinqian==0 :                     #如果金钱等于0
            print('poor pussy play a hammer')
        elif cishu>=10 :
            print('菜鸡，没机会了')

'''


