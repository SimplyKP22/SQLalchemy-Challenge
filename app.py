from operator import index
from textwrap import indent
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create engine using the `demographics.sqlite` database file
engine = create_engine("sqlite:///hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Assign the classes to variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Now that you have completed your initial analysis, you’ll design a Flask API based on the queries.
# Create the app
app = Flask(__name__)

# Create the 'Home' route
@app.route("/")
def Home():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

    # Create the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Using this date, retrieve the previous 12 months of precipitation data by querying 
    the 12 previous months of data."""  
    
    sel = [Measurement.date,Measurement.prcp]
    monthly_precip = session.query(*sel).\
    filter(Measurement.date <= dt.date(2017,8,23)).filter(Measurement.date >= dt.date(2016,8,23)).all()

    # Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    prcp_dict = {}
    for result in monthly_precip:
        if not result[0] in prcp_dict:
            prcp_dict[result[0]] = []
            prcp_dict[result[0]].append(result[1])
        else:
            prcp_dict[result[0]].append(result[1])
    

    # Close our session
    session.close()

    # Convert list of tuples into normal list
    precip = list(np.ravel(prcp_dict))

    return jsonify(precip)

    # Create the stations route
@app.route("/api/v1.0/stations")
def stations():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a JSON list of stations from the dataset."""  
    
    staton_list = session.query(Station.id, Station.station).all()

    # Close our session
    session.close()

    # Convert list of tuples into normal list
    stations_json = list(np.ravel(staton_list))

    return jsonify(stations_json)

@app.route("/api/v1.0/tobs")
def tobs():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Query the dates and temperature observations of the most active station for the previous year of data"""  
    
    # List the stations and observation counts in descending order. Print the first listing which will be the station
    # with the highest number of observations
    station_observations = session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).\
    order_by(func.count(Measurement.station).desc()).first()

    print(f"The station with the highest number of observations is: {station_observations}")

    # Finding the station ID that matches the station description above
    highest_observation_station = session.query(Station.id).filter(Station.station == 'USC00519281').scalar()

    print(f"The ID for station {station_observations} is: {highest_observation_station}")

    # Design a query to retrieve the previous 12 months of temperature observation data (TOBS)
    sel = [Measurement.tobs]
    twelve_month_temps = session.query(*sel).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date <= dt.date(2017,8,23)).\
    filter(Measurement.date >= dt.date(2016,8,23)).all()

    # Close our session
    session.close()

    # Convert list of tuples into normal list
    monthly_TOBS_data = list(np.ravel(twelve_month_temps))
   

    return jsonify(monthly_TOBS_data)

@app.route("/api/v1.0/<start>")
def start_date(start):

    print('Date should be entered in the following format: YYYY-MM-DD')

    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start date."""

    # Create our session (link) from Python to the DB
    session = Session(engine)

    trim_date = start.replace("-", "")
    print(trim_date)
    real_date = dt.datetime.strptime(trim_date,'%Y%m%d')
    print(real_date)
    print(type(real_date))
     # Setup for the query for the start data criteria   
    sel = [Measurement.date, 
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs), 
        func.max(Measurement.tobs)]

    temp_search = session.query(*sel).filter(Measurement.date >= real_date).group_by(Measurement.date).all()
   
    # Close our session
    session.close()

    # Convert list of tuples into normal list
    start_temp_results = list(np.ravel(temp_search))

    return jsonify(start_temp_results)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):

    print('Date should be entered in the following format: YYYY-MM-DD')

    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start-end range."""

    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    trim_date = start.replace("-", "")

    real_date = dt.datetime.strptime(trim_date,'%Y%m%d')

    trim_date2 = end.replace("-", "")

    real_date2 = dt.datetime.strptime(trim_date2,'%Y%m%d')


     # Setup for the query for the start data criteria   
    sel = [Measurement.date, 
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs), 
        func.max(Measurement.tobs)]

    temp_search2 = session.query(*sel).filter(Measurement.date >= real_date).filter(Measurement.date <= real_date2).group_by(Measurement.date).all()
   
    # Close our session
    session.close()

    # Convert list of tuples into normal list
    start_end_temp_results = list(np.ravel(temp_search2))

    return jsonify(start_end_temp_results)

# BOILERPLATE Syntax
if __name__ == '__main__':
    app.run(debug=True)