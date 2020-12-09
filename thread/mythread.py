import threading
from time import sleep, ctime


# 创建线程类
# 创建MyThread类，用于继承threading.Thread类
class MyThread(threading.Thread):
    # 用__init__类方法对func,args,name等参数进行初始化
    def __init__(self, func, args, name=""):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        # args是一个包含将要提供给函数的按位置传递的参数的元组，如果省略了args，则任何参数都不会被传递
        self.func(*self.args)


def super_play(file_, time):
    for i in range(2):
        print("Start playing: %s! %s" % (file_, ctime()))
        sleep(time)


lists = {"爱情买卖.mp3": 3, "阿凡达": 5, "我和你": 4}

threads = []
files = range(len(lists))

for file_, time in lists.items():
    t = MyThread(super_play, (file_, time), super_play.__name__)
    threads.append(t)

if __name__ == "__main__":
    # 启动线程
    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()

    print("end: %s" % ctime())

