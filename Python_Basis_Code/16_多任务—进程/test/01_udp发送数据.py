# udp
import socket


def main():
    # 1. 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2. 收发数据
    udp_socket.sendto(b"hahahah", ("192.168.0.102", 8080))
    # 3. 关闭socket
    udp_socket.close()


if __name__ == '__main__':
    main()
