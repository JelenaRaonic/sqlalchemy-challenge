
# Import Flask
from operator import and_
from flask import Flask, jsonify

# Import SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# Import Numpy and Datetime
import numpy as np
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
measurement=Base.classes.measurement
station=Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")

#  1.Start at the homepage
@app.route("/home")

def homepage():

    #list all available routes
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>" 
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>"

    )

 #  2. Route source PRECIPITATION
@app.route("/api/v1.0/precipitation")
def precipitation():
    #open session
    session = Session(engine)

    date_precipation = session.query(measurement.date, measurement.prcp)\
                .filter(measurement.date > "2016-08-22").\
                order_by(measurement.date.desc()).all()

    session.close()

    prcp_data = []

    for date, prcp in date_precipation:
        prcp_dictionary = {}
        prcp_dictionary[date] = prcp

        prcp_data.append(prcp_dictionary)
    
    return jsonify(prcp_data)


#   3. Route source STATIONS
@app.route("/api/v1.0/stations")
def stations():
    #open session
    session = Session(engine)

    most_active_stations = session.query(measurement.station, func.count(measurement.station)).\
                        group_by(measurement.station).\
                        order_by(func.count(measurement.station).desc()).all()


    session.close()

    list_station = list(np.ravel(most_active_stations))
    
    return jsonify(list_station)


#  4. Route source TOBS
@app.route("/api/v1.0/tobs")
def tobs():
    #open session
    session = Session(engine)

    most_active_stations_previous_year = session.query(measurement.date, measurement.tobs).\
                        filter(measurement.date > "2016-08-22").\
                        filter(measurement.station == "USC00519281").all()
    session.close()
    tobs_data = []

    for date, tobs in most_active_stations_previous_year:
        tobs_dictionary = {}
        tobs_dictionary[date] = tobs

        tobs_data.append(tobs_dictionary)
    
    return jsonify(tobs_data)



# 5. min, max and avg temp for specific start or start-end range
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def stats(start=None, end=None):
    
    session = Session(engine)
    
    query_item = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]

    try:
        start = dt.datetime.strptime(start, "%m%d%Y")
        if end:
            end = dt.datetime.strptime(end, "%m%d%Y")
    except ValueError:
        session.close()
        return jsonify({"error": "Invalid date format, please use MMDDYYYY"}), 400

    if end:
        results = session.query(*query_item).filter(measurement.date >= start, measurement.date <= end).all()
    else:
        results = session.query(*query_item).filter(measurement.date >= start).all()
    session.close()

    if results:
        temps = list(np.ravel(results))
        return jsonify(temps)
    else:
        return jsonify({"error": "No data found for the given dates"}), 404

if __name__ == '__main__':
    app.run(debug=True)

        

