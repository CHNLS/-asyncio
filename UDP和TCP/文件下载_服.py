import socket

import os

HOST = ''
PORT = 12345
ADDR = (HOST, PORT)

server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定端口
server_soc.bind(ADDR)
# 监听
server_soc.listen(128)

while True:
    print('等待连接...')
    conn, addr = server_soc.accept()
    file_name_data = conn.recv(1024)

    # 判断文件存不存在
    if os.path.exists('./%s' % file_name_data.decode('utf-8')):
        with open('./%s' % file_name_data.decode('utf-8'), 'rb') as file:
            while True:
                file_data = file.read(1024)
                if file_data:
                    conn.send(file_data)

                else:
                    break

    else:
        print('文件不存在')

    conn.close()
server_soc.close()