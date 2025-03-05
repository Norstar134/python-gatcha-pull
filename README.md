# python-gatcha-pull

## Project Background

Honkai: Star Rail has a poor way of keeping track of how many pulls you're close to pulling a 5 star character. Meaning, if you want to know how many pulls you've had from your previous 5 star, you had to look at your pull history that only shows 5 per page. This is to help keep track of how many pulls you have done and if you lost your 50/50. I also plan to work out the average of pulls it takes overall for each pull.

I also plan on having it read a CSV file that has character information and current limited banners, which will be stored in a database that the user can select the banner of and add their pulls to as well visualising the data using Grafana to work out the average of pulls it takes to get a 5 Star, how often is a 50/50 is lost and when banners are re-ran.

## How to Run the App
The application uses python 3.12 and (eventually) Docker. Please make sure that these are installed on your system.

### Basic Set Up
- Fork or clone this repo onto your PC
- Run either python3 -m venv .venv or py -m venv .venv to create a virtual env
- Activate the venv using either .source .venv/bin/activate or .\venv\Scripts\activate
- Install the requirements using either python3 -m pip install -r requirements.txt or py -m pip install -r requirements.txt