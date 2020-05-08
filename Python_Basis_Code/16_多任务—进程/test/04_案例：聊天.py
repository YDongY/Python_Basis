import socket


def send_message(udp_socket):
    dest_ip = input("输入对方的ip：")
    dest_port = int(input("输入对方的port："))
    message = input("输入发送的消息：")
    udp_socket.sendto(message.encode("gbk"), (dest_ip, dest_port))


def recv_message(udp_socket):
    content = udp_socket.recvfrom(1024)
    return content


def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # 2. 发送数据
        send_message(udp_socket)

        # 3. 接受数据
        content = recv_message(udp_socket)
        if content[0].decode("utf-8") == "exit":
            break
        print("%s:%s" % (content[1], content[0].decode("utf-8")))

    # 4. 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
