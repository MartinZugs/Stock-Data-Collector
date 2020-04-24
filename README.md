# Stock-Data-Scraper
This is a Docker file that is run using kubernetes on my raspbery pis that utilizes the World Trading Data API to pull data down for given stocks and pushes that data to a Python Flask API that I built that adds the data to a MySQL server database located on another one of my Raspberry Pis.

### Commands to run

`sudo docker build . -t code && sudo docker run code <insert-ticker-symbol-here> <insert-api-token-here>`

### Commands to delete all Docker containers

`sudo docker stop $(sudo docker ps -a -q) && sudo docker rm $(sudo docker ps -a -q)`
