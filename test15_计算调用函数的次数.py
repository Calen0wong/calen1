# def set_func(func):
#     num = [0]   # 闭包中外函数中的变量指向的引用不可变
#
#     def call_func():
#         func()
#         num[0] += 1
#         print("执行次数",num[0])
#     return call_func
#
#
# # 待测试方法
# @set_func
# def test():
#     pass
#
#
# test()
# test()
# test()

# 执行次数 1
# 执行次数 2
# 执行次数 3
import time


def fun_count(func):
    num = [0]  # 外部函数的变量不会改变

    def call_fun():
        func()
        num[0] += 1
        print("函数调用了%s 次" % num[0])
    return call_fun


@fun_count
def test():
    print("hahah")

test()
time.sleep(1)
test()
time.sleep(1)
test()

