import requests, time
import pymongo

client = pymongo.MongoClient("mongodb+srv://Ruchit:1234@cluster0.8uyay.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.get_database('Test1')
records = db.Test1


while True:
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=JM3G4VEGRLIU5WLY',verify=False)
    
    if r.status_code ==200:
        data = r.json()
        print(data)
        #records.insert_one(data)
        time.sleep(600000)
else:
    exit()