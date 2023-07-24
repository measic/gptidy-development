# inspect 模块
# signature(callable), 获取签名(函数签名包含了一个函数的信息，包含函数名，它的参数类型，它所在的类和名称空间及其信息)

import inspect

def add(x: int, y: int, *args, **kwargs) -> int:  # 可变参数 不建议加 int 因为可以收集不同类型参数
    return x + y

sig = inspect.signature(add)