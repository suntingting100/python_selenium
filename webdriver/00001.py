# # 定义了支持参数收集的函数
# def test(*books, num):
#     print(books)
#     # books被当成元组处理
#     for b in books:
#         print(b)
#     print(num)
# # 调用test()函数
# test("疯狂ios讲义", "疯狂的Android讲义",num=20)
#
# # 定义了支持参数收集的函数
# def test(x, y, z=3, *books, **scores):
#     print(x, y, z)
#     print(books)
#     print(scores)
# test(1, 2, 3, "疯狂ios讲义", "疯狂Android讲义", 语文=89, 数学=90)


# def test(name, message):
#     print("用户是：", name)
#     print("欢迎消息是： ", message)
# my_list = ["孙悟空", "欢迎来疯狂软件"]
# test(*my_list)
#
# def foo(name, *nums):
#     print("name参数：", name)
#     print("nums参数：", nums)
# my_tuple = (1, 2, 3)
# foo("fkit", *my_tuple)
#
# foo(*my_tuple)
# foo(my_tuple)
#
# def bar(book, price, desc):
#     print(book, "这本书的价格是:", price)
#     print("描述信息", desc)
# my_dict = {"price":89, "book":"疯狂python讲义", "desc": "这是一本系统全面的python学习图书"}
#
# bar(**my_dict)

# def swap(a, b):
#     # 下面代码实现a,b变量的值交换
#     a, b = b, a
#     print("在swap函数里，a的值是", a, "b的值是", b)
# a = 6
# b = 9
# swap(a, b)
# print("交换结束后，变量a的值是", a, "变量b的值是", b)

# def test():
#     age = 20
#     # 直接访问age局部变量
#     print(age)
#     # 访问函数局部范围内的“变量数组”
#     print(locals())
#     # 通过函数局部范围内的“变量数组”访问age变量
#     print(locals()["age"])
#     # 通过locals函数局部范围内的“变量数组”改变age变量的值
#     locals()["age"] = 12
#     # 再次访问age变量的值
#     print("xxx", age)
#     # 通过globas函数修改全局变量
#     globals()["x"] = 19
# x = 5
# y = 20
# print(globals())
# # 在全局范围内使用locals函数，方位的是全局变量的“变量数组”
# print(locals())
# # 直接访问x变量
# print(x)
# # 通过全局变量的“变量数组”访问x全局变量
# print(globals()["x"])
# #  通过全局变量的“变量数组”对X全局变量赋值
# globals()["x"] = 39
# print(x)
#
# name = "chairs"
# def test():
#     print(globals()["name"])
#     name = "孙悟空"
# test()
# print(name)

# name = "chairs"
# def test():
#     global name
#     print(name)
#     name = "孙悟空"
# test()
# print(name)

# 定义函数，该函数会包含局部函数
# def get_math_func(type, nn):
#     # 定义一个计算平方的局部函数
#     def square(n):
#         return n * n
#     # 定义一个计算立方的局部函数
#     def cube(n):
#         return n * n * n
#     def factorial(n):
#         result = 1
#         for index in range(2, n+1):
#             result *= index
#         return result
#     # 调用局部函数
#     if type == "square":
#         return square(nn)
#     if type == "cube":
#         return cube(nn)
#     else:
#         return factorial(nn)
#
#
# print(get_math_func("square", 3))
# print(get_math_func("cube", 3))
# print(get_math_func("", 3))

# def foo():
#     # 局部变量name
#     name = "Chairs"
#     def bar():
#         nonlocal name
#         # 在访问bar函数所在的foo函数内的name局部变量
#         print(name)
#         name = "孙悟空"
#     bar()
# foo()

# # 定义一个计算乘方的函数
# def pow(base, exponent):
#     result = 1
#     for i in range(1, exponent + 1):
#         result *= base
#     return result
# # 将pow函数赋值给my_fun,则my_fun可被当成pow使用
# my_fun = pow
# print(my_fun(3, 4))
#
#
# # 定义一个计算面积
# def area(width, height):
#     return width * height
# my_fun = area
# print(my_fun(3, 4))

# # 定义函数类型的形参，其中fn是一个函数
# def map(data, fn):
#     result = []
#     # 遍历data中的每个元素，并用fn函数对每个元素进行计算
#     # 然后将计算结果作为新数组的元素
#     for e in data:
#         result.append(fn(e))
#     return result
# def square(n):
#     return n * n
# def cub(n):
#     return n * n * n
# def factorial(n):
#     result = 1
#     for index in range(2, n+1):
#         result *= index
#     return result
#
# data = [3, 4, 9, 5, 8]
# print("原数据：", data)
# print("计算数组元素的平方")
# print(map(data, square))
# print("计算数组元素的立方")
# print(map(data, cub))
# print("计算数组元素的阶乘")
# print(map(data, factorial))
# print(type(map))

# def get_math_func(type):
#     result = 1
#     if type == "square":
#         return lambda n : n * n
#     elif type == "cube":
#         return lambda n : n * n * n
#     else:
#         return lambda n : (1 + n) * n / 2
# math_func = get_math_func("cube")
# print(math_func(5))
# math_func = get_math_func("square")
# print(math_func(5))
# math_func = get_math_func("other")
# print(math_func(5))

# # 传入计算平方的lambda表达式作为参数
# x = map(lambda x : x*x, range(8))
# print([e for e in x])
# y = map(lambda x : x*x if x % 2 == 0 else 0, range(8))
# print([e for e in y])

# class person:
#     # 这是学习python定义的一个person类
#     hair = "black"
#     def __init__(self, name="chairs", age=8):
#         self.name = name
#         self.age = age
#     # 下面定义了一个say方法
#     def say(self, content):
#         print(content)
#
# p = person()
# # 输出p的name、age实例变量
# print(p.name, p.age)
# # 访问p的name实例你变量，直接为该实例变量赋值
# p.name = "李刚"
# #调用p的say（）方法，在声明say()方法时定义了两个形参
# # 但在第一个形参（self）是自动绑定的，因此调用该方法只需为第二个形参指定一个值
# p.say("python语言很简单，学习很容易")
# print(p.name, p.age)

# # 为p对象增加一个skills实例变量
# p.skills = ["programming", "swimming"]
# print(p.skills)
# del p.name
# print(p.name)
#
# # 先定义一个函数
# def info(self):
#     print("-------info函数-------")
# # 使用info对p的foo方法赋值（动态增加方法）
# p.foo = info
# # python不会自动将调用者绑定到第一个参数
# # 因此程序需要手动将调用者绑定到第一个参数
# p.foo(p)
#
# # 使用lambda表达式为p对象的bar方法赋值（动态增加方法）
# p.bar = lambda self : print("-----lambda-----", self)
# p.bar(p)
# class person:
#     # 这是学习python定义的一个person类
#     hair = "black"
#     def __init__(self, name="chairs", age=8):
#         self.name = name
#         self.age = age
#     # 下面定义了一个say方法
#     def say(self, content):
#         print(content)
# p = person()
#
# def intro_func(self, content):
#     print("我是一个人，信息为：%s" % content)
#         # 导入methodtype
# from types import MethodType
#     # 使用MethodType对intro_func进行封装，将该函数的第一个参数绑定为p
# p.intro = MethodType(intro_func, p)
# p.intro("生活在别处")

# class Dog:
#     # 定义一个jump方法
#     def jump(self):
#         print("正在执行jump方法")
#     # 定义一个run方法
#     def run(self):
#         self.jump()
#         print("正在执行run方法")


# class InConstructor:
#     def __init__(self):
#         # 在构造方法中定义一个foo变量（局部变量）
#         foo = 0
#         # 使用self代表构造方法正在初始化的对象
#         # 下面的代码将会把改构造方法正在初始化的对象的foo实例变量设为6
#         self.foo = 6
# #  所有使用Inconstructor创建的对象的foo实例变量黄贝设为6
# print(InConstructor().foo)

# class User:
#     def test(self):
#         print("self参数： ", self)
#
# u = User()
# # 以方法形式调用test()方法
# u.test()
# # 将User对象的test方法赋值给foo变量
# foo = u.test
# # 通过foo变量（函数形式）调用test（）方法
# foo()

# class ReturnSelf:
#     def grow(self):
#         if hasattr(self, "age"):
#             self.age += 1
#         else:
#             self.age = 1
#         # return self返回该调用方法的对象
#         return self
# rs = ReturnSelf()
# # 可以连续调用同一个方法
# rs.grow().grow().grow()
# print("rs的age属性值是：", rs.age)

# # 定义全局变量的foo函数
# def foo():
#     print("全局空间的foo方法")
# # 定义全局空间的bar变量
# bar = 20
# class Bird:
#     def foo(self):
#         print("Bird空间的foo方法")
#     # 定义Bird空间的bar变量
#     bar = 200
# # 调用全局空间的函数和变量
# foo()
# print(bar)
# Bird().foo()
# print(Bird.bar)

# class User:
#     def walk(self):
#         print(self, "正在慢慢地走")
# # 通过类调用实例方法
# User.walk("fkit")

# class Bird:
#     @classmethod
#     def fly(cls):
#         print("类方法fly:", cls)
#     @staticmethod
#     def info(p):
#         print("静态方法：", p)
# Bird.fly()
# Bird.info("crazyit")
#
# # 创建Bird对象
# b = Bird()
# b.fly()
# b.info("fkit")

# def funA(fn):
#     print("A")
#     fn()
#     return "fkit"
# """
# 下面的装饰器效果相当于funA(funB)
# funB将会被替换(装饰)成该语句的返回值
# 由于funA函数返回fkit,因此funB就是
# """
# @funA
# def funB():
#     print("B")
# print(funB)

# def foo(fn):
#     # 定义一个嵌套函数
#     def bar(*args):
#         print("===1===", args)
#         n = args[0]
#         print("===2===", n * (n - 1))
#         # 查看传给foo函数的fn函数
#         print(fn.__name__)
#         fn(n * (n - 1))
#         print("*" * 15)
#         return fn(n * (n - 1))
#     return bar
# @foo
# def my_test(a):
#     print("==my_test函数==", a)
# print(my_test)
# my_test(10)
# my_test(6, 5)

# def auth(fn):
#     def auth_fn(*args):
#         print("--------模拟执行权限检查--------")
#         fn(*args)
#     return auth_fn
# @auth
# def test(a, b):
#     print("执行test函数，参数a: %s,参数b: %s" % (a, b))
# test(20, 15)

xxxxx