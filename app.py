#from sched import scheduler
from flask import Flask, request, jsonify,render_template
#import requests, time
#import pymongo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/google-charts/pie-chart')
def google_pie_chart():
    data = {'Task':'Hours per Day','Work': 11,'Eat':2,'Commute':2,'Watch TV':2,'Sleep':7}
    #data = getRecord()
    return render_template('pie-chart.html',data=data)

@app.route('/google-charts/bar-chart')
def google_bar_chart():
    data1 = {'Task':'Hours per Day','Work': 11,'Eat':2,'Commute':2,'Watch TV':2,'Sleep':7}

    #data1 = getRecord()
    return render_template('bar-chart.html',data=data1)
'''    
def getRecord():
    client = pymongo.MongoClient("mongodb+srv://Ruchit:1234@cluster0.8uyay.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.get_database('Test1')
    records = db.Test1
    
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=JM3G4VEGRLIU5WLY')
    
    if r.status_code ==200:
        data = r.json()
        print(data)
        records.insert_one(data)
            
    
    return records
'''    
if __name__ == '__main__':
    app.run()

