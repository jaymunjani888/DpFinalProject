from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/google-charts/pie-chart')
def google_pie_chart():
    data = {'Task':'Hours per Day','Work': 11,'Eat':2,'Commute':2,'Watch TV':2,'Sleep':7}
    #return render_template('index.html')
    return render_template('pie-chart.html',data=data)
    
if __name__ == '__main__':
    app.run()

