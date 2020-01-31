import csv
import requests #for gets
#from keys import KEY  #gets openweathermap api key
KEY = '813e77b87c63fbeb6328993f99b3f844'

class airport:
	id = 000
	name = 'name'
	lati = 0
	longi = 0

	def __init__(self, var1, var2, var3, var4):
		self.id = var1
		self.lati = var2
		self.longi = var3
		self.name = var4

airportList = []
with open('airports.csv', 'r', encoding='utf-8') as f:
	reader = csv.reader(f)
	firstrow=next(reader) #get to second row to skip row names
	for row in reader:
		airportList.append(airport(row[1], row[4], row[5],row[3]))



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

	address = 'http://api.openweathermap.org/data/2.5/weather?lat='
	url = address+Lat+'&lon='+Long+'&appid='+KEY
	json_data= requests.get(url).json()
	formatted_data1 = json_data['weather'][0]['description']
	kelvintemp = json_data['main']['temp']#current temp from current api
	fahrentemp =(kelvintemp-273.15)*(9/5)+32
	return fahrentemp



def CodeToCoord(code):
	for i in airportList:
		if(i.id==code):
			return i.lati, i.longi
	raise KeyError('Entered code not in airport list')		


