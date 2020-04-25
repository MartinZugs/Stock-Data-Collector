# Stock-Data-Scraper
This is a Docker file that is orchestrated using kubernetes that runs a Python script on my raspbery pi. This script utilizes the World Trading Data API to pull data for given stocks and clean, organzie, and push that data to a Python Flask API running on another one of my raspberry pis that adds the data to a MarisDB database located on that pi.

### Commands to run

`sudo docker build . -t code && sudo docker run code <insert-ticker-symbol(s)-here> <insert-api-token-here>`

Example:

`sudo docker build . -t code && sudo docker run code SNAP,TWTR,TSLA hjr7u378hdf89wuii34kjsgho9w`

### Commands to delete all Docker containers

`sudo docker stop $(sudo docker ps -a -q) && sudo docker rm $(sudo docker ps -a -q)`
