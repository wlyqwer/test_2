# -*- coding: utf-8 -*-
#@time :2021-10-31 10:58
#@Author：sky
import json
import requests
from common.logger import Logger

log = Logger('Address Book api').getlog()

class Address_Book():
    def get_access_token_ab(self,corpid=None,corpsecret=None,corpid_flag=1,corpsecret_flag=1):
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'

        if corpid_flag and corpsecret_flag:
            url = f'{base_url}?corpid={corpid}&corpsecret={corpsecret}'
        elif corpid_flag:
            url = f'{base_url}?corpid={corpid}'
        elif corpsecret_flag:
            url = f'{base_url}?corpsecret={corpsecret}'
        else:
            url = base_url

        log.info(f'url->{url}')
        try:
            res = requests.get(url=url)

            content  = json.loads(res.text)
            log.info(f"content->{content}")

            code = content['errcode']
            errmsg =  content['errmsg']

            access_token = ''
            expires_in = ''

            if code == 0:
                access_token = content['access_token']
                expires_in = content['expires_in']
        except Exception as error:
            log.error(f'error->{error}')

        return code,errmsg,access_token,expires_in

    def create_persionel_ab(self,access_token,userid,name,mobile,email,department,
                            access_token_flag=1,userid_flag=1,name_flag=1,mobile_flag=1,
                            email_flag=1,department_flag=1):
        if access_token_flag:
            url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}'
        else:
            url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"

        data = {}
        if userid_flag:
            data['userid'] = userid
        if name_flag:
            data['name'] = name
        if mobile_flag:
            data['mobile'] = mobile
        if email_flag:
            data['email'] = email
        if department_flag:
            data['department'] = department

        log.info(f"传入的参数值为data->{data}")
        try:
            res = requests.post(url,json.dumps(data))
            content = json.loads(res.text)
            code = content["errcode"]
            message = content["errmsg"]
            log.info(f"content->{content}")
        except Exception as error:
            log.error(f"error->{error}")

        return code,message

    #查询成员
    def search_persionel_ab(self,access_token=None,userid=None,access_token_flag=1,userid_flag=1):
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'

        if access_token_flag and userid_flag:
            url = f'{base_url}?access_token={access_token}&userid={userid}'
        elif access_token_flag:
            url = f'{base_url}?access_token={access_token}'
        elif userid_flag:
            url = f'{base_url}?userid={userid}'
        else:
            url = base_url

        log.info(f'url->{url}')
        try:
            res = requests.get(url=url)

            content  = json.loads(res.text)
            log.info(f"content->{content}")

        except Exception as error:
            log.error(f'error->{error}')

        return content

    #更新成员
    def put_persionel_ab(self,access_token,userid,**kwargs):

        if "access_token_flag" in kwargs.keys():
            url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={access_token}'
        else:
            url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"

        data = {}

        if "userid_flag" in  kwargs.keys():
            data['userid'] = userid

        if "name"in  kwargs.keys() :
            data['name'] = kwargs['name']

        log.info(f"传入的参数值为data->{data}")

        try:
            res = requests.post(url,json.dumps(data))
            content = json.loads(res.text)
            code = content["errcode"]
            message = content["errmsg"]
            log.info(f"content->{content}")

        except Exception as error:
            log.error(f"error->{error}")

        return code,message

    #删除成员
    def delete_persionel_ab(self,access_token=None,userid=None,access_token_flag=1,userid_flag=1):
        base_url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'

        if access_token_flag and userid_flag:
            url = f'{base_url}?access_token={access_token}&userid={userid}'
        elif access_token_flag:
            url = f'{base_url}?access_token={access_token}'
        elif userid_flag:
            url = f'{base_url}?userid={userid}'
        else:
            url = base_url

        log.info(f'url->{url}')
        try:
            res = requests.get(url=url)

            content  = json.loads(res.text)
            log.info(f"content->{content}")

        except Exception as error:
            log.error(f'error->{error}')

        return content['errcode'],content['errmsg']



if __name__ == '__main__':
    ab = Address_Book()
    data = ab.get_access_token_ab('ww386957bad20fab64',corpsecret_flag=0)
    print(data)
    print(type(data))
    print(data['access_token'])
