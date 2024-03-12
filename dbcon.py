from flask import Flask
from flask import render_template
import pymongo
import dash
from dash import dcc, html
import pandas as pd

app = Flask(__name__)
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Weather_db"]
collection = db["data"]

# Fetch data from MongoDB and convert to DataFrame
data_from_mongodb = list(collection.find({}, {"_id": 0}))
df = pd.DataFrame(data_from_mongodb)

# Dashboard layout
dash_app.layout = html.Div([
    html.H1('Weather Data Dashboard'),
    dcc.Graph(
        id='weather-graph',
        figure={
            'data': [
                {'x': df['city'], 'y': df['temperature'], 'type': 'bar', 'name': 'Temperature'},
                {'x': df['city'], 'y': df['humidity'], 'type': 'bar', 'name': 'Humidity'}
            ],
            'layout': {
                'title': 'Temperature and Humidity by City'
            }
        }
    )
])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
