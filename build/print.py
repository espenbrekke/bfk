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

index={}
   
def populateIndex(data):
    for key in data:
        item=data[key]
        if isinstance(item, list):
            populateIndexFromList(item)
        elif isinstance(item,dict):
            if "id" in item:
                id=item["id"]
                index[id]=item
            populateIndex(item)

def populateIndexFromList(aList):
    for item in aList:
        if isinstance(item, list):
            populateIndexFromList(item)
        elif isinstance(item,dict):
            populateIndex(item)

i = 1
while i < len(sys.argv):
    arg=sys.argv[i]
    print("**********"+arg+"************")
    if os.path.isfile(arg):
      with open(arg) as f:
        data = json.load(f)
      print(data)
      populateIndex(data)
    i += 1
    print("----------"+arg+"-------------")

for uri in index:
    print(uri+"\n")
