import socket
import time
import re
import select  # 用于linux

# 1. 特殊内存：kernel 和 应用程序共享
# 2. 事件通知的方式
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

    # 创建一个epoll对象，用于Linux
    epl = select.epoll()
    epl.register(tcp_socket, select.EPOLLIN)  # 注册
    fd_event_dict = dict()

    while True:
        # time.sleep(0.5)
        # 默认会堵塞，直到os监测到数据到来，
        # 通知事件的方法告诉程序，解堵塞，返回有反应的列表
        fd_event_list = epl.poll()
        # [(fd,event],(套接字文件描述符，事件类型)
        for fd, event in fd_event_list:
            if fd == tcp_socket.fileno():
                new_client_socket, new_client_addr = tcp_socket.accept()
                epl.register(new_client_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_client_socket.fileno()] = new_client_socket
            elif event == select.EPOLLIN:
                # 判断已经有链接的客户但是否有数据发过来
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    deal(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)  # 注销
                    del fd_event_dict[fd]
    # 关闭监听套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
