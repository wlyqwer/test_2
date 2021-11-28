# -*- coding: utf-8 -*-
#@Author：Susy.huang
#@time :2021/3/10 11:19
import base64
import os
import random

import allure

from common.logger import Logger
log = Logger("common function").getlog()


class Common():

    #遍历某个目录下的所有文件
    def ergodic_dir_file(self,file_path):
        file_list = []
        all_file = os.listdir(file_path)
        for file in all_file:
            file_list.append(f'{file_path}/{file}')
        return file_list

    #生成base64
    def  get_base64(self,image_path):
        with open(f"{image_path}", 'rb') as f:
            image = f.read()
            image_base64 = str(base64.b64encode(image), encoding='utf-8')
        return image_base64

    #两次base64加密
    def  get_base64_mixture_base32(self,image_path):
        basecode={
            '32': lambda x: base64.b32encode(x),
            '64': lambda x: base64.b64encode(x)
            }
        data=image_path.encode('utf-8')
        for i in range(10):
            order=random.choice(['32','64'])
            data=basecode[order](data)
        data=data.decode('utf-8')
        return data

    def read_file(self,filename):
        with open(filename,encoding="utf-8") as file:
            contents = file.read()
            file.close()
        return contents

    def common_for_qurrey(self,data):
        common_list = []

        for result in data:
            if result[0] not in common_list:
                common_list.append(result[0])
        allure.attach(f"common_list {common_list} ")
        return common_list

if __name__ == '__main__':
    common = Common()
    common.ergodic_dir_file('./common')
