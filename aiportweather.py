import csv
import requests #for gets

class airport:
	id = 000
	name = 'name'
	lati = 0
	longi = 0

airportList = []





def getWeatherFromCoord(lat,long,apikey):
	address = 'http://api.openweathermap.org/data/2.5/weather?lat=40&lon=-74&appid=813e77b87c63fbeb6328993f99b3f844'

	address = 'http://api.openweathermap.org/data/2.5/weather?lat='
	url = address+Lat+'&lon='+Long+'&appid='+apikey

