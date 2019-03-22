import socket
import threading


class Server():
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = "127.0.0.1"
        self.port = 7890
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(128)
        self.client_dic = dict()
        self.client_list = list()
        self.main()

    def main(self):
        print("-----服务器已开启-----")
        while True:
            # 等待客户端链接
            client_socket, client_addr = self.server_socket.accept()
            print(client_addr, "已登录")

            # 每链接一个客户端，开启一个线程
            # client_socket.fileno():套接字的文件描述符
            threading.Thread(target=self.handler, args=(client_socket, client_socket.getpeername())).start()

    def handler(self, client_socket, client_id):
        print(client_id)
        # 接受客户端发过来的名字
        client_name = client_socket.recv(1024).decode("utf-8")
        # 将名字添加到字典中，例：{510:ydy}
        self.client_dic[client_id] = client_name
        print(self.client_dic)
        # 将链接的客户端socket添加到列表中
        self.client_list.append(client_socket)
        print(self.client_list)
        # 将上线消息发送给所有人
        self.send__to_all_client(client_id, '【系统提示：' + self.client_dic[client_id] + ' 进入聊天室】')
        while True:
            try:
                recv_message = client_socket.recv(1024).decode()
                if recv_message:
                    print(self.client_dic[client_id], ":", recv_message)
                    self.send__to_all_client(client_id, self.client_dic[client_id] + ":" + recv_message)

            except:
                break

    def send__to_all_client(self, client_id, message_content):
        for client in self.client_list:
            if client.getpeername() != client_id:
                try:
                    client.send(message_content.encode("utf-8"))
                except:
                    pass


if __name__ == '__main__':
    server = Server()
