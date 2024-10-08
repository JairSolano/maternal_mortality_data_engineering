# Import dependencies
import numpy as np
import psycopg2
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify



# Connection between sqlalchemy and postgresql
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/maternal_mortality')
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# References to tables
Dates = Base.classes.dates
Black = Base.classes.black
Asian = Base.classes.asian
Pacific_Islander = Base.classes.pacific_islander
Hispanic = Base.classes.hispanic
Native_Indian = Base.classes.native_indian
White = Base.classes.white


# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################




# 'Homepage': Shows the possible routes
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/dates<br/>"
        f"/api/v1.0/black<br/>"
        f"/api/v1.0/hispanic<br/>"
        f"/api/v1.0/native-indian<br/>"
        f"/api/v1.0/asian<br/>"
        f"/api/v1.0/pacific-islander<br/>"
        f"/api/v1.0/white<br/>"
        f"/api/v1.0/aggregate<br/>"
    )



# Displays all the dates of the data and their corresponding indices
@app.route("/api/v1.0/dates")
def dates():

    date_data = session.query(Dates.date_m).all()
    session.close()

    dates_dict = []
    for result in date_data:
        result_dict = {}
        result_dict["Date"] = result[0]
        dates_dict.append(result_dict)

    return jsonify(dates_dict)




# Displays the data on Black maternal mortality extracted from the SQL database
@app.route("/api/v1.0/black")
def blackData():

    black_data = session.query(Dates.date_m, Black.maternal_deaths, Black.live_births, Black.maternal_mortality_rate).where(Dates.date_index == Black.date_index).order_by(Dates.date_m).all()
    session.close()

    black_dict = []
    for result in black_data:
        result_dict = {}
        result_dict["Date"] = result[0]
        result_dict["Maternal Deaths"] = result[1]
        result_dict["Live Births"] = result[2]
        result_dict["Maternal Mortality Rate"] = result[3]
        black_dict.append(result_dict)
        
    return jsonify(black_dict)




# Displays the data on Hispanic maternal mortality extracted from the SQL database
@app.route("/api/v1.0/hispanic")
def hispanicData():

    hispanic_data = session.query(Dates.date_m, Hispanic.maternal_deaths, Hispanic.live_births, Hispanic.maternal_mortality_rate).where(Dates.date_index == Hispanic.date_index).order_by(Dates.date_m).all()
    session.close()

    # List of dictionaries with each dictionary corresponding to a row of data
    hispanic_dict = []
    for result in hispanic_data:
        result_dict = {}
        result_dict["Date"] = result[0]
        result_dict["Maternal Deaths"] = result[1]
        result_dict["Live Births"] = result[2]
        result_dict["Maternal Mortality Rate"] = result[3]
        hispanic_dict.append(result_dict)

    return jsonify(hispanic_dict)




# Displays the data on Native-Indian (Native-American) maternal mortality extracted from the SQL database
@app.route("/api/v1.0/native-indian")
def native_indian_Data():

    native_data = session.query(Dates.date_m, Native_Indian.maternal_deaths, Native_Indian.live_births, Native_Indian.maternal_mortality_rate).where(Dates.date_index == Native_Indian.date_index).order_by(Dates.date_m).all()
    session.close()

    # List of dictionaries with each dictionary corresponding to a row of data
    native_dict = []
    for result in native_data:
        result_dict = {}
        result_dict["Date"] = result[0]
        result_dict["Maternal Deaths"] = result[1]
        result_dict["Live Births"] = result[2]
        result_dict["Maternal Mortality Rate"] = result[3]
        native_dict.append(result_dict)

    return jsonify(native_dict)




# Displays the data on Asian maternal mortality extracted from the SQL database
@app.route("/api/v1.0/asian")
def asianData():

    asian_data = session.query(Dates.date_m, Asian.maternal_deaths, Asian.live_births, Asian.maternal_mortality_rate).where(Dates.date_index == Asian.date_index).order_by(Dates.date_m).all()
    session.close()

    # List of dictionaries with each dictionary corresponding to a row of data
    asian_dict = []
    for result in asian_data:
        result_dict = {}
        result_dict["Date"] = result[0]
        result_dict["Maternal Deaths"] = result[1]
        result_dict["Live Births"] = result[2]
        result_dict["Maternal Mortality Rate"] = result[3]
        asian_dict.append(result_dict)

    return jsonify(asian_dict)





# Displays the data on Pacific-Islander maternal mortality extracted from the SQL database
@app.route("/api/v1.0/pacific-islander")
def pacificData():

    pacific_data = session.query(Dates.date_m, Pacific_Islander.maternal_deaths, Pacific_Islander.live_births, Pacific_Islander.maternal_mortality_rate).where(Dates.date_index == Pacific_Islander.date_index).order_by(Dates.date_m).all() 
    session.close()

    pacific_dict = []
    for result in pacific_data:
        result_dict = {}
        result_dict["Date"] = result[0]
        result_dict["Maternal Deaths"] = result[1]
        result_dict["Live Births"] = result[2]
        result_dict["Maternal Mortality Rate"] = result[3]
        pacific_dict.append(result_dict)

    return jsonify(pacific_dict)



# Displays the data on White maternal mortality extracted from the SQL database
@app.route("/api/v1.0/white")
def whiteData():

    white_data = session.query(Dates.date_m, White.maternal_deaths, White.live_births, White.maternal_mortality_rate).where(Dates.date_index == White.date_index).order_by(Dates.date_m).all()
    session.close()

    white_dict = []
    for result in white_data:
        result_dict = {}
        result_dict["Date"] = result[0]
        result_dict["Maternal Deaths"] = result[1]
        result_dict["Live Births"] = result[2]
        result_dict["Maternal Mortality Rate"] = result[3]
        white_dict.append(result_dict)

    return jsonify(white_dict)




# Displays the mean maternal mortality rates of each racial group
@app.route("/api/v1.0/aggregate")
def aggregate():

    black_avg = session.query(func.avg(Black.maternal_mortality_rate)).first()
    hispanic_avg = session.query(func.avg(Hispanic.maternal_mortality_rate)).first()
    native_american_avg = session.query(func.avg(Native_Indian.maternal_mortality_rate)).first()
    asian_avg = session.query(func.avg(Asian.maternal_mortality_rate)).first()
    pacific_avg = session.query(func.avg(Pacific_Islander.maternal_mortality_rate)).first()
    white_avg = session.query(func.avg(White.maternal_mortality_rate)).first()
                    
    session.close()

    aggregate_dict = {}
    aggregate_dict["Average Black Maternal Mortality Rate"] = black_avg[0]
    aggregate_dict["Average Hispanic Maternal Mortality Rate"] = hispanic_avg[0]
    aggregate_dict["Average Native American Maternal Mortality Rate"] = native_american_avg[0]
    aggregate_dict["Average Asian Maternal Mortality Rate"] = asian_avg[0]
    aggregate_dict["Average Pacific Islander Maternal Mortality Rate"] = pacific_avg[0]
    aggregate_dict["Average White Maternal Mortality Rate"] = white_avg[0]

    return jsonify(aggregate_dict)




if __name__ == '__main__':
    app.run(debug=True)
