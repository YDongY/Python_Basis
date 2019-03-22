import socket


def send_file_to_client(client_socket):
    file_name = client_socket.recv(1024).decode("utf-8")
    content = None
    try:
        f = open(file_name, 'rb')
        content = f.read()
        f.close()
    except Exception as ret:
        print("没有此文件%s" % file_name)

    if content:
        client_socket.send(content)


def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))

    # 3. 将套接字有主动变为被动（listen）
    tcp_server_socket.listen(128)

    # 4. 等待客户端链接
    while True:
        client_socket, client_addr = tcp_server_socket.accept()
        print("----客户端链接----")
        print(client_addr)

        # 5. 收发数据
        send_file_to_client(client_socket)

        # 6. 关闭套接字
        client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
