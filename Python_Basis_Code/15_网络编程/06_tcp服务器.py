import socket


def main():
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定
    tcp_server_socket.bind(("", 7890))

    # 3. 将套接字有主动变为被动（listen）
    tcp_server_socket.listen(128)
    print("----开启监听----")

    # 4. 等待客户端链接
    client_socket, client_addr = tcp_server_socket.accept()
    print("----客户端链接----")
    print(client_addr)
    print(client_socket.fileno())

    # 5. 收发数据
    content = client_socket.recv(1024)
    print(content.decode("utf-8"))
    message = input("发送消息：")
    client_socket.send(message.encode("gbk"))

    # 6. 关闭套接字
    client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
