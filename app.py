
from flask import Flask, request, jsonify,render_template
import pymongo
import datetime

app = Flask(__name__)
#data = {}
today = str(datetime.date.today())
data2 = {'time': 'Temperature degree celcius'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/google-charts/pie-chart')
def google_pie_chart():
    x = fetchdataforPieChart()
    data = fetchdataforPieChart()
    return render_template('pie-chart.html',data=data)

@app.route('/google-charts/bar-chart')
def google_bar_chart():
    #data1 = {'Task':'Hours per Day','Work': 11,'Eat':2,'Commute':2,'Watch TV':2,'Sleep':7}
    #data1 = {'Task':'Hours per Day','maxtemp_c':10.8}
    data1 = fetchdataforBarChart()
    return render_template('bar-chart.html',data=data1)

@app.route('/google-charts/line-chart')
def google_line_chart():
    #data1 = {'Task':'Hours per Day','Work': 11,'Eat':2,'Commute':2,'Watch TV':2,'Sleep':7}
    #data1 = {'Task':'Hours per Day','maxtemp_c':10.8}
    data2 = fetchdataLineChart()
    return render_template('line-chart.html',data=data2)

def fetchdataforPieChart():
    client = pymongo.MongoClient("mongodb+srv://Ruchit:1234@cluster0.8uyay.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # Database Name
    db = client["Test1"]
    # Collection Name
    col = db["Test1"]
    data = {'Air-Quality': 'Proportion'}
    x = col.find_one()
    # print(type(x))
    current = (x.get("current"))
    day = current.get("last_updated")
    # datetime_obj = datetime.strptime(abc, '%y/%m/%d')
    if (day[0:10]) == (today):
        air_quality = (current.get("air_quality"))
        air_quality.pop('us-epa-index')
        air_quality.pop('gb-defra-index')
        data.update(air_quality)
        return data

def fetchdataforBarChart():
    client = pymongo.MongoClient("mongodb+srv://Ruchit:1234@cluster0.8uyay.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # Database Name
    db = client["Test1"]
    # Collection Name
    col = db["Test1"]
    data = {'Date':'Avg Humidity'}
    x = col.find_one()
    # print(type(x))
    current = (x.get("current"))
    day = current.get("last_updated")
    # datetime_obj = datetime.strptime(abc, '%y/%m/%d')
    forecastday = (x.get("forecast")).get('forecastday')
    if (day[0:10]) == (today):
        for i in forecastday:
            # print (i.get('date'))
            # print (((i.get('day')).get('avghumidity')))
            data[i.get('date')] = (i.get('day')).get('avghumidity')
        return data


# lastupdated = datetime.datetime(2022, 4, 7)
today = str(datetime.date.today())

def fetchdataLineChart():
    client = pymongo.MongoClient("mongodb+srv://Ruchit:1234@cluster0.8uyay.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    # Database Name
    db = client["Test1"]

    # Collection Name
    col = db["Test1"]

    x = col.find_one()

    # print(type(x))

    current = (x.get("current"))
    day = current.get("last_updated")
    # datetime_obj = datetime.strptime(abc, '%y/%m/%d')

    forecastday = (x.get("forecast")).get('forecastday')

    for i in forecastday:
        # print (i.get('date'))
        # print (((i.get('day')).get('avghumidity')))
        # data[(i.get('hour')).get('avghumidity')]= (i.get('day')).get('avghumidity')
        # print (i.get('hour'))
        for j in i.get('hour'):
            data2[j.get('time')] = j.get('temp_c')

    return data2

if __name__ == '__main__':
    app.run()