# -*- coding: utf-8 -*-
#@time :2021-10-31 11:45
#@Author：sky
import allure
import pytest
from  util.address_book_api import Address_Book
from common.read_yaml import Read_Yaml
from database.mysql import try_mysql
from common.config import Config


#初始化api
@pytest.fixture(scope='module')
def origin_api():
    api = Address_Book()
    return api

#获取access token
@pytest.fixture(scope='module')
def get_access_token(origin_api):
    data = Read_Yaml().yaml_parse('address_book','create_persionel.yaml','common')[0]
    corpid = data['corpid']
    corpsecret = data['corpsecret']

    code, errmsg, access_token, expires_in=origin_api.get_access_token_ab(corpid=corpid,corpsecret=corpsecret)
    return access_token

#环境清理
@pytest.fixture(scope='function')
def clear_mysql():
    #host=None,user=None,passwd=None, db=None, port=3320
    host = Config().get_value('envi.conf',"sit","host")
    user = Config().get_value('envi.conf',"sql","user")
    passwd = Config().get_value('envi.conf',"sql","password")
    db =  Config().get_value('envi.conf',"sql","db")
    port = Config().get_value('envi.conf',"sql","port")
    table = Config().get_value('envi.conf',"sql","table")

    try_mysql(host,user,passwd,db,port).clear_database_table(table)


#数据转发函数
@pytest.fixture(scope='function',autouse=True)
def origin_data(request):
    data = request.param
    return data

@allure.feature('新增成员')
class Test_Create_Persionel():

    @allure.title('正常场景_全量参数正确')
    @pytest.mark.parametrize('origin_data',Read_Yaml().yaml_parse('address_book','create_persionel.yaml','test_case01'),indirect=True)
    def test_case01(self,origin_api,origin_data,get_access_token):
        access_token = get_access_token
        code, message = origin_api.create_persionel_ab(access_token,origin_data['userid'],origin_data['name'],origin_data['mobile'],origin_data['email'],origin_data['department'])
        assert code == 0
        assert message == 'created'
        allure.attach(f"code->{code} message->{message}")