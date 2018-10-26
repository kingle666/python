import threading
import time
def coding():
    for x in range(3):
        print('一一一一一%s' % threading.current_thread())
        time.sleep(1)

def drawing():
    for x in range(3):
        print('二二二二二二%s ' % threading.current_thread())
        time.sleep(1)
# def single_thread():
#     coding()
#     drawing2()
def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    t1.start()
    t2.start()
    print(threading.enumerate())
if __name__ =='__main_':
    main()