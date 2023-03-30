import pytest

from common.yaml_util import YamlUtil


@pytest.fixture(scope="function")
def conn_database():
    print("链接数据库")
    yield
    print("关闭数据库")


@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_yaml()
    print("清除成功")
