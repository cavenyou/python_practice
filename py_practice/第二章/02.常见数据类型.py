#int
# float
# str(需要引号引起来)
# bool
# NoneType

#type(--),查看数据类型
# print(type("python"))
# print(type(13))
# print(type(1.3))
# print(type(True))
# print(type(None))

#isinstance（数据，类型）  判定数据是否是指定的类型 True/False
print(isinstance(4,int))
print(isinstance(4.1,int))
print(isinstance("ppp",str))
print(isinstance(4,bool))
print(isinstance(True,bool))

#字符串定义

s1 = "hello" #双引号定义
s2 = 'Python' #单引号定义

s3 = """
Hello
12312s
    """ #三引号定义（多行）
print("-------------------")
print(s1)
print(s2)
print(s3)

# 定义it's very good（含单引号）
msg = 'it\'s very good'
#转义字符   \' 定义单引号 \" 定义双引号 \n 换行 \t 制表符（缩进一个tab的大小）
print ("--------------------------------")
print(msg)

#字符串拼接 +号拼接字符串，只能是字符串，非字符串需要先转换为字符串
# 字面量可以直接写，变量需要用加号拼接
msg1 = "人生苦短"
msg2 = "我用Python"
print("..说：" + msg1 + "," + msg2)

# 案例
name = "zephyi"
age = 22
pro = "通信工程"
hobby = "Python"
print("\n大家好,我是" + name + ",今年" + str(age) + "岁,学习的专业是" + pro + ",爱好"+ hobby) #str(int数字)将其转换为字符串类型

#字符串格式化--------> 方式一: %s 占位符
print("\n大家好,我是%s"%name)
print("大家好,我是%s,今年%s岁"%(name,age)) #多项数据需要用括号括起来

#字符串格式化--------> 方式二: f"内容{变量/表达式}" ----------->推荐方式
print ("\n\n----------------------------------------")
print(f"大家好,我是{name},今年{age}岁")