import sys
import builtins
import module1.s1

# print(sys.path)
# 输出：
'''
['/root/github/liubei90/demo/python', 
'/usr/lib64/python36.zip', 
'/usr/lib64/python3.6', 
'/usr/lib64/python3.6/lib-dynload', 
'/root/.local/lib/python3.6/site-packages', 
'/usr/local/lib/python3.6/site-packages', 
'/usr/lib64/python3.6/site-packages', 
'/usr/lib/python3.6/site-packages']
'''

# print(dir(sys))
'''
['__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', 
'__loader__', '__name__', '__package__', '__spec__', '__stderr__', 
'__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', 
'_debugmallocstats', '_getframe', '_git', '_home', '_xoptions', 
'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 
'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 
'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', 'excepthook', 
'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 
'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_wrapper', 
'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 
'getdlopenflags', 'getfilesystemencodeerrors', 'getfilesystemencoding', 
'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 
'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 
'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 
'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 
'set_asyncgen_hooks', 'set_coroutine_wrapper', 'setcheckinterval', 
'setdlopenflags', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 
'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 
'version_info', 'warnoptions']
'''

# print(dir(builtins))
'''
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 
'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 
'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 
'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 
'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 
'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 
'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 
'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 
'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 
'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 
'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 
'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 
'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 
'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 
'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 
'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 
'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 
'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', 
'__build_class__', '__debug__', '__doc__', '__import__', '__loader__', 
'__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 
'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 
'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 
'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 
'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 
'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 
'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 
'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 
'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 
'tuple', 'type', 'vars', 'zip']
'''

# print(dir(module1))
'''
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__path__', '__spec__']
'''

print(dir(module1.s1))
'''
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__', 'f1']
'''

# print(dir())
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', 
'__file__', '__loader__', '__name__', '__package__', '__spec__', 'sys']
'''