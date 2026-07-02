#在使用模块中的功能时,必须先导入模块
"""
    导入整个模块:
    1. import 模块名
    调用方式: 模块名.功能名
    2. import 模块名 as 别名
    调用方式: 别名.功能名

    导入模块中具体的功能:
    1. from 模块名 import 功能名
    调用方式: 功能名
    2. from 模块名 import 功能名 as 别名
    调用方式: 别名
    3. from 模块名 import *
    调用方式: 功能名
"""

#导入模块
import random

for i in range(10):
    print(random.randint(1, 100),end='\t')#生成1到100的随机整数,包含1和100
print()

import random as r

for i in range(10):
    print(r.randint(1, 100),end=',')#生成1到100的随机整数,包含1和100
print()

#导入模块中的指定功能
from random import randint
for i in range(10):
    print(randint(1, 100),end=' ')#生成1到100的随机整数,包含1和100
print()

from random import randint as rint
for i in range(10):
    print(rint(1, 100),end='-')#生成1到100的随机整数,包含1和100
print()


"""
    自定义模块:
    每一个python文件都可以作为一个模块,模块的名字就是文件的名字
"""