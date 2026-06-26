"""
    字符串操作常见方法:
    find():         在字符串中查找子串,返回第一次出现的索引位置,找不到返回-1  s.find('sd')
    count():        统计子串在字符串中出现的次数      s.count('a')
    upper():        将字符串中所有字母转为大写       s.upper()
    lower():        将字符串中所有字母专为小写       s.lower()
    split():        将字符串按指定分隔符分割成列表         s.split(' ')
    strip():        去除字符串两端的空白字符或指定字符       s.strip()/s.strip('*')
    replace():      将字符串中的指定子串替换为新的子串       s.replace('H','C'): 将H换为C
    startswish():   检查字符串是否是指定子串开头,返回布尔值    s.startswith('H')
"""

string = 'Hello-young,Hello-python'

#find()
index = string.find('-') #int类型
print(index)
print()

#count
num = string.count('o') #int类型
print(num)
print()

#upper()
print(string.upper())
print()

#lower
print(string.lower())
print()

#split()
print(string.split(','))
print()

#strip()
print(string.strip('n'))
print()

#replace()
print(string.replace(',',' '))
print()

#startswish()
print(string.startswith('H'))
print()
print(string.startswith('h'))