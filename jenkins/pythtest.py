import sys
def callFunc(a, b):
  return a
  return b
  print('------')
if __name__ == '__main__':
  locals()[sys.argv[1]](sys.argv[2], sys.argv[3])

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
