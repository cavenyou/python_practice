"""
    案例:
    1. 计算每个学生的总分,各科平均分,然后一并输出出来
    2. 统计各科成绩的最低分,最高分,平均分
    3. 查找成绩优秀(平均分大于90)的学生,并输出
"""

#录入数据
students_scores = (
    ("S001", "王林 ", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三 ", 78, 85, 82),
    ("S004", "曾牛 ", 88, 79, 91),
    ("S005", "周轶 ", 95, 96, 89),
    ("S006", "王卓 ", 76, 82, 77),
    ("S007", "红蝶 ", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木 ", 86, 89, 98),
    ("S010", "通天 ", 66, 59, 72),
)

#计算总分和平均分
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for s in students_scores:
    total = s[2] + s[3] + s[4]
    average = total/3
    print(f'{s[0]}\t{s[1]}\t{s[2]}\t\t{s[3]}\t\t{s[4]}\t\t{total}\t\t{average:.1f}')

#利用元组解包的方法对上述循环进行优化,增强其可读性
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for id,name,chinese,math,english in students_scores:
    total = chinese + math + english
    average = total/3
    print(f'{id}\t{name}\t{chinese}\t\t{math}\t\t{english}\t\t{total}\t\t{average:.1f}')

#统计各科成绩的最高分,最低分,平均分
#将各科成绩拉出来
chinese_scores = [s[2] for s in students_scores]
math_scores    = [s[3] for s in students_scores]
english_scores = [s[4] for s in students_scores]

#找到最高分最低分对应的索引,找到对应的名字
max_index_chinese = chinese_scores.index(max(chinese_scores))
max_index_math = math_scores.index(max(math_scores))
max_index_english = english_scores.index(max(english_scores))
min_index_chinese = chinese_scores.index(min(chinese_scores))
min_index_math = math_scores.index(min(math_scores))
min_index_english = english_scores.index(min(english_scores))

#输出
print(f"语文成绩最高分是{students_scores[max_index_chinese][1].strip()}的{max(chinese_scores)}分,"
      f"最低分为{students_scores[min_index_chinese][1].strip()}的{min(chinese_scores)}分,"
      f"语文的平均分为{sum(chinese_scores)/len(chinese_scores)}分")
print(f"数学成绩最高分是{students_scores[max_index_math][1].strip()}的{max(math_scores)}分,"
      f"最低分为{students_scores[min_index_math][1].strip()}的{min(math_scores)}分,"
      f"数学的平均分为{sum(math_scores)/len(math_scores)}分")
print(f"英语成绩最高分是{students_scores[max_index_english][1].strip()}的{max(english_scores)}分,"
      f"最低分为{students_scores[min_index_english][1].strip()}的{min(english_scores)}分,"
      f"英语的平均分为{sum(english_scores)/len(english_scores)}分")

#查找优秀学生
print("成绩优秀的学生为: ")
for s in students_scores:
    if (s[2] + s[3] + s[4])/3 > 90 :
        print(f"{s[1].strip()}",end=" ")