"""
 * Project name(项目名称)：Python局部函数
 * Package(包名): 
 * File(文件名): test4
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 13:32
 * Version(版本): 1.0
 * Description(描述)： 如果局部函数中定义有和所在函数中变量同名的变量，也会发生“遮蔽”的问题
 """


# 全局函数
def f1():
    name = "所在函数中定义的 name 变量"
    a = 1

    # 局部函数
    def f2():
        print(name)
        print(a)
        name = "局部函数中定义的 name 变量"

    f2()


if __name__ == '__main__':
    f1()
