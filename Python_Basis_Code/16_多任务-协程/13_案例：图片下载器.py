import urllib.request
import time
import gevent


# https://rpic.douyucdn.cn/live-cover/appCovers/2019/02/05/3659788_20190205232541_small.jpg
def downloader(name, url):
    req = urllib.request.urlopen(url)
    img_content = req.read()
    with open(name, 'wb') as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, '1.jpg',
                     'https://rpic.douyucdn.cn/live-cover/appCovers/2019/02/05/3659788_20190205232541_small.jpg'),
        gevent.spawn(downloader, '2.jpg', 'https://rpic.douyucdn.cn/asrpic/190215/6113690_5948059_36770_2_1542.jpg')
    ])


if __name__ == '__main__':
    main()
