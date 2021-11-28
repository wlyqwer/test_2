# -*- coding: utf-8 -*-
#@Author：Susy.huang
#@time :2021/4/25 15:03
import os
import yaml


class Read_Yaml():
    def yaml_parse(self,folder,filename,section):
        rootdir = os.path.abspath(".")
        folder_dir = os.path.join(rootdir,"data")
        service_dir = os.path.join(folder_dir,folder)
        configPath = os.path.join(service_dir, filename)
        path = os.path.abspath(configPath)
        fr = open(path, "r", encoding="utf-8")
        content = yaml.load(fr, Loader=yaml.FullLoader)
        return content[section]



if __name__ == '__main__':
    RM = Read_Yaml().yaml_parse('address_book','search_persionel.yaml','test_case01')[0]['userid']
    print(RM)

