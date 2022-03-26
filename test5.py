"""
 * Project name(项目名称)：Python局部函数
 * Package(包名): 
 * File(文件名): test5
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 13:34
 * Version(版本): 1.0
 * Description(描述)： 
 """


# 全局函数
def f1():
    name = "所在函数中定义的 name 变量"
    a = 1

    # 局部函数
    def f2():
        """
        nonlocal语句导致列出的标识符引用最近的封闭范围内的先前绑定的变量，不包括全局变量。这很重要，
        因为绑定的默认行为是首先搜索本地命名空间。该语句允许封装代码重新绑定全局（模块）范围之外的局部范围之外的变量。
        与global语句中列出的名称不同，在nonlocal语句中列出的名称必须引用封闭范围中的预先存在的绑定（无法明确确定应创建新绑定的范围）。
        非本地语句中列出的名称不得与本地范围内的预先存在的绑定发生冲突。
        :return:
        """
        nonlocal name
        print(name)
        print(a)
        name = "局部函数中定义的 name 变量"

    f2()


if __name__ == '__main__':
    f1()
