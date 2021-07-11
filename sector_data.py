import json

newData = list()

with open('search_tikers.json') as json_file:
   data = json.load(json_file)["data"]["rows"]

for i in range(len(data)):
   newData.append(data[i]["sector"])

newData.remove(newData[11])
newData = tuple(dict.fromkeys(newData))
newData = {
   "sectors": list(newData)
}
print(newData)