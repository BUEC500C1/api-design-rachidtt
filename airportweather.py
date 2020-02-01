import csv
import requests #for gets
import time
import matplotlib.pyplot as plt
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
		float(Lat)
	except ValueError:
		return False

	try:
		float(Long)
	except ValueError:
		return False

	if ( (float)(Lat)>90 or (float)(Lat)<-90) or ( (float)(Long)<-180 or (float)(Long)>80 ) :
		raise ValueError('Latitude should be between -90 and 90, Longitude should be between -180 and 80')

	address = 'http://api.openweathermap.org/data/2.5/weather?lat='
	url = address+Lat+'&lon='+Long+'&appid='+KEY
	json_data= requests.get(url).json()
	kelvintemp = json_data['main']['temp']#current temp from current api
	conditions = json_data['weather'][0]['description']
	fahrentemp =(kelvintemp-273.15)*(9/5)+32
	return fahrentemp,conditions



def getPastWeather(Lat,Long):
	try:
		float(Lat)
	except ValueError:
		return False

	try:
		float(Long)
	except ValueError:
		return False

	if ( (float)(Lat)>90 or (float)(Lat)<-90) or ( (float)(Long)<-180 or (float)(Long)>80 ) :
		raise ValueError('Latitude should be between -90 and 90, Longitude should be between -180 and 80')

	epoch_time = int(time.time()) #current time
	epoch_time = epoch_time -(12*3600) #time 12h ago
	address = 'https://api.darksky.net/forecast/db56554ec429849dbbb84af695d39f93/'
	url = address+str(Lat)+','+str(Long)+','+str(epoch_time)+'?exclude=currently,flags,minutely,daily'
	json_data= requests.get(url).json()
	temperatures_arr= []
	conditions_arr = []
	for i in range(12):
		temp = json_data['hourly']['data'][12+i]['temperature']
		temperatures_arr.append(temp)
		conditions = json_data['hourly']['data'][12+i]['summary']
		conditions_arr.append(conditions)

	return temperatures_arr, conditions_arr



def CodeToCoord(code):
	for i in airportList:
		if(i.id==code):
			return i.lati, i.longi
	raise KeyError('Entered code not in airport list')		



def plotData(temperatures_arr,conditions_arr):
	x=range(1,13)#from 1 to 12
	x=x[::-1]#reverse so from 12 to 1
	plt.scatter(x,temperatures_arr,color='r')
	plt.xlabel('hours ago')
	plt.ylabel('temperature (in fahreinheit)')
	plt.title('Past 12h weather history')
	plt.show()
	return


def getAirportWeather(code):
	Lat,Long = CodeToCoord(code)
	fahrentemp, conditions = getWeatherFromCoord(Lat,Long)
	return fahrentemp

def getAirportConditions(code):
	Lat,Long = CodeToCoord(code)
	fahrentemp, conditions = getWeatherFromCoord(Lat,Long)
	return conditions


def getPastData(code,Plotbool):
	Lat,Long = CodeToCoord(code)
	temperatures_arr, conditions_arr = getPastWeather(Lat,Long)
	if(Plotbool):
		plotData(temperatures_arr,conditions_arr)
	return temperatures_arr, conditions_arr