import multiprocessing


def worker(i):
    for i in range(i):
        print("-----正在执行%d----" % i)


def main():
    # 创建进程池，最大进程数3
    po = multiprocessing.Pool(3)
    for i in range(10):
        po.apply_async(worker, (i,))
    print("----start---")
    po.close()
    po.join()
    print("---end----")


if __name__ == '__main__':
    main()
