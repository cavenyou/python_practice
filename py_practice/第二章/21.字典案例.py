"""
    案例: 进行购物车操作
    1. 添加购物车: 添加商品名称,价格和数量
    2. 修改购物车
    3. 删除购物车
    4. 查询购物车
    5. 退出购物车
"""

#购物车界面
muse = """
############## 购物车操作系统 ###################
#             1. 添加购物车                    #
#             2. 修改购物车                    #
#             3. 删除购物车                    #
#             4. 查询购物车                    #
#             5. 退出购物车                    #
##############################################
"""
# 利用字典 shopping_cart = {shopping_name:{price:shopping_price,num:shopping_num}}
shopping_cart = {}
while True:
    print(muse)
    choice = input("请输入数字以执行对应的操作(1-5): ")

    #主程序
    #match匹配

    match choice:
    #添加购物车
        case "1":
            shopping_name = input("请输入添加的商品名称:")
            if  shopping_name not in shopping_cart.keys():
                shopping_price = float(input("请输入添加的商品价格:"))
                shopping_num = int(input("请输入添加的商品数量:"))
                shopping_cart[shopping_name] = {"price":shopping_price,"num":shopping_num}
                print("商品添加成功")
            else :
                print("商品已在购物车中")

    #修改购物车
        case "2":
            shopping_name = input("请输入要修改的商品名称:")
            if shopping_name  in shopping_cart.keys():
                shopping_price = float(input("请输入修改后的商品价格:"))
                shopping_num = int(input("请输入修改后的商品数量:"))
                shopping_cart[shopping_name] = {"price": shopping_price, "num": shopping_num}
                print("商品修改成功")
            else:
                print("要修改的商品不在购物车中")

    #删除购物车
        case "3":
            shopping_name = input("请输入要删除的商品名称:")
            if shopping_name in shopping_cart.keys():
                del shopping_cart[shopping_name]
                print("商品删除成功")
            else:
                print("要删除的商品不在购物车中")

    #查询购物车
        case "4":
            if not shopping_cart:
                print("购物车为空,请添加商品")
            else :
                for goods in shopping_cart.keys():
                    goods_info = shopping_cart[goods]
                    print(f"商品名称: {goods},商品价格: {goods_info['price']},商品数量: {goods_info['num']}")

    #退出购物车
        case "5":
            shopping_cart.clear()
            print("操作完成")
            break
        case _ :
            print("输入错误")


