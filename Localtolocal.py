import pymongo
import time
t0 = time.time()
import csv
import json
import io
import requests
#with requests.Session() as s:
 #   download = s.get('https://github.com/gibello/whocovid19/blob/master/global_who_data.csv?raw=true')
with open(r'local location', 'r') as data_file:
   data_json = json.load(data_file)
seconds = time.time()
print("Time in seconds since the epoch:", seconds)
local_time = time.ctime(seconds)
print("Local time:", local_time)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testpython1"] 
mycol = mydb["testpymongo"]


# formula is: { "collumn 1": "data", "collumn 2": "data"},
#mylist = json.loads('testmongo.txt')

#reader = csv.DictReader(io.StringIO(download.text))
#json_data = json.dumps(list(reader))
x = mycol.insert_many(data_json)

t1 = time.time()

#print list of the _id values of the inserted documents:
#print(x.inserted_ids)


total = t1-t0
print(total)




      