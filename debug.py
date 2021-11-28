# -*- coding: utf-8 -*-
#@time :2021-10-31 10:15
#@Author：sky

from common.common import Common

from common.config import Config
from common.read_yaml import Read_Yaml
# ry = Read_Yaml().yaml_parse('address_book','create_persionel.yaml','common')
# print(ry)
# print(type(ry))
# print(ry[0])
# print(type(ry[0]))
# print(ry[0]['corpid'])
#
# data = [{"a":1,"b":2},{"a":3,"b":4}]
# for  i in data:
#     print(i["a"])

from util.address_book_api import Address_Book

ab = Address_Book()
data = ab.search_persionel_ab("-FqwyS6FMS4eEfwLdEHkooWtHXqRu20q0ecsaKHEjgCPAFFQJNm6rFqefQPC7uZ3p62_2cAth3jDEwJOS1NqUWZNGjgJSaWlP-4brQ1AMWTQuxX-3IFrAocV--yOK1o1L2tJd0Jqi9O9su3KaEVFWJLfT8HQuYH3aGhX6_xVpfFTQn4CPsFLCRwnHZKGD3GyVa8enGoNhUEC7_i1M4rdNQ","xungeng_test01")
print(data)
