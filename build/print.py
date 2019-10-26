import sys
import os

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

i = 1
while i < len(sys.argv):
    arg=sys.argv[i]
    os.path.isfile(arg)
      print(arg+" exists")
    else 
      print(arg+" missing")
    i += 1
