import sys
import os
glob = "Never Have I Ever"
def test():
  print('Yes')
def callFunc(a):
  a = "Aditi"
  b = "Srivastava"
  list = [a, b]
  return a
  print('------')
if __name__ == '__main__':
  args = sys.argv
  print(globals()[args[1]](args[2]))

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
