import multiprocessing
import os
import time


def inputQ(queue):
    info = str(os.getpid()) + "(put):" + str(time.time())
    queue.put(info)


def outputQ(queue, lock):
    info = queue.get()
    # 具体实现上 acquire() 为一个条件阻塞函数，
    # 当有任意一个进程先进行了acquire操作后，其他进程再企图进行acquire操作时就会阻塞，
    # 直到lock对象被 release 后其他进程才可进行下次acquire操作
    lock.acquire()
    print(str(os.getpid()) + "(get):" + info)
    lock.release()


if __name__ == "__main__":

    record1 = []
    record2 = []
    lock = multiprocessing.Lock()  # 加锁，为防止散乱的打印
    queue = multiprocessing.Queue(3)

    for i in range(10):
        process = multiprocessing.Process(target=inputQ, args=(queue,))
        process.start()
        record1.append(process)

    for i in range(10):
        process = multiprocessing.Process(target=outputQ, args=(queue, lock))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()

    queue.close()  # 没有更多的对象进来，关闭queue

    for p in record2:
        p.join()
