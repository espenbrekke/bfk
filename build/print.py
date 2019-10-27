import sys
import os
import json

print("Number of arguments:"+ str(len(sys.argv))+ "arguments.")
print("Argument List:"+ str(sys.argv))

base="http://data.bufdir.no/bfk/"
newBase="http://data.bufdir.no/bfk2/"

def writeJson(id, json):
   relId=id.replace(base,"");
   fullId=relId
   if not fullId.startswith("http://"):
      fullId=fullId
   json["id"]=fullId
   targetFile="out/"+relId
   targetDir=targetFile.split('\\')[:-1]
   if not os.path.exists(targetDir):
      os.makedirs(targetDir)
   with open(targetFile, 'w') as outfile:
      json.dump(json, outfile)
      
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
         writeJson(id, result)
         index[id]=result
         return id
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
