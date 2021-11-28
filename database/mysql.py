# -*- coding: utf-8 -*-
#@Author：Susy.huang
#@time :2021/4/28 17:32

import pymysql
import allure

from common.common import Common


class try_mysql():

    def __init__(self,host=None,user=None,passwd=None, db=None, port=3320):
        self.conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=port)
        self.db = db

    def clear_database_table(self,tables):
        self.cur = self.conn.cursor()
        self.conn.ping(reconnect=True)
        sql_common = "TRUNCATE TABLE{0}.{1};"
        allure.attach(f"sql_common {sql_common} ")
        for table in tables:  #将字符串转化为list，遍历和删除表
            self.cur.execute(sql_common.format(self.db,table))
        self.conn.commit()
        self.conn.close()

    def common_query_data(self,sql):
        try:
            self.cur = self.conn.cursor()
            self.conn.ping(reconnect=True)
            self.cur.execute(sql)
            allure.attach(f"sql {sql} ")
            result  = self.cur.fetchall()
            self.cur.close()
            self.conn.close()
        except Exception as error:
            print(error)
        allure.attach(f"result {result} ")

        return result


if __name__ == '__main__':
    pass