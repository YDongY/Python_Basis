# udp
import socket


def main():
    # 1. 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7890))  # 可以绑定端口，也可以不绑定，系统自动分配
    while True:
        udp_data = input("输入发送的数据：")
        if udp_data == "exit":
            break
        # 2. 收发数据
        udp_socket.sendto(udp_data.encode("utf-8"), ("192.168.0.102", 8080))
    # 3. 关闭socket
    udp_socket.close()


if __name__ == '__main__':
    main()
