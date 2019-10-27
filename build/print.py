import sys
import os
import json

print 'Number of arguments:'+ len(sys.argv)+ 'arguments.'
print 'Argument List:'+ str(sys.argv)

index={}
   
def populateIndex(data):
   id="";
   if isinstance(data, basestring):
      return
   if isinstance(data, dict):
      result={}
      for key in data:
         value=data[key]
         print(key)
         if key=="id":
            print("its id")
            id=value
         result[key]=value
      if(id != ""):
         index[id]=result
         return id
      return result
   elif  isinstance(data, list):
      result=[]
      for value in data:
         result.append(populateIndex2(value))
      return result
   return data

i = 1
while i < len(sys.argv):
    arg=sys.argv[i]
    print("**********"+arg+"************")
    if os.path.isfile(arg):
      with open(arg) as f:
        raw_data = f.read()
        data = json.loads(raw_data.decode('utf-8'))
      populateIndex(data)
    i += 1
    print("----------"+arg+"-------------")

for uri in index:
    print(uri+"\n")
