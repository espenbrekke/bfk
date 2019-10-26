import sys
import os
import json

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

index={}
   
def populateIndex(data):
    print("populateIndex"+"\n")
    print(data)
    for key in data:
        item=data[key]
        if isinstance(item, list):
            for listItem in item:
               populateIndexFromList(listItem)
        elif isinstance(item,dict):
            if "id" in item:
                id=item["id"]
                index[id]=item
                print(id+"\n")
            populateIndex(item)

i = 1
while i < len(sys.argv):
    arg=sys.argv[i]
    print("**********"+arg+"************")
    if os.path.isfile(arg):
      with open(arg) as f:
        data = json.load(f)
      populateIndex(data)
    i += 1
    print("----------"+arg+"-------------")

for uri in index:
    print(uri+"\n")
