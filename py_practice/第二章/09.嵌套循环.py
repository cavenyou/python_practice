# 案例-------输出一个长度为10,宽度为5的长方形
# length = int(input("请输入长方形的长度: "))
# width  = int(input("请输入长方形的宽度: "))
# for i in range(width):
#     for j in range(length):
#         print("*",end=" ") #print语句自带换行操作,加上(,end=" ")就把换行转义
#     print()

# 案例-----------打印九九乘法表
# print("九九乘法表:")
# for i in range(1,10) :
#     for j in range(1,i+1) :
#          print (f"{j}×{i}={j*i}",end=" ")
#     print()

# 案例------------根据输入的直角边的边长，打印等腰直角三角形
#输入直角边边长
# length = int(input("请输入要打印的直角边的边长: "))
#
# #打印直角三角形
# for i in range(length):
#     for j in range(i+1):    #由于i是从零开始的
#         print("*",end="\t")
#     print()


#案例-------------根据输入的数字，打印对应的数字金字塔
#输入数字
# num = int(input("请输入要打印数字金字塔对应的数字："))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end="\t")
#     print()

#案例-----------------打印国际象棋棋盘
for i in range(1,9):
    for j in range(1,9):
        if (i+j)%2==0:
            print ("■",end="\t")
        else:
            print("□",end="\t")
    print()

