import pytest

@pytest.fixture(scope = "function")
def conn_database():
    print("链接数据库")
    yield
    print("关闭数据库")
