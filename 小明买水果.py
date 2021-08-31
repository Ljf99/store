dict={'k1':'v1','k2':'v2','k3':'v3'}


'''
#value

for i in dict.values():
    print(i)

'''

'''
#key

for i in dict.keys():
        print(i)
'''
'''
#增加     k4:v4
dict['k4']='v4'
print(dict)
'''
info={
    '苹果':32.8,
    '香蕉':22,
    '葡萄':15.5
}
friuts={
    '苹果':'12.3',
    '草莓':'4.5',
    '香蕉':'6.3',
    '葡萄':'5.8',
    '橘子':'6.4',
    '樱桃':'15.8'
}

info={
    '小明':{
        'fruits':{'苹果':4,'草莓':13,'香蕉':10},
        'money':{'苹果':4*12.3,'草莓':13*4.5,'香蕉':10*6.3}
     },
    '小刚':{
        'fruits':{'葡萄':19,'橘子':12,'樱桃':30},
        'money':{'葡萄':19*5.8,'橘子':12*6.4,'樱桃':30*15.8}
    }
}
print('小明',end=' ')
print(sum(info['小明']['money'].values()))
print('小刚',end=' ')
print(sum(info['小刚']['money'].values()))
# print(info['小明'])
# print(info['小刚'])









