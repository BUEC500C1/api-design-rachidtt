import csv
import requests #for gets
#from keys import KEY  #gets openweathermap api key
KEY = '813e77b87c63fbeb6328993f99b3f844'

class airport:
	id = 000
	name = 'name'
	lati = 0
	longi = 0

airportList = []





def getWeatherFromCoord(Lat,Long):
	try:
		int(Lat)
	except ValueError:
		return False

	try:
		int(Long)
	except ValueError:
		return False

	if ( (int)(Lat)>90 or (int)(Lat)<-90) or ( (int)(Long)<-180 or (int)(Long)>80 ) :
		raise ValueError('Latitude should be between -90 and 90, Longitude should be between -180 and 80')


	#check correct Lat
	#check correct Long
	address = 'http://api.openweathermap.org/data/2.5/weather?lat='
	url = address+Lat+'&lon='+Long+'&appid='+KEY
	json_data= requests.get(url).json()
	formatted_data1 = json_data['weather'][0]['description']
	kelvintemp = json_data['main']['temp']#current temp from current api
	fahrentemp =(kelvintemp-273.15)*(9/5)+32
	return fahrentemp

def CodeToCoord():
	print('x')