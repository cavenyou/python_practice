"""
    字典: 通过字/词语,找到对应的解释
    每个字/词语对应一个解释,字/词语不能重复
    定义: dict1 = {key: value, key: value,......}  key不能重复,如果重复了,后面的值会覆盖前面的值 key必须是不可变类型(str.int,float,tuple)
    空字典: dict = {]
"""
"""

    常用操作:
    类型    操作                        含义                                    样例
    添加    字典名称[key] = value       往指定字典中添加key-value键值对           dict1["A"] = 688
    删除    字典名称.pop(key)           删除字典中指定的key，并返回该key对应的value  score = dict1.pop("A")
    删除    del 字典名称[key]           删除字典中指定的键值对                     del dict1["A"]
    修改    字典名称[key] = value       修改字典中指定的key对应的值               dict1["A"] = 658
    查询    字典名称[key]               根据key获取value                          dict1["A"]
    查询    字典名称.get(key)           根据key获取value                          dict1.get("A")
    查询    字典名称.keys()             获取所有的key                             dict1.keys()
    查询    字典名称.values()           获取所有的value                           dict1.values()
    查询    字典名称.items()            获取所有的key-value键值对                 dict1.items()

"""

#定义字典
week_dict = {
    "周一": "Monday",
    "周二": "Tuesday",
    "周三": "Wednesday",
    "周四": "Thursday",
    "周五": "Friday",
    "周六": "Saturday",
    "周日": "Sunday"
}

print(week_dict)
print(type(week_dict))

print(week_dict["周三"]) #获取
week_dict["周三"] = "wednesday"
print(week_dict["周三"])

#遍历
for key, value in week_dict.items():
    print(f"{key}: {value}")

for key in week_dict.keys():
    print(f"{key}: {week_dict[key]}")

for item in week_dict.items():
    print(f"{item[0]}: {item[1]}")