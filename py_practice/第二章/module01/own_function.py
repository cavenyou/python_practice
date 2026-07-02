#常量: 定义为不会再修改的值
#__all__ = ["pai","name",....]: 用于指定from 模块名 import * 时会导入哪些功能(只影响*的通配)
pai = 3.1415926
NAME = "Lzzepy"

def long_seperator1():
    print("-" * 50) # 表示前面的输出输出50次

def long_seperator2():
    print("+" * 50)

def long_seperator3():
    print("#" * 50)

def long_seperator4():
    print("*" * 50)

#测试函数调用
# long_seperator1()
# long_seperator2()
# long_seperator3()
# long_seperator4()

#__name__: python中内置变量,表示当前模块的名字(直接运行该模块,__name__的值为"__main__";当该模块被导入时,__name__的值就是模块的名称)
if __name__ == "__main__": #表明直接运行该文件,则运行下面语句,如果作为模块,则不运行
    long_seperator1()
    long_seperator2()
    long_seperator3()
    long_seperator4()
else :
    print(__name__)


"""
    main:  与if __name__ == "_main__"一致,是简化语句
"""