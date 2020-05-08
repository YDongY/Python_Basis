import socket
import threading
import re


def response_content(client_socket, title):
    if title != "favicon.ico":
        try:
            f = open(title, "rb")
        except:
            f = open("404.html", "rb")
            content = f.read()
            f.close()
            client_socket.send(b"HTTP/1.1 200 OK\r\n" + b"\r\n" + content)
        else:
            content = f.read()
            f.close()
            client_socket.send(b"HTTP/1.1 200 OK\r\n" + b"\r\n" + content)
    client_socket.close()


def deal(client_socket):
    request_content = client_socket.recv(1024).decode("utf-8")
    # print(request_content)
    ret = re.match(r"GET (/.*) HTTP/1.1", request_content)
    if ret:
        title = ret.group(1)
        print(title)
        if title == "/":
            title = "/index.html"
        response_content(client_socket, title[1:])
    client_socket.close()


def main():
    # 1. 创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 完成3次握手4次挥手，重复使用端口
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2. 绑定
    tcp_socket.bind(("", 7890))
    # 3. 监听
    tcp_socket.listen(128)
    # 4. 等待链接
    while True:
        print("----服务器已经开启----")
        client_socket, client_addr = tcp_socket.accept()
        # 开启线程
        # threading.Thread(target=deal, args=(client_socket,)).start()
        deal(client_socket)
    # tcp_socket.close()


if __name__ == '__main__':
    main()
