from keys import KEY
from airportweather import *


'''
Lat='40'
Long='74'
temp,conditions = getWeatherFromCoord(Lat,Long)

latitude, longitude = CodeToCoord('00A')
#print(latitude)
#print(longitude)
#print(conditions)

temp_arr = []
conditions_arr =[]
temp_arr,conditions_arr = getPastWeather(Lat,Long)
#print(temp_arr)
#print(conditions_arr)
#print(temp)
#plotData(temp_arr,conditions_arr)'''

'''
fahrentemp=getAirportWeather('00A')
print(fahrentemp)
'''

fahrentemp=getAirportWeather('00A')
conditions=getAirportConditions('00A')
print(fahrentemp)
print(conditions)
