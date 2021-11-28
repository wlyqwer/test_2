# -*- coding: utf-8 -*-
#@Author：Susy.huang
#@time :2021/3/12 14:18
import os


if __name__ == '__main__':
    # os.system(r'pytest  -s  -v ./testcase/address_book/test_delete_persionel.py::Test_Delete_Persionel   --alluredir  ./reports/xml --clean-alluredir -o log_cli=true -o log_cli_level=INFO')
    os.system('pytest  -s  --tb=no   ./testcase/address_book/test_delete_persionel.py::Test_Delete_Persionel   --alluredir  ./allure-results --clean-alluredir -o log_cli=true -o log_cli_level=INFO')
    # os.system('pytest  -s  -v       ./testcase/address_book/test_delete_persionel.py::Test_Delete_Persionel     --alluredir  ./allure-results --clean-alluredir -o log_cli=true -o log_cli_level=INFO')
    # os.system('pytest  -s --tb   --alluredir  ./allure-results --clean-alluredir -o log_cli=true -o log_cli_level=INFO')
    # # # pytest.main(['-s', '-q', '--alluredir', './reports/xml', '--clean-alluredir'])
    # os.system(r'allure  generate ./reports/xml -o ./reports/html --clean')
    # print(os.path.abspath("."))

    #E:\02.code\api\interface_frame_start\testcase\address_book\test_delete_persionel.py
    #E:\02.code\api\interface_frame_start\testcase\address_book\test_delete_persionel.py::Test_Delete_Persionel