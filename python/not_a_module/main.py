import sys
import os
# 当前文件夹执行，not_a_module目录在path中
# 上个目录执行，父目录在path中
print(sys.path)

# 执行脚本时所在的文件夹
print(os.getcwd())

from m1 import say

# try:
#     # 当前文件夹不是一个模块，相对导入报错
#     from .m1 import say
# except ImportError:
#     from m1 import say


say()

if __name__ == "__main__":
    print('in __main__')
