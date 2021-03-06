import socket


def main():
    # 1. 创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 链接服务器
    server_ip = input("请输入链接的ip：")
    server_port = int(input("请输入链接的port:"))
    server_addr = (server_ip, server_port)
    tcp_client_socket.connect(server_addr)

    # 3. 收发数据
    content = input("发送消息：")
    tcp_client_socket.send(content.encode("gbk"))
    recv_message = tcp_client_socket.recv(1024)
    print(recv_message.decode("utf-8"))
    # 4. 关闭套接字
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
