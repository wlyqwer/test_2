# -*- coding: utf-8 -*-
#@Author：Susy.huang
#@time :2020/12/16 10:46

import os
import configparser

class Config():
    def __init__(self):
        self.config_folder = "config"

    '''将文件路径加入到环境变量中'''
    @staticmethod
    def get_file_path(folder_name,file_name,childer_folder=None):
        config_path =  os.path.abspath(".")
        print(f'config_path->{config_path}') #工程路径
        file_path = os.path.join(config_path,folder_name) #工程路径+目录路径
        print(f'file_path->{file_path}')
        final_path = os.path.join(file_path,file_name)  #工程路径+目录路径+文件路径
        print(f'final_path->{final_path}')
        if childer_folder:
            final_path = os.path.join(final_path,childer_folder)
        return final_path

    '''读取配置文件名称'''
    def get_config_file(self,file_name):
        try:
            config = configparser.ConfigParser()
            file_path = self.get_file_path("config",file_name)
            config.read(file_path,encoding="utf-8-sig")
            return config
        except Exception as error:
            print("read config file error" + str(error))

    '''读取测试数据文件名称'''
    def get_data_file(self, service_name,file_name,child_file=0):
        try:
            file_path = None
            parent_path = self.get_file_path("data", "file",service_name)
            if file_name:
                file_path = os.path.join(parent_path,file_name)
            if child_file:
                file_path = os.path.join(file_path,child_file)
            return file_path
        except Exception as error:
            print("read filepath error" + str(error))

    '''读取配置文件中指定section和key的值'''
    def get_value(self,file_name,section,key):
        try:
            config = self.get_config_file(file_name)
            value  = config.get(section,key)
            return value
        except Exception as error:
            print("get value failed:"+str(error))

    '''在配置文件中写入数据'''
    def set_value(self,file_name,section,key,value):
        try:
            config = self.get_config_file(file_name)
            config.set(section,key,value)
            config.write(open(self.get_file_path("config",file_name),"w+"))
        except Exception as error:
            print("set value failed:" + str(error))

    '''在配置文件中更新指定section、key的值'''
    def update_value(self, file_name, section, key, value):
        try:
            config = self.get_config_file(file_name)
            config.set(section, key, value)
            config.write(open(self.get_file_path("config", file_name), "w+"))
        except Exception as error:
            print("set value failed:" + str(error))

    '''移除配置文件中指定section'''
    def remove_section(self,file_name,section):
        try:
            config = self.get_config_file(file_name)
            config.remove_section(section)
            config.write(open(self.get_file_path("config",file_name),"w+"))
        except Exception as error:
            print("remove section error" + str(error))


    '''移除配置文件中指定key的值'''
    def remove_option(self,filename,section,key):
        try:
            config = self.get_config_file(filename)
            config.remove_option(section,key)
            config.write(open(self.get_file_path("config",filename),"w+"))
        except Exception as error:
            print("remove section error" + str(error))



if __name__ == '__main__':
    CF = Config()
    print(CF.get_file_path('config','envi.conf'))

#E:\勋更文档\20210702\文件\代码\interface_frame_start\config\envi.conf
#E:\勋更文档\20210702\文件\代码\interface_frame_start\config\envi.conf
#E:\勋更文档\20210702\文件\代码\interface_frame_start\config\envi.conf
#E:\勋更文档\20210702\文件\代码\interface_frame_start\common\config\envi.conf