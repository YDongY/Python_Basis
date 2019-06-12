import socket
import time

client_socket_list = list()


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(("", 7890))
    tcp_socket.listen(128)
    # 设置套接字为非堵塞
    tcp_socket.setblocking(False)

    while True:
        # time.sleep(0.5)
        try:
            new_client_socket, new_client_addr = tcp_socket.accept()
        except:
            print("---没有客户端链接---")
        else:
            print("----没有异常，客户端已连接----")
            new_client_socket.setblocking(False)
            client_socket_list.append(new_client_socket)

        for client_socket in client_socket_list:
            try:
                message = client_socket.recv(1024)
            except:
                print("-----这个客户端没有发送数据过来-----")
            else:
                if message:
                    print("-----客户端发送过来了数据-----", message)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)
                    print("******客户端已经断开连接******")


if __name__ == '__main__':
    main()
