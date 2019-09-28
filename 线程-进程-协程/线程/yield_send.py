# -*- coding:utf-8 -*-
def func():
    val = yield 1
    print(val)
    yield 2


f = func()
print(next(f))
# 调用send向生成器发送值
f.send(3)
f.close()
# next(f)
# print(next(f))
# 主动扔异常
# f.throw(Exception, "a error")
