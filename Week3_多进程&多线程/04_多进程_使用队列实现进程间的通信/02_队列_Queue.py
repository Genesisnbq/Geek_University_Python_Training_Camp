# multiprocessing 支持进程之间的两种通信通道
# 队列
# 来自官方文档的一个简单demo
# Queue类是一个近似 queue.Queue的克隆
# 现在有这样一个需求, 我们有两个进程, 一个负责写(write), 一个进程负责读(read)\
# 当写的进程写完某部分以后要把数据交给读的进程进行使用
# write() 将写完的数据交给队列, 再由队列交给read()

from multiprocessing import Queue, Process


def f(q):
    q.put(['倪彬琪', '刘亦菲'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()

# 队列是线程和进程安全
