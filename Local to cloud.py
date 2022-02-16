import pymongo
import time
import csv
import json
import io
import requests
t0 = time.time()

with open(r'(file location)', 'r') as data_file:
   data_json = json.load(data_file)
seconds = time.time()
print("Time in seconds since the epoch:", seconds)
local_time = time.ctime(seconds)
print("Local time:", local_time)

myclient = pymongo.MongoClient("(Cloud server name)")
mydb = myclient["test"] 
mycol = mydb["testprogram"]


# formula is: { "collumn 1": "data", "collumn 2": "data"},
#mylist = json.loads('testmongo.txt')

#reader = csv.DictReader(io.StringIO(download.text))
#json_data = json.dumps(list(reader))  
x = mycol.insert_many(data_json)

 
#print list of the _id values of the inserted documents:
t1 = time.time()
#print(x.inserted_ids)

total = t1-t0
print(total)
