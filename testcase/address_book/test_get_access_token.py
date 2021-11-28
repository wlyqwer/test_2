# -*- coding: utf-8 -*-
#@time :2021-10-31 11:45
#@Author：sky
import allure
import pytest
from  util.address_book_api import Address_Book
from common.read_yaml import Read_Yaml


#初始化api
@pytest.fixture(scope='module')
def origin_api():
    api = Address_Book()
    return api

#数据转发函数
@pytest.fixture(scope='function',autouse=True)
def origin_data(request):
    data = request.param
    return data

@allure.feature('获取Access_Token')
class Test_Get_Access_Token():

    @allure.title('正常场景_corpid/corpscret均传入正确的string')
    @pytest.mark.parametrize('origin_data',Read_Yaml().yaml_parse('address_book','get_access_token.yaml','test_case01'),indirect=True)
    def test_case01(self,origin_api,origin_data):
        code, errmsg, access_token, expires_in = origin_api.get_access_token_ab(corpid=origin_data['corpid'],corpsecret=origin_data['corpsecret'])
        assert code == 0
        assert errmsg == 'ok'
        assert access_token != ''
        allure.attach(f"code->{code} errmsg->{errmsg} access_token->{access_token} expires_in->{expires_in}")

    @allure.title('异常场景_必需参数缺失_corpid缺失')
    @pytest.mark.parametrize('origin_data',Read_Yaml().yaml_parse('address_book','get_access_token.yaml','test_case02'),indirect=True)
    def test_case02(self,origin_api,origin_data):
        code, errmsg, access_token, expires_in = origin_api.get_access_token_ab(corpsecret=origin_data['corpsecret'],corpid_flag=origin_data["corpid_flag"])
        assert code == 41002
        assert errmsg == 'corpid missing'
        allure.attach(f"code->{code} errmsg->{errmsg} access_token->{access_token} expires_in->{expires_in}")

