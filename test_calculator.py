""""
homework-1
1.补全计算器（加减乘除）的测试用例
2.使用数据驱动完成测试用例的自动生成
3.在调用方法前打印【开始计算】，在调用测试方法之后打印【计算结束】
"""
import pytest

from pythoncode1.calculator import Calculator

list_add = [(2, 3, 5), (10000, 20000, 30000), (-2, -3, -5)]
list_s = [(5, 3, 2), (30000, 20000, 10000), (-5, -3, -2)]
list_m = [(5, 2, 10), (30000, 20000, 600000000), (-5, -3, 15)]
list_d = [(10, 2, 5), (600000000, 20000, 30000), (15, -3, -5), (3, 0, ValueError )]


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("\n======================================="
              "此处测试开始"
              "=========================================\n")
    def teardown_class(self):
        print("\n\n======================================="
              "测试结束"
              "=========================================")

    def setup_method(self):
        print("\n****用例开始")

    def teardown_method(self):
        print("\n***计算结束")

    @pytest.mark.parametrize("a, b, expect", list_add)
    def test_add(self, a, b, expect):
        # cal = Calculator()
        # print(len(list_add))
        assert expect == self.calc.add(a, b)

    @pytest.mark.parametrize("a, b, expect", list_s)
    def test_sub(self, a, b, expect):
        # cal = Calculator()
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a, b, expect", list_m)
    def test_mul(self, a, b, expect):
        # cal = Calculator()
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a, b, expect", list_d)
    def test_div(self, a, b, expect):
        # cal = Calculator()
        try:
            assert expect == self.calc.div(a, b)
        except Exception as e:
            print("\nDivider couldn't be ZERO!")
