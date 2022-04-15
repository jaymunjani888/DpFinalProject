from apscheduler.schedulers.blocking import BlockingScheduler
import requests, time
import pymongo

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1440)
def timed_job():
    client = pymongo.MongoClient("mongodb+srv://Ruchit:1234@cluster0.8uyay.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.get_database('Test1')
    records = db.Test1


#while True:
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    #r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=1440min&apikey=JM3G4VEGRLIU5WLY',verify=False)
    r = requests.get('https://api.weatherapi.com/v1/forecast.json?key=3185d7975ee149ed9e9200725220804&q=London&days=7&aqi=yes&alerts=no')
    if r.status_code ==200:
        data = r.json()
        records.delete()
        records.insert_one(data)
        #time.sleep(600000)
    

        
    else:
        exit()

sched.start()