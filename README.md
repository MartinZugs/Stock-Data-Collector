# Stock Data Collector
This is a Docker file that is orchestrated using kubernetes that runs a Python script on my raspbery pi. This script utilizes the World Trading Data API to pull data for given stocks and clean, organzie, and push that data to a Python Flask API running on another one of my raspberry pis that adds the data to a MySQL database located on that pi.
