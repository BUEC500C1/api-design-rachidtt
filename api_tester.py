#Example of how to use the API:
from airportweather import *


myAirport = '00A'

fahrentemp=getAirportWeather(myAirport) #get current temperature of airport
conditions=getAirportConditions(myAirport) #get current conditions of airport
print(fahrentemp,conditions)

temperatures_arr, conditions_arr = getPastData(myAirport,True)#plots temperature of the past 12 hours, also returns temperature and conditions of past 12h 

