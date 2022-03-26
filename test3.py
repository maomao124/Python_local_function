"""
 * Project name(项目名称)：Python局部函数
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 13:29
 * Version(版本): 1.0
 * Description(描述)： 
 """


# 全局函数
def f1():
    # 局部函数
    def f2():
        print("hello")

    return f2()


if __name__ == '__main__':
    f1()
