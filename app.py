import datetime as dt
import numpy as np
import pandas as pd
import json

#My SQL Class I wrote
from sqlHelper import SQLHelper
from flask import Flask, jsonify

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

sqlHelper = SQLHelper()

#################################################
# Flask Routes
#################################################
@app.route("/api/v1.0/precipitation")
def get_total_rain():
    data = sqlHelper.getRainOnDates()
    #convert to json string
    data = data.to_json(orient='records')
    #convert to list
    data = json.loads(data)
    #return jsonify
    return(jsonify(data))

@app.route("/api/v1.0/stations")
def get_all_station_data(): #insert a variable
    data = sqlHelper.getAllStationData()
    return(jsonify(json.loads(data.to_json(orient='records')))) #hack it all into one line

@app.route("/api/v1.0/tobs")
def get_active_station_data(): #insert a variable
    data = sqlHelper.getActiveStationData()
    return(jsonify(json.loads(data.to_json(orient='records')))) #hack it all into one line

@app.route("/api/v1.0/temperature/<start>")
def get_temp_for_date(start): #insert a variable
    data = sqlHelper.getTempForDate(start)
    return(jsonify(json.loads(data.to_json(orient='records')))) #hack it all into one line


@app.route("/")
def home():
    return (
        f"Welcome to the Hawaii Rainfall Report!<br/>"

        f"""
        <ul>
            <li><a target="_blank" href='/api/v1.0/precipitation'>Get All Rain On Date Here</a></li>
            <li><a target="_blank" href='/api/v1.0/stations'>Get All Station Data Here</a></li>
            <li><a target="_blank" href='/api/v1.0/tobs'>Get Most Active Station Data Here</a></li>
            <li><a target="_blank" href='/api/v1.0/temperature/2017-03-18'>Get Temperature For Date</a></li>
        </ul>
        """
    )


#################################################
# Flask Run
#################################################
if __name__ == "__main__":
    app.run(debug=True)
