import csv
import requests #for gets
from keys import KEY #gets openweathermap api key

class airport:
	id = 000
	name = 'name'
	lati = 0
	longi = 0

airportList = []





def getWeatherFromCoord(Lat,Long,apikey):
	address = 'http://api.openweathermap.org/data/2.5/weather?lat='
	url = address+Lat+'&lon='+Long+'&appid='+KEY
	json_data= requests.get(url).json()
	formatted_data1 = json_data['weather'][0]['description']
	kelvintemp = json_data['main']['temp']#current temp from current api
	fahrentemp =(kelvintemp-273.15)*(9/5)+32
	return fahrentemp

def CodeToCoord():
	print('x')