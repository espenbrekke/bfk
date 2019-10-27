import sys
import os
import json

print("Number of arguments:"+ str(len(sys.argv))+ "arguments.")
print("Argument List:"+ str(sys.argv))

base="http://data.bufdir.no/bfk/"
newBase="http://data.bufdir.no/bfk2/"

def writeJson(id, data):
   relId=id.replace(base,"");
   if not id.endswith(".json"):
      relId=relId+".json"
   if relId.startswith("http"):
      return id
   fullId=newBase+relId
   data["id"]=fullId
   targetFile="__out/"+relId
   targetDir="/".join(targetFile.split('/')[:-1])
   if not os.path.exists(targetDir):
      os.makedirs(targetDir)
   niceString=json.dumps(data, indent=4, sort_keys=True)
   with open(targetFile, 'w') as outfile:
      print(niceString, outfile)
   return fullId
      
index={}

def populateIndex(data):
   id="";
   if isinstance(data, dict):
      result={}
      for key in data:
         value=data[key]
         if key=="id":
            id=value
         result[key]=populateIndex(value)
      if(id != ""):
         newId=writeJson(id, result)
         index[id]=result
         return newId
      return result
   elif  isinstance(data, list):
      result=[]
      for value in data:
         result.append(populateIndex(value))
      return result
   return data

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
    print(uri+":\n")
    print(index[uri])
