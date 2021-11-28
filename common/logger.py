# -*- coding: utf-8 -*-
#@Author：Susy.huang
#@time :2020/12/16 10:43
import os.path
import logging
import time
from common.config import Config

class Logger():
    ''''''
    '''
    指定保存日志的文件路径，日志级别，调用文件
    将日志存入到指定的文件中
    '''
    def __init__(self,logger):
        #读取配置文件中的日志设置
        # import pdb;pdb.set_trace()
        cf = Config()
        self.log_dir = cf.get_value("log.conf","basiclog","log_dir") #log所在的位置
        self.format = cf.get_value("log.conf","basiclog","format") ##log格式
        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        cur_data = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
        package_path = os.path.abspath(".")
        print(package_path)
        file_path = os.path.join(package_path,self.log_dir)
        print(file_path)
        file_name  = cur_data + ".log"
        log_file = os.path.join(file_path,file_name)
        print(log_file)
        fh = logging.FileHandler(log_file) #将文件写到日志文件中
        fh.setLevel(logging.INFO) #设置日志的级别，默认是warning

        #再定义一个hendler，用于输出到控制台
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.INFO)

        #定义handler的输出格式
        formatter = logging.Formatter(self.format)
        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)

        #给handler 添加handler
        self.logger.addHandler(fh)
        # self.logger.addHandler(ch)

    '''所有用到logger的地方，只import这个封装库就行，然后直接调用'''
    def getlog(self):
        return self.logger


if __name__ == '__main__':
    log = Logger(logger="john").getlog()