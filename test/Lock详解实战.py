import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()
gTotalTimes = 10
gTimes = 0


class Produer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            if gTimes >= 10:
                gLock.release()
                break
            gMoney += money
            print('%s生产%d元钱,剩余%d元钱' % (threading.current_thread(), money, gMoney))
            gTimes += 1
            gLock.release()
            time.sleep(0.5)
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费了%d元钱,剩余%d元钱' % (threading.current_thread(), money, gMoney))
            else:
                if gTimes >= gTotalTimes:
                    gLock.release()
                    break
                print('%s准备消费了%d元钱,余额布置' % (threading.current_thread(), money, gMoney))
            gLock.release()
            time.sleep(0.5)
def main():
    for x in range(5):
        t = Produer(name='生产者%d' % x)
        t.start()
    for x in range(3):
        t = Consumer(name='消费者%d' % x)
        t.start()
if __name__ == '__main__':
    main()