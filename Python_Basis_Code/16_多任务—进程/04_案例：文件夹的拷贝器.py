import os
import multiprocessing


def copy_file(copy_file_name, new_file_name, file_name, q):
    # 打开要拷贝的文件
    cf = open(copy_file_name + '/' + file_name, 'rb')
    content = cf.read()
    cf.close()

    # 将拷贝的文件放入到新的文件夹中
    nf = open(new_file_name + '/' + file_name, 'wb')
    nf.write(content)
    nf.close()

    q.put(file_name)


def main():
    # 1. 获取想要复制的文件夹
    copy_file_name = input("输入要复制的文件夹名字：")

    # 2. 创建新的文件夹
    new_file_name = copy_file_name + "【附件】"
    try:
        os.mkdir(new_file_name)
    except:
        pass

    # 3. 获取文件夹中所有的文件名
    file_names = os.listdir(copy_file_name)

    # 创建队列
    q = multiprocessing.Manager().Queue()

    # 4. 创建进程池
    po = multiprocessing.Pool(3)
    for file_name in file_names:
        po.apply_async(copy_file, (copy_file_name, new_file_name, file_name, q))

    po.close()

    all_file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        # print("已经完成拷贝：%s" % file_name)
        copy_ok_num += 1
        print("\r拷贝进度：%.2f%%" % (copy_ok_num * 100 / all_file_num), end='')
        if copy_ok_num >= all_file_num:
            break


if __name__ == '__main__':
    main()
