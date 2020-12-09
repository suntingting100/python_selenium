# 计算器类
class Count:

    # 通过__init__()方法对两个数进行初始化
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    # 计算加法，创建add()方法返回两个数相加的结果
    def add(self):
        return self.a + self.b

    # 计算减法
    def sub(self):
        return self.a - self.b
