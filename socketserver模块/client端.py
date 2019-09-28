import socket

HOST = "localhost"
PORT = 5656
ADDR = (HOST, PORT)

client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_soc.connect(ADDR)

while True:

    data = input("信息>")
    if data == "q": break
    client_soc.send(data.encode("utf-8"))

    data_recv = client_soc.recv(1024)
    if not data_recv:
        break
    print("服务端信息>%s" % data_recv.decode("utf-8"))

client_soc.close()