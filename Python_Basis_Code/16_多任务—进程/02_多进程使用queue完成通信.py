import multiprocessing


def download_to_web(q):
    '''获取数据'''
    # 模拟从网上获取数据
    data = [11, 22, 33, 44, 55, 66]

    # 将数据写入队列
    for i in data:
        q.put(i)
    print("------数据写入队列完毕----")


def deal_data(q):
    '''处理数据'''
    data = list()
    while not q.empty():
        data.append(q.get())
    print(data)


def main():
    # 创建一个队列
    q = multiprocessing.Queue()
    # 创建多个进程
    p1 = multiprocessing.Process(target=download_to_web, args=(q,))
    p2 = multiprocessing.Process(target=deal_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
