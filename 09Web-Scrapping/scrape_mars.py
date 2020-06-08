from bs4 import BeautifulSoup
import requests
from splinter import Browser
import time 
import pandas as pd
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

app = Flask(__name__)

# Make a connection to Mongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars"
mongo = PyMongo(app)

#create a root route `/`
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


#create a route called `/scrape`
@app.route("/scrape")
def scraper():
    mars = mongo.db.mars
    mars_data = mission_to_mars.scrape_all()
    mars.replace_one({}, mars_data, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)