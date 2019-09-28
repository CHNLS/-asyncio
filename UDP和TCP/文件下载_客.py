import socket

HOST = 'localhost'
PORT = 12345
ADDR = (HOST, PORT)

client_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_soc.connect(ADDR)

# while True:
file_name = input('输入要下载的文件名>')
file_name_data = client_soc.send(file_name.encode('utf-8'))

save_file_name = input('输入保存信息文件名>')


with open('./%s' % save_file_name, 'wb') as file:
    while True:
        file_data = client_soc.recv(1024)
        if file_data:
            file.write(file_data)

        else:
            break

client_soc.close()
