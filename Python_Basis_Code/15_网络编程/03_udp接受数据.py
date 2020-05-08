import socket


def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 绑定端口号
    local_addr = ('', 7788)
    udp_socket.bind(local_addr)
    # 3. 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        # 4. 打印收到的数据 , (b'http://www.cmsoft.cn', ('192.168.0.102', 8080))
        recv_message = recv_data[0]  # 存储数据
        send_addr = recv_data[1]  # 存储发送方的信息
        print("%s:%s" % (str(send_addr), recv_message.decode("gbk")))
    # 5. 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
