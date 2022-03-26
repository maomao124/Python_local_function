"""
 * Project name(项目名称)：Python局部函数
 * Package(包名): 
 * File(文件名): test6
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 13:57
 * Version(版本): 1.0
 * Description(描述)： Python 允许直接将函数赋值给其它变量，这样做的效果是，程序中也可以用其他变量来调用该函数
 """


def f1():
    """

    :return:
    """
    print("hello")
    return 123


def add(a, b):
    """
    add
    :param a:
    :param b:
    :return:
    """
    return a + b


def multi(a, b):
    """
    乘
    :param a:
    :param b:
    :return:
    """
    return a * b


def my_def(a, b, dis):
    return dis(a, b)


if __name__ == '__main__':
    f = f1()
    print(f)

    # 求 2 个数的和
    print(my_def(3, 4, add))
    # 求 2 个数的乘积
    print(my_def(3, 4, multi))
