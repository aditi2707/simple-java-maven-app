import sys
import os
glob = "Never Have I Ever"
def callFunc():
  os.environ['a'] = "Aditi"
  os.environ['b'] = "Srivastava"
  list = [os.environ['a'], os.environ['b']]
  return list
  print('------')
if __name__ == '__main__':
  print(callFunc())

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
