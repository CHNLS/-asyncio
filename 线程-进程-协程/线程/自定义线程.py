import threading


class MyThread(threading.Thread):

    def __init__(self, msg1, msg2):
        # 继承父类属性
        super().__init__()
        self.msg1 = msg1
        self.msg2 = msg2

    def test1(self):
        print(self.msg1)

    def test2(self):
        print('%s' % self.msg2)

    def run(self):
        self.test1()
        self.test2()


my_thread = MyThread('子线程1', '子线程2')
# 启动线程start方法,start方法内部调用run方法(创建的子线程调用)
my_thread.start()

# 自定义线程不能使用参数target,自定义线程里面的任务都统一在run方法里面执行
# 启动线程统一调用start方法，不要直接调用run方法, 使用子线程调用run方法.
# 直接调用run方法则是主线程调用,这样不是使用子线程去执行任务
