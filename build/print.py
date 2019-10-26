import sys
import os
import json

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

i = 1
while i < len(sys.argv):
    arg=sys.argv[i]
    if os.path.isfile(arg):
      print(arg+" exists")
    else: 
      print(arg+" missing")
    i += 1

i = 1
while i < len(sys.argv):
    arg=sys.argv[i]
    if os.path.isfile(arg):
      with open('path_to_file/person.json') as f:
        data = json.load(f)
      print(data)
    i += 1
