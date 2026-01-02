import os

if __name__ == '__main__':
    # 生成数据源（执行测试并生成 Allure 原始数据）
    os.system('pytest --alluredir=./temp --clean-alluredir')

    # 生成 Allure 测试报告
    os.system('allure generate ./temp -o reports --clean')

    os.system('allure open reports')
