import threading
import time
class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('一一一一一%s' % threading.current_thread())
            time.sleep(1)
class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('二二二二二二%s ' % threading.current_thread())
            time.sleep(1)
def main():
    t1 = CodingThread()
    t2 = CodingThread()

    t1 = start()
    t2 = start()

if __name__ == '__main__':
    main()