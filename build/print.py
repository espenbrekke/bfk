import sys
import os
import json

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

index={}

index["a"]=1
index["b"]=1
   
def populateIndex(data):
    if isinstance(data, basestring):
         return
    print("populateIndex")
    print(data.keys())
    for key in data:
        if isinstance(data, dict):
            item=data[key]
        else:
            item=key
        if isinstance(item, list):
            for listItem in item:
               populateIndex(listItem)
        elif isinstance(item,dict):
            if "id" in item.keys():
               id=item["id"]
               index[id]=1
               print("-"+id)
            else:
               print("-")
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
