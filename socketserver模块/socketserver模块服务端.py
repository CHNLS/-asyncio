from socketserver import TCPServer as TCP, StreamRequestHandler as SRH

HOST = ''
PORT = 12465
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):

    # 重写handle方法，该方法在基类中没有任何行为，即pass
    def handle(self):
        print("连接自：", self.client_address)
        self.wfile.write(self.rfile.readline())


tcp_ser = TCP(ADDR, MyRequestHandler)
print("等待连接...")
tcp_ser.serve_forever()
