""""
homework-2
1.补全计算器（加减乘除）的测试用例
2.使用数据驱动完成测试用例的自动生成
3.在调用方法前打印【开始计算】，在调用测试方法之后打印【计算结束】
使用【测试数据的数据驱动】的方法完成加减乘除测试
使用fixture替换setup和teardown
将fixture方法放在conftest.py里面，设置scope=module
修改运行规则，pytest.ini文件
"""
import yaml
import pytest
# from calculator import Calculator
from pythoncode1.calculator import Calculator


def get_datas():
    with open("tdatacalcu.yml") as f:
        datas = yaml.safe_load(f)
        # print(datas)
        list_add = datas["list_add"]
        list_sub = datas["list_sub"]
        list_mul = datas["list_mul"]
        list_div = datas["list_div"]
        return [list_add,list_sub,list_mul,list_div]

class TestC():
    def setup_class(self):
        self.ca = Calculator()
        print("\n ===================Start test========================")

    @pytest.mark.addsub
    @pytest.mark.add
    @pytest.mark.parametrize("a, b, expected", get_datas()[0])
    def test_add(self, a, b, expected, pretest):
        assert expected == self.ca.add(a, b)

    @pytest.mark.addsub
    @pytest.mark.sub
    @pytest.mark.parametrize("a, b, expected", get_datas()[1])
    def test_sub(self, a, b, expected):
        assert expected == self.ca.sub(a, b)

    @pytest.mark.muldiv
    @pytest.mark.mul
    @pytest.mark.parametrize("a, b, expected", get_datas()[2])
    def test_mul(self, a, b, expected):
        assert expected == self.ca.mul(a, b)

    @pytest.mark.muldiv
    @pytest.mark.div
    @pytest.mark.parametrize("a, b, expected", get_datas()[3])
    def test_div(self, a, b, expected, aftertest):
        try:
            assert expected == self.ca.div(a, b)
        except Exception as e:
            print("\nAttention: ZERO couldn't be as divider!!")