import socket
import threading


class Client(object):
    def __init__(self, dest_ip, dest_port, name):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.dest_ip = dest_ip
        self.dest_port = dest_port
        self.name = name
        self.main()

    def send_to_message(self):
        while True:
            content = input("发送消息：")
            self.tcp_socket.send(content.encode("utf-8"))

    def recv_message(self):
        while True:
            try:
                message_data = self.tcp_socket.recv(1024)
                if not message_data:
                    break
                print(message_data.decode("utf-8"))
            except:
                break

    def main(self):
        '''主要逻辑'''
        # 1. 链接服务器
        try:
            self.tcp_socket.connect((dest_ip, dest_port))
            self.tcp_socket.send(self.name.encode("utf-8"))
        except ConnectionRefusedError as ret:
            print(ret)
            return

            # 2. 发送消息线程
        t1 = threading.Thread(target=self.send_to_message)

        # 3. 接受消息线程
        t2 = threading.Thread(target=self.recv_message)

        # 开启线程
        t1.start()
        t2.start()


if __name__ == '__main__':
    # 输入服务器ip和port
    name = input("输入名字：")
    dest_ip = input("输入ip地址：")
    dest_port = int(input("输入port:"))
    client = Client(dest_ip, dest_port, name)
