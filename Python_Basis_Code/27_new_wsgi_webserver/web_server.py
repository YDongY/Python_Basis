import socket
import multiprocessing
import re
import mini_frame


class WSGIServer(object):
    def __init__(self):
        # 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 完成3次握手和4次挥手
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定
        self.tcp_server_socket.bind(("", 7890))
        # 监听
        self.tcp_server_socket.listen(128)

    # 客户端处理线程
    def deal(self, client_socket):
        request_content = client_socket.recv(1024).decode("utf-8")
        ret = re.match(r"GET (/.*) HTTP/1.1", request_content)
        if ret:
            # 得到（）内的结果
            title = ret.group(1)
            # print(title)
            if title == "/":
                title = "/index.html"
            if title.endswith(".html"):
                self.response_static_content(client_socket, title)
            else:
                self.response_dynamic_content(client_socket, title)

        client_socket.close()

    # 静态响应处理
    def response_static_content(self, client_socket, title):
        # print("=========")
        # print(title)
        try:
            f = open("./html" + title, 'rb')
        except:
            f = open("./html/404.html", "rb")
            content = f.read()
            f.close()
            client_socket.send(b"HTTP/1.1 200 OK\r\n" + b"\r\n" + content)
        else:
            content = f.read()
            f.close()
            client_socket.send(b"HTTP/1.1 200 OK\r\n" + b"\r\n" + content)

    # 动态相应处理
    def response_dynamic_content(self, client_socket, title):
        header = "HTTP/1.1 200 OK\r\n"
        header += "\r\n"
        env = dict()
        body = mini_frame.application(env, self.set_response_header)
        response = header + body
        client_socket.send(response.encode("utf-8"))

    def set_response_header(self, status, headers):
        pass

    def run_forever(self):
        # 等待客户端链接
        while True:
            print("----------服务器已经运行-----------")
            client_socket, client_addr = self.tcp_server_socket.accept()
            # 每链接一个客户端，开启一个进程
            p = multiprocessing.Process(target=self.deal, args=(client_socket,))
            p.start()
            client_socket.close()
        self.tcp_server_socket.close()


def main():
    # 完成主要逻辑
    server = WSGIServer()
    server.run_forever()


if __name__ == '__main__':
    main()
