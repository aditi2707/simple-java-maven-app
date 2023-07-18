import sys
import os
from another import *
glob = "Never Have I Ever"
def callFunc(a):
  a = another.getValue(a)
  b = "Srivastava"
  list = [a, b]
  #return a
  print(a)
if __name__ == '__main__':
  test()
  args = sys.argv
  print(locals()[args[1]](args[2]))

"""
import sys

def print_fn():
    print("Hi")

def sum_fn(a, b):
    print(a + b)

if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    globals()[args[1]](*args[2:])
"""
