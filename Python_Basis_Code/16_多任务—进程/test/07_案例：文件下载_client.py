import socket


def main():
    # 1. 创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 获取服务器的ip和port
    server_ip = input("输入ip地址：")
    server_port = int(input("输入端口号："))
    # 3. 链接服务器
    tcp_client_socket.connect((server_ip, server_port))
    # 4. 获取下载文件的名字
    file_name = input("输入想要下载文件的名字：")
    # 5. 将名字发送到服务器
    tcp_client_socket.send(file_name.encode("utf-8"))
    # 6. 接受文件中的数据
    recv_data = tcp_client_socket.recv(1024)  # 1K的数据
    if recv_data:
        # 7. 保存数据到一个文件中
        with open("[附件]" + file_name, 'wb') as f:
            f.write(recv_data)
    # 8. 关闭套接字
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
