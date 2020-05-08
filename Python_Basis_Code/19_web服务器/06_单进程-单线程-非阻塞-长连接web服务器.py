import socket
import time
import re

client_socket_list = list()


def response_content(client_socket, title):
    if title != "favicon.ico":
        try:
            f = open(title, "rb")
        except:
            f = open("404.html", "rb")
            content_body = f.read()
            f.close()
            content_head = "HTTP/1.1 200 OK\r\n"
            content_head += "Content-Length:%d\r\n" % len(content_body)
            content_head += "\r\n"
            response_content = content_head.encode("utf-8") + content_body
            client_socket.send(response_content)
        else:
            content_body = f.read()
            f.close()
            content_head = "HTTP/1.1 200 OK\r\n"
            content_head += "Content-Length:%d\r\n" % len(content_body)
            content_head += "\r\n"
            response_content = content_head.encode("utf-8") + content_body
            client_socket.send(response_content)


def deal(client_socket, request_content):
    # request_content = client_socket.recv(1024).decode("utf-8")
    # print(request_content)
    ret = re.match(r"GET (/.*) HTTP/1.1", request_content)
    if ret:
        title = ret.group(1)
        print(title)
        if title == "/":
            title = "/index.html"
        response_content(client_socket, title[1:])


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
                message = client_socket.recv(1024).decode("utf-8")
            except:
                print("-----这个客户端没有发送数据过来-----")
            else:
                if message:
                    # print("-----客户端发送过来了数据-----", message)
                    deal(client_socket, message)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)
                    print("******客户端已经断开连接******")
    # 关闭监听套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
