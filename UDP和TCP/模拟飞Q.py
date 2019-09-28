import socket
# import random

# 利用socket模块生成套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 设置socket的选项，允许发送广播消息
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)


# 定义一个元组,包含ip地址,和端口号,ip地址必须为字符串,端口号为
# 数字 飞秋的默认端口为2425

addr = ("192.168.24.255", 2425)
while True:
    msg = input("输入信息>")
    # 定义字符串 其中1表示版本2356表示包号 这里可以自由设置
    # 和主机名 32表示发送消息 我无敌是发送的内容 这个是固定的格式
    info = "1:2356:来找我啊:来找我啊:32:%s" % msg
    s.sendto(info.encode("gbk"), addr)

    data, addr = s.recvfrom(4096)
    if not data: break
    print(data.decode("utf-8"))


s.close()
