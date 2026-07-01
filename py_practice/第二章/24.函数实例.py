"""
    案例1: 计算N的阶乘
"""
def factorial(n):
    """
    这个函数用来计算输入n的阶乘
    :param n: 阶乘阶数,请大于等于0
    :return: n!
    """
    fac = 1
    # if n == 0:
    #     return 1 #这部分好像多余了,n为零时,range(0)为空,fac保持为1
    # else:
    for i in range(n):
        fac *= i + 1
    return fac

user_input = input("请输入要计算的阶乘数(请输入自然数): ")
if not user_input.isdigit(): #isdigit()方法是来判断字符串是不是只有数字
    print(f"请输入一个整数,现在的输入为:{user_input}")
else:
    N = int(user_input)
    # if N < 0:
    #     print(f"请输入一个不小于0的整数,现在的输入为{N} ")    #这部分也可以删了,负数含"-",也会被isdigit()拦截
    # else :
    print(f"{N}的阶乘为{factorial(N)}")

'''
    递归写法:
    def factorial(n):
    """
    这个函数用来计算输入n的阶乘
    :param n: 阶乘阶数,请大于等于0
    :return: n!
    """
    if n <= 1:          # 基线条件（停止）
        return 1
    return n * factorial(n - 1)  # 递归条件（调用自己）
'''

"""
    案例2: 电商订单计算器
    定义一个函数,用于根据传入的一批商品信息(商品名,价格,数量),优惠(优惠券,积分抵扣),运费信息计算订单的总金额
    规则如下:
    1. 优惠券需要商品金额满5000才可以使用,且优惠券金额不能超过商品总价
    2. 积分抵扣需要商品总金额满5000才可以使用,100积分抵扣1元(且抵扣金额不能超过商品总价,积分只能整百抵扣)
"""
def e_commerce_order_calculator(coupon,points,shipping_cost,*args):
    """
    函数用于根据传入的一批商品信息(商品名,价格,数量),优惠(优惠券,积分抵扣),运费信息计算订单的总金额
    规则如下:
    1. 优惠券需要商品金额满5000才可以使用,且优惠券金额不能超过商品总价
    2. 积分抵扣需要商品总金额满5000才可以使用,100 积分抵扣1元(且抵扣金额不能超过商品总价,积分只能整百抵扣)
    :param args: 商品信息(name,price,num)
    :param coupon:  优惠券
    :param points:  积分
    :param shipping_cost: 运费
    :return: 优惠前金额,优惠后金额,剩余积分
    """
    original_price = 0
    #计算总价(不带优惠和运费)
    for item in args:
        original_price += item[1] * item[2]

    #判断是否可以使用优惠券
    if original_price >= 5000 and coupon <= original_price:
        after_coupon_price = original_price - coupon
    else:
        after_coupon_price = original_price

    #判断是否可以用积分抵扣完全,并计算剩余积分
    if original_price >= 5000:
        if after_coupon_price + shipping_cost > points//100:
            final_price = shipping_cost + after_coupon_price - points//100
            remaining_points = 0
        else :
            final_price = 0
            remaining_points = points - (after_coupon_price + shipping_cost)*100
    else:
        final_price = after_coupon_price + shipping_cost
        remaining_points = points
    return original_price, final_price,remaining_points

#输入商品信息
goods_info = []
while True:
    choice = input("请输入商品信息: 1.继续输入  2.输入完成\n")
    match choice:
        case "1":
            name = input("请输入商品名称: ")
            #检验商品价格是否符合规范和价格--------并没有检查是否输入非数字字符,因为上一个案例已经分析了,利用isdigit()可以判断num
            while True:
                price = float(input("请输入商品价格: "))
                if price > 0:
                    break
                print("商品价格要大于0,请重新输入商品价格")
            while True:
                num = int(input("请输入商品数量: "))
                if num > 0:
                    break
                print("商品数量不能小于1,请重新输入商品数量")
            goods_info.append([name,price,num])
        case "2":
            print("商品输入完毕")
            break
        case _ :
            print("输入错误")
#输入优惠信息和运费信息
coupon = float(input("请输入优惠券的金额: "))
points = int(input("请输入剩余积分数: "))
shipping_cost = float(input("请输入运费: "))

#调用函数
o_price,f_price,remaining_points = e_commerce_order_calculator(coupon,points,shipping_cost,*goods_info)

#打印信息
print(f"这批商品优惠前需支付的金额为{o_price},优惠后需支付的金额为{f_price}元,原积分为{points}分,还剩余{remaining_points}分")
