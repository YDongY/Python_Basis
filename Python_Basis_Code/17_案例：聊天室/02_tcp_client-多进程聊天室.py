import multiprocessing
import socket
import time


def send_message(client_socket):
    while True:
        message = input("输入消息：")
        client_socket.send(message.encode("utf-8"))


def recv_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(message)
            else:
                break
        except:
            pass


def main():
    # 创建套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 链接服务器
    client_socket.connect(("127.0.0.1", 8080))

    p1 = multiprocessing.Process(target=recv_message, args=(client_socket,))
    p1.start()
    send_message(client_socket)


if __name__ == '__main__':
    main()
