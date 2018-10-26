import threading
VALUE = 0
gLock = threading.Lock()
def add_value():
    gLock.acquire()
    global VALUE #使用全局的变量,不是自己的
    for x in range(100000):
        VALUE += 1
    gLock.release()
    print('value: %d' %VALUE)
def main():
    for x in range(2):
        t = threading.Thread(target=add_value())
        t.start()
if __name__ == '__main__':
    main()