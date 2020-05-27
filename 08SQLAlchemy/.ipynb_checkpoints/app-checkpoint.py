import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><end>"
        )
# Create session and query precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation_result = session.query(Measurement.prcp, Measurement.date)\
                                  .filter(Measurement.date >= query_date).all()
    session.close()
    
    # Create dictionary and append to a list of precipitation
    pre = []
    for date, prcp in precipitation_result:
        pre_dict = {}
        pre_dict["prcp"] = prcp
        pre_dict["date"] = date
        pre.append(pre_dict)
    return jsonify(pre)

# Create session and query stations
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station_result = session.query(Station.station, Station.name).all()
    session.close()
    station_list = list(np.ravel(station_result))

    return jsonify(station_list)

# Create session and query tobs
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tob_query = session.query(Measurement.tobs).filter(Measurement.station ==  Station.station)\
                       .filter(Measurement.date>query_date).filter(Station.name=='WAIHEE 837.5, HI US').all()
    session.close()
    tob_list=list(np.ravel(tob_query))
    return jsonify(tob_list)
    
# Create session and query    
@app.route("/api/v1.0/<start>")
def start(start):

    # Calculate `TMIN`, `TAVG`, and `TMAX`
    session = Session(engine)
    temp=session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)\
                .filter(Measurement.date >= start)).all()
    temp_value = []
    for TMIN, TAVG, TMAX in temp:
        temp_dict = {}
        temp_dict["TMIN"] = temp[0][0]
        temp_dict["TAVG"] = temp[0][1]
        temp_dict["TMAX"] = temp[0][1]
        temp_value.append(temp_dict)

    return jsonify(temp_value)
    session.close()
    
# Create session and query    
@app.route("/api/v1.0/<start>/<end>")
def se_date(start_date, end_date):

    session = Session(engine)
    temp_both = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
                     .filter(Measurement.date >= start_date)\
                     .filter(Measurement.date <= end_date).all()
    temp_list = list(np.ravel(temp_both))

    return jsonify(temp_list)
    session.close()


if __name__ == "__main__":
    app.run(debug=True)
    
    