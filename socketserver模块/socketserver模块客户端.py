from socket import *

HOST = 'localhost'
PORT = 12465
ADDR = (HOST, PORT)


while True:
    cli_soc = socket(AF_INET, SOCK_STREAM)
    cli_soc.connect(ADDR)
    data = input("输入信息>")
    if data:
        cli_soc.send(data.encode("utf-8"))
    else:
        break
    data = cli_soc.recv(1024)
    if data:
        print(data.decode("utf-8"))
    else:
        break

cli_soc.close()
