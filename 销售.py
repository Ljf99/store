print('----------------------------------------------衣服销售----------------------------------------------')
print('       日期            服装名称                价格/件                 库存数量              销售量每日')
print('       1 号             羽绒服                 253.6                    500                    10   ')
print('       2 号             牛仔裤                 86.3                     600                    60   ')
print('       3 号             风  衣                 96.8                     335                    43   ')
print('       4 号             皮  草                 135.9                    855                    63   ')
print('       5 号             T   恤                 65.8                     632                    63   ')
print('       6 号             衬  衫                 49.3                     562                    120  ')
print('       7 号             牛仔裤                 86.3                     600                     72  ')
print('       8 号             牛仔服                 253.6                    500                     69  ')
print('       9 号             牛仔裤                 86.3                     600                     35  ')
print('       10号             羽绒服                 135.9                    500                    140  ')
print('       11号             牛仔裤                 65.8                     600                     90  ')
print('       12号             皮  草                 96.8                     855                     24  ')
print('       13号             T   恤                 86.3                     632                     45  ')
print('       14号             风  衣                 65.8                     335                     25  ')
print('       15号             牛仔裤                 253.6                    600                     60  ')
print('       16号             T   恤                 96.8                     632                    129  ')
print('       17号             羽绒服                 65.8                     500                     10  ')
print('       18号             风  衣                 253.6                    335                     43  ')
print('       19号             T   恤                 65.8                     632                     63  ')
print('       20号             牛仔裤                 86.3                     600                     60  ')
print('       21号             皮  草                 135.9                    855                     63  ')
print('       22号             风  衣                 96.8                     335                     60  ')
print('       23号             T   恤                 65.8                     632                     58  ')
print('       24号             牛仔裤                 86.3                      600                    140  ')
print('       25号             T   恤                 65.8                     632                     48  ')
print('       26号             风  衣                 96.8                     335                     43  ')
print('       27号             皮  草                 135.9                    855                     57  ')
print('       28号             羽绒服                 253.6                    500                     10  ')
print('       29号             T   恤                 65.8                    632                     63  ')
print('       30号             风  衣                 96.8                    335                     78  ')
print('')
money=  (253.6*10+86.3*60+96.8*43+135.9*63+65.8*63+49.3*120+86.3*72+253.6*69+86.3*35+253.6*140+86.3*90+135.9*24+65.8*45+96.8*25+86.3*60+65.8*129+253.6*10+96.8*43+65.8*63+86.3*60+135.9*63+96.8*60+65.8*58+86.3*140+65.8*48+96.8*43+135.9*57+253.6*10+65.8*63+96.8*78)
money=round(money,2)
print('销售总价格:',money)
print('')
print('')
print('---------------月销量占比---------------')
print('')
yurongfu1= ((10+69+140+10+10)/(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78))
yurongfu1=round (yurongfu1,2)
print('羽绒服月销量占比:',yurongfu1,'%')
niuzaiku1= ((60+72+35+90+60+60+140)/(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78))
niuzaiku1=round(niuzaiku1,2)
print('牛仔裤月销量占比：',niuzaiku1,'%')
fengyi1=((43+25+43+60+43+78)/(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78))
fengyi1=round(fengyi1,2)
print('风衣月销量占比：',fengyi1,'%')
picao1= ((63+24+63+57)/(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78))
picao1=round(picao1,2)
print('皮草月销量占比:',picao1,'%')
tx1=((63+45+129+63+58+63)/(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78))
tx1=round(tx1,2)
print('T恤月销量占比:',tx1,'%')
chenshan1=(120/(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78))
chenshan1=round(chenshan1,2)
print('衬衫月销量占比:',chenshan1,'%')
print('')
print('')
print('---------------平均日销售量---------------')
print('')
yurongfu2=(10+69+140+10+10)/30
yurongfu2=round(yurongfu2,2)
print('羽绒服平均销量',yurongfu2,'%')
niuzaiku2=(60+72+35+90+60+60+140)/30
niuzaiku2=round(niuzaiku2,2)
print('牛仔裤平均销量',niuzaiku2,'%')
fengyi2= (43+25+43+60+43+78)/30
fengyi2=round(fengyi2,2)
print('风衣平均销量', fengyi2,'%')
picao2=(63+24+63+57)/30
picao2=round(picao2,2)
print('皮草平均销量',picao2,'%')
tx2= (63+45+129+63+58+63)/30
tx2=round(tx2,2)
print('T恤平均销量',tx2,'%')
chenshan2=120/30
chenshan2=round(chenshan2,2)
print('衬衫平均销量',chenshan2,'%')

















