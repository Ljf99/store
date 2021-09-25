from threading import Thread
import threading
import time
import random


LZ=500
DT=2
a=threading.RLock()


class chef(Thread):
    name = ''
    # efficiency = random.randint(0, 2)
    efficiency = 1
    def run(self) -> None:
        while True:
            global LZ
            if LZ<500:
                a.acquire()
                LZ = LZ+self.efficiency
                print(self.name,'做了',self.efficiency,'现在有', LZ, '个蛋挞')
                time.sleep(0.1)
                a.release()
            elif LZ == 500 :
                a.acquire()
                print('现在有',LZ,'个蛋挞')
                time.sleep(3)
                a.release()
            else:
                print('篮子满了')
                break






class client(Thread):
    buyer =''
    count = 0
    money =3000
    def run(self) -> None:
        global LZ
        while True:
            if LZ >0 and self.money > 0:
                a.acquire()
                LZ=LZ-1
                self.money=self.money-DT
                self.count=self.count+1
                print(self.buyer,'买了',self.count,'还有',self.money,'元')
                a.release()
            elif LZ == 0 and self.money > 0:
                time.sleep(2)
            elif self.money == 0:
                a.acquire()
                print('篮子有',LZ,'个蛋挞',self.buyer,'有',self.money,'元')
                a.release()
        return









b1=client()
b2=client()
b3=client()
b4=client()
b5=client()
b6=client()
b1.buyer='买家1'
b2.buyer='买家2'
b3.buyer='买家3'
b4.buyer='买家4'
b5.buyer='买家5'
b6.buyer='买家6'
b1.start()
b2.start()
b3.start()
b4.start()
b5.start()
b6.start()

c1 =chef()
c2 =chef()
c3 =chef()
c1.name='厨师1'
c2.name='厨师2'
c3.name='厨师3'
c1.start()
c2.start()
c3.start()



