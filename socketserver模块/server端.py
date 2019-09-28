import socketserver

HOST = ""
PORT = 5656
ADDR = (HOST, PORT)


# 必须继承类BaseRequestHandler
class MyServer(socketserver.BaseRequestHandler):
    # 必须有handle方法
    def handle(self):
        print(f"连接来自>{ADDR}")
        while True:

            data = self.request.recv(1024)
            print(data.decode("utf-8"))

            msg = input(f"回复{ADDR}>")
            self.request.send(msg.encode("utf-8"))
            # print(self.request, self.client_address, self.server)


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(ADDR, MyServer)
    print("等待连接...")
    # 服务一直执行
    server.serve_forever()



