import sys
def callFunc(a, b):
  a = "why"
  b = "Aditi"
  print('------')
if __name__ == '__main__':
  args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
  globals()[args[1]](*args[2:])
