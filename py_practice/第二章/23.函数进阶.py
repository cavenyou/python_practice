"""
    函数-变量作用域: 变量的作用域指的是变量的作用范围(标识这个变量在哪可以使用,在哪儿不可以使用)
    全局变量: 函数之外的变量,在整个文件中都可以使用,一般定义在函数顶部
    局部变量: 在函数内部定义的变量,只能在该函数内部使用,外部无法访问(函数执行完毕后会自动销毁其内部局部变量)
"""
#pass

#global关键字: 告诉解释器要在函数中用到全局变量,使得可以在函数内部修改全局变量的值
num = 100
def hanshu1():
    num = 10000 #只是创建了一个局部变量
    print(num)
hanshu1()
print(num)

num = 100
def hanshu2():
    global num
    num = 10000 #修改了全局变量
    print(num)
hanshu2()
print(num)

#传参方式

# 定义函数
def reg_stu1(name, age, gender, city):
    print(f"注册成功, 姓名:{name}, 年龄:{age}, 性别:{gender}, 城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 调用函数
#位置传参: 调用函数时根据函数的定义的位置来传递参数----->简洁

stu1 = reg_stu1("张三", 18, "男", "北京")
print(stu1)

#关键字传参: 调用函数时以函数定义的形参名称作为关键字,以键=值的形式来传递参数(不要求顺序)---->可读性强
stu2 = reg_stu1(gender="男", city="北京",name="张三", age = 18)   #不要求顺序
print(stu2)

#位置加关键字传参---------->位置参数在前,关键字参数值在后
stu3 = reg_stu1("张三", 18, city="北京",gender="男")
print(stu3)


#默认参数: 在定义函数时,为参数提供默认值,调用函数时可以不传递有默认值的参数,在函数调用时为默认参数传递了新的值,那么就会覆盖默认值
def reg_stu2(name, age, gender, city="北京"):   #设置默认值的参数放在后面
    print(f"注册成功, 姓名:{name}, 年龄:{age}, 性别:{gender}, 城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}
#不传递默认参数
stu4 = reg_stu2("张三", 18, "男")
print(stu4)

#修改默认参数
stu5 = reg_stu2("张三", 18, "男","修改")
print(stu5)


"""
    不定长参数: 也称可变参数,用于函数定义参数个数不确定(0个或一个)的场景
"""
# 位置传递
#需求: 根据输出的一组数据,计算其最大值,最小值和平均值
def calc_data1(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data, max_data, round(avg_data,1)
min_data, max_data, avg_data = calc_data1(12889,1231,423,3242,131,132123,123) #传递的所有参数会被args变量收集,合并为一个元组
print(min_data, max_data, avg_data)

#关键字传递(**kwargs-->字典)
def calc_data2(*args,**kwargs):   #*args用来存储数据,**kwargs用来存储选项(定制函数的行为)
    """
    根据输出的一组数据,计算其最大值,最小值和平均值,并且通过输入的实参判断是否进行输出,输出几位小数
    :param args:不定长未知参数,需要计算的数据
    :param kwargs: 不定长关键字参数
        round:保留的小数
        print:是否进行输出打印
    :return:最小值,最大值,平均值
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get("round") != None:
        avg_data = round(avg_data,kwargs.get("round"))
    if kwargs.get("print"):
        print( min_data, max_data, avg_data)

    return min_data, max_data, avg_data
#调用函数
calc_data2(123,1231,234,4533,12312,12839,1,round=4,print=True)

"""
    函数的参数类型
    普通参数: 数字,布尔,字符串,列表,元组,集合,字典
    特殊参数: 函数
"""
#加
def add(x,y):
    return x + y

#减
def sub(x,y):
    return x - y

#乘
def mul(x,y):
    return x * y

#除
def div(x,y):
    return x / y

def calc(x,y,operator):
    return operator(x,y)

print(calc(10,100,sub))


"""
    匿名函数: 通过lambda表达式来声明函数:
        lambda 参数列表:函数体
"""
# 定义命名函数

def out_line1():
    print('-------------')

def add1(x, y):
    return x + y

out_line1()
print(add1(10, 20))

# 定义匿名函数   函数逻辑比较简单,可以用匿名函数来简化,通常作为高阶函数的参数使用

#lambda 参数列表 : 函数体

out_line2 = lambda : print('----------------')

add2 = lambda x, y: x + y

out_line2()
print(add2(100, 200))


#案例: 按照每一个元素的字符个数,从小到大排序
data_list = ["C++","C","Python","Jack","PHP","Java","Go","JavaScript","Rust"]
def sort(d_list):
    d_list.sort(key=lambda item:len(item),reverse=False)
    print(d_list)
sort(data_list)