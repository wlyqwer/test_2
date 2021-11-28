# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml


def yaml_parse(folder,filename):
    rootdir =  os.path.abspath(".")
    folder_dir = os.path.join(rootdir,"data")
    service_dir = os.path.join(folder_dir,folder)
    configPath = os.path.join(service_dir, filename)
    path = os.path.abspath(configPath)
    fr = open(path, "r", encoding="utf-8")
    content = yaml.load(fr, Loader=yaml.FullLoader)
    return content


def get_params(folder,filename: object, modlue: object, keyname: object) -> object:
    """
    读取解析后的yaml中的数据
    :param filename: 待读取数据所在文件的文件名
    :param modlue: yaml文件中的模块名
    :param keyname: 键值名
    :return:
    """

    content = yaml_parse(folder,filename)
    params = content[modlue][keyname]
    # print(params)
    # for param in params:
    #     print(type(param))
    return params


if __name__ == "__main__":
    y = yaml_parse("Match_Image","delete_index.yaml")["normal"][0]["image"]
    print(type(y))
    print(y)
    # print(get_params("Match_Image","create_index.yaml"))
