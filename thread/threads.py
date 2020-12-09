from time import sleep, ctime
import threading


# 音乐播放器 func：播放文件  loop:播放次数
def music(func, loop):
    for i in range(loop):
        print("I was listening to %s! %s" % (func, ctime()))
        sleep(2)


# 视频播放器
def movie(func, loop):
    for i in range(loop):
        print("I was at the %s! %s" % (func, ctime()))
        sleep(5)

# 创建线程数组
threads = []

# 创建线程t1,并添加到线程数组   调用threading模块的Thread()方法来创建线程
t1 = threading.Thread(target=music, args=("爱情买卖", 2))
threads.append(t1)

# 创建线程t2 ,并添加到线程数据组
t2 = threading.Thread(target=movie, args=("阿凡达", 2))
threads.append(t2)

if __name__ == "__main__":
    # 启动线程
    for t in threads:
        t.start()
    # 守护线程
    for t in threads:
        # join()方法是等待线程终止，如果不使用join方法对每个线程做等待终止，那么在线程运行的过程中可能回去执行最后的打印"all end"
        t.join()

    print("all end: %s" % ctime())









