# -*- coding: utf-8 -*-
#@Author：Susy.huang
#@time :2021/5/19 14:37


from pymongo import MongoClient
from common.logger import Logger

log = Logger("common function").getlog()


class Mongo():

    '''
    连接mongodb,初始化mongodb
    '''
    def __init__(self,host,port,database,conllection,username,password):
        self.client = MongoClient(f"mongodb://{host}:{port}/")
        self._database = self.client[database]
        self._database.authenticate(username,password)
        self._collection = self._database[conllection]

    def search_common(self,key,values):
        filter = {key:values}
        results = self._collection.find(filter)
        log.info(f"filter {filter}")
        return results

    def search_all(self,filter):
        results = self._collection.find(filter)
        log.info(f"filter")
        return results

    def clear_mong_common(self,collections):
        try:
            mydb = self._database
            mycol = mydb[collections]
            mycol.delete_many({})
        except Exception as error:
            print(error)

if __name__ == '__main__':
    pass


