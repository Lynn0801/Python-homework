import pytest

# @pytest.fixture(autouse = "true") 每个用例都会调用
@pytest.fixture(scope="module")
def pretest():
    print("\n***env is ok, start test now!***")
@pytest.fixture(scope="module")
def aftertest():
    print("\n***It is the last function test***")

mydata = ["param1", "param2"]
@pytest.fixture(params=mydata)
def myfixture2(request):
    # print("%s" % request.param)
    # return request.param
    yield request.param # yield 类似return
    print("\n下面执行下一个目标操作")

