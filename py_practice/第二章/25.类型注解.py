"""
    类型注解:
    python中的一种语法特性,用于明确标识变量,函数参数和返回值的数据类型,从而使代码更清晰,更安全,更易维护
"""
# 定义变量----用类型注解,后续如果将不同类型值定义到该变量时就会有错误提示
a: int = 695

score: float = 98.5

hobby: str = "Python"

flag: bool = True

pic: None = None

names: list[str | int] = ["A", "C", "E" , 1 , 2, 3 ]

phones: set[str] = {"13309091111", "15209109121"}

options: dict[str, int] = {"count": 0, "total": 0}

goods: tuple[str, int, int] = ("手机", 5999, 1)

"""
    类型推断: 
    未进行类型注解的变量,python解释器根据定义的值来判断变量,表达式和函数返回值的数据类型
    所以在对变量直接赋值时,或者涉及变量的运算,容器的推导,解释器会自动推导出变量的类型
"""

#函数的类型注解
def calc(scores: list[int]) -> float:#前面是函数参数的数据类型,后面是函数返回值的类型
    return sum(scores) / len(scores)

def calc_data(scores: list[int]) -> tuple[int, int, float]:
    max_v = max(scores)
    min_v = min(scores)
    avg_v = sum(scores) / len(scores)
    return max_v, min_v, avg_v

