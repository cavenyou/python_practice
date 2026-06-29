"""
   根据提供的班级学生的选课情况，完成如下需求：
    1. 找出同时选修了法语和艺术的学生
    2. 找出同时选修了所有四门课程的学生
    3. 找出选修了足球，但是没有选修篮球的学生
    4. 统计每一个学生选修的课程数量
"""
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "通天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}

# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}

# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎跑", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}

# 选修艺术学生名单
art_set = {"通天", "天运子", "韩立", "虎跑", "姜老道", "紫灵"}

#选修法语和艺术
french_art = french_set.intersection(art_set)
print("同时选修了法语和艺术的学生有: ")
print(french_art)

#选修全部四门
all_set = french_art.intersection(basketball_set).intersection(football_set)
print("同时选修了所有四门课程的学生有: ")
print(all_set)

# 选修足球但是没篮球
football_no_basketball_set = football_set.difference(basketball_set)
print("选修了足球但是没有选修篮球的学生有: ")
print(football_no_basketball_set)

#统计每一个学生选修的课程数量
#获取所有学生
all_students = french_set | basketball_set | football_set | art_set  #&:交集 |:并集 -:差集
for student in all_students:
    count = 0
    if student in french_set :
        count += 1
    if student in art_set :
        count += 1
    if student in basketball_set :
        count += 1
    if student in football_set :
        count += 1
    print(f"{student}:\t{count}门")