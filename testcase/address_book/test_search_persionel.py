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
    data = Read_Yaml().yaml_parse('address_book','search_persionel.yaml','common')[0]
    corpid = data['corpid']
    corpsecret = data['corpsecret']

    code, errmsg, access_token, expires_in=origin_api.get_access_token_ab(corpid=corpid,corpsecret=corpsecret)
    return access_token

#新增成员
@pytest.fixture(scope='module')
def create_persionel(origin_api,get_access_token):
    data = Read_Yaml().yaml_parse('address_book','search_persionel.yaml','test_case01')[0]
    access_token = get_access_token

    code, message=origin_api.create_persionel_ab(access_token=access_token,userid=data['userid'],name=data['name'],mobile=data['mobile'],email=data['email'],department=data['department'])
    assert code == 0

    return data['userid']


#数据转发函数
@pytest.fixture(scope='function',autouse=True)
def origin_data(request):
    data = request.param
    return data

@allure.feature('查询成员')
class Test_Search_Persionel():

    @allure.title('正常场景_全量参数正确')
    @pytest.mark.parametrize('origin_data',Read_Yaml().yaml_parse('address_book','search_persionel.yaml','test_case01'),indirect=True)
    def test_case01(self,origin_api,origin_data,get_access_token,create_persionel):
        access_token = get_access_token
        userid = create_persionel

        with allure.step('step1:查询成员'):
            data =  origin_api.search_persionel_ab(access_token,userid,1,1)
            assert data['errcode']  == 0
            assert data['errmsg'] == 'ok'
            assert data['userid'] == origin_data['userid']

            allure.attach(f"data->{data}")
