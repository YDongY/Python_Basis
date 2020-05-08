import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="./log.txt",  # 当前路径log.txt
                    filemode="a", # a的方式写入
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# 开始使用log功能
logging.debug('这是 loggging debug message')  # 级别最低
logging.info('这是 loggging info message')
logging.warning('这是 loggging a warning message')
logging.error('这是 an loggging error message')
logging.critical('这是 loggging critical message')