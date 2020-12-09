from calculator import Count  # 引入calculator文件的Count类


# 测试两个整数相加
class Testcount:

    def test_add(self):
        try:
            j = Count(2, 3)  # 传入参数
            add = j.add()  # 调用add方法
            # 通过assert()方法判断add()返回的值是不是5,如果不相等则抛出自定义的"Integer addition result error"
            # assert语句--断言  用于检查表达式是否为真，如果为假，则引发AssertionError错误
            assert(add == 5), "Integer addition result error"
        except AssertionError as msg:
            print(msg)
        else:
            print("Test:pass!")  # 如果相等则打印"Test:pass!"


# 执行测试类的测试方法
mytest = Testcount()
mytest.test_add()
