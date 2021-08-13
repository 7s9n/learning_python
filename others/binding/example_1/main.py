from ctypes import *
from typing import (
    List,
    Any
)

lib = cdll.LoadLibrary('./test.so')

def wrap_function(funcname: str, argtypes: List[Any]= None, restype: Any= None):
    func = lib.__getattr__(funcname)
    func.argtypes = argtypes
    func.restype = restype
    return func


func = wrap_function('func')
sum_cpp = wrap_function('sum', [c_int, c_int], c_int)


func()
print(sum_cpp(1 , 200))
