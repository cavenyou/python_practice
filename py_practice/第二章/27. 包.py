"""
    包：
    本质就是一个文件夹，该文件夹中可以包含若干Python模块（.py文件），文件夹下还包含了一个 __init__.py(用来描述当前包的信息)。
    作用：模块文件较多时，用来管理多个模块。（包的本质也是一个模块）

    包的导入方式:
    import 包名.模块名	        import utils.my_fun	                            包名.模块名.功能名	    utils.my_fun.log_separator1()
    from 包名 import 模块名	    from utils import my_fun	                    模块名.功能名	        my_fun.log_separator1()
    from 包名 import *	        from utils import *	                            模块名.功能名	        my_fun.log_separator1()
    from 包名.模块名 import 功能名	from utils.my_fun import log_separator1	        功能名	            log_separator1()
    from 包名.模块名 import *	    from utils.my_fun import *	                    功能名	            log_separator1()

    如果用*来导入,那么需要在__init__.py文件中加入 __all__ = []
"""
#导入包
import util01.own_function as own_fun
own_fun.long_seperator1()