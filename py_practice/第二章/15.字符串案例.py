"""
    案例:
    邮箱格式验证: 用户输入一个邮箱,验证邮箱格式是否正确(包含一个@和至少一个.),如果输入正确,输出"邮箱格式正确",否则输出"邮箱格式错误"
"""

#接收用户输入的邮箱
print("邮箱格式验证:O.o")
email = input("请输入要进行格式验证的邮箱: ")

#检测@和'.'的数量
num_at = email.count('@')
num_dot = email.count('.')

#判断格式是否正确
if num_at == 1 and num_dot >= 1:    #或者用 if '.' in email 替换 num_dot >= 1
    print("邮箱格式正确✅️")
else :
    print("邮箱格式错误❌️")

print("🎯 邮箱格式大冒险！")
print("规则很简单：要有1个@，至少1个. 就让你过关！😎")

email = input("✏️ 壮士，请出示你的邮箱：")

num_at = email.count('@')
num_dot = email.count('.')

if num_at == 1 and num_dot >= 1:
    print("🎉 哇塞！格式正确！你是个合格的互联网公民！")
    print("   _.--._")
    print("  (  👍  )")
    print("   '--'--'")
else:
    print("❌ 哎呀呀！格式不对哦～")
    if num_at != 1:
        print(f"   💢 你放了 {num_at} 个@，我需要正好1个啊喂！")
    if num_dot < 1:
        print(f"   💢 你放了 {num_dot} 个.，至少要有1个点才行啦！")
    print("😝 再试试吧，骚年！")



"""
    练习:
    1. 输入一个字符串,判断该字符串是否是回文(两边对称)
    2. 将用户输入的10个字符串,反转后全部转为大写,然后记录在列表中,最后将列表内容,遍历输出出来   
"""
#练习一
str1 = input("请输入要判断的字符串:")
if str1 == str1[::-1] :
    print('该字符串是回文')
else :
    print('该字符不是回文')


#练习二
s = []
for i in range(10):
    str_input = input(f"请输入第{i+1}个字符串: ")
    str_input_oppo_upper = str_input[::-1].upper()
    s.append(str_input_oppo_upper)
for item in s:
    print(item)
