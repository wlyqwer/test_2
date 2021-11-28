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
    data = Read_Yaml().yaml_parse('address_book','put_persionel.yaml','common')[0]
    corpid = data['corpid']
    corpsecret = data['corpsecret']

    code, errmsg, access_token, expires_in=origin_api.get_access_token_ab(corpid=corpid,corpsecret=corpsecret)
    allure.attach(f"code->{code} errmsg->{errmsg} access_token->{access_token} expires_in->{expires_in}")
    return access_token

# @pytest.fixture(scope='module')
# def delete_persionel(origin_api,get_access_token):
#     data = Read_Yaml().yaml_parse('address_book','put_persionel.yaml','common')[0]
#     access_token = get_access_token
#
#     code, message=origin_api.delete_persionel_ab(access_token,data['userid'])
#     assert code == 0
#     allure.attach(f"code->{code} message->{message}")
#     return data['userid']

#新增成员
@pytest.fixture(scope='module')
def create_persionel(origin_api,get_access_token):
    data = Read_Yaml().yaml_parse('address_book','put_persionel.yaml','common')[0]
    access_token = get_access_token

    code, message=origin_api.create_persionel_ab(access_token=access_token,userid=data['userid'],name=data['name'],mobile=data['mobile'],email=data['email'],department=data['department'])
    assert code == 0
    allure.attach(f"code->{code} message->{message}")
    return data['userid']


#数据转发函数
@pytest.fixture(scope='function',autouse=True)
def origin_data(request):
    data = request.param
    return data

@allure.feature('更新成员')
class Test_Put_Persionel():

    @allure.title('正常场景_更新name值')
    @pytest.mark.parametrize('origin_data',Read_Yaml().yaml_parse('address_book','put_persionel.yaml','test_case01'),indirect=True)
    def test_case01(self,origin_api,origin_data,get_access_token,create_persionel):
        access_token = get_access_token
        userid = create_persionel

        with allure.step('step1:更新成员'):
            code, message =  origin_api.put_persionel_ab(access_token,userid,access_token_flag=origin_data['access_token_flag'],userid_flag=origin_data['userid_flag'],name=origin_data['name'])
            assert code  == 0
            assert message == 'updated'

            allure.attach(f"code->{code} message->{message}")
