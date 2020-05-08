import threading
import socket


def recv(udp_socket):
    '''接受数据'''
    while True:
        recv_data = udp_socket.recv(1024)
        print(recv_data)


def send(udp_socket, dest_ip, dest_port):
    '''发送数据'''
    while True:
        content = input("输入信息：")
        udp_socket.sendto(content.encode("utf-8"), (dest_ip, dest_port))


def main():
    '''聊天器的主要逻辑'''
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定端口
    udp_socket.bind(('', 7890))

    # 3. 获取对方ip和port
    dest_ip = input("输入对方ip：")
    dest_port = int(input("输入对方port："))

    # 4. 创建两个线程
    t_recv = threading.Thread(target=recv, args=(udp_socket,))
    t_send = threading.Thread(target=send, args=(udp_socket, dest_ip, dest_port))
    t_recv.start()
    t_send.start()


if __name__ == '__main__':
    main()
