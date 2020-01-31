from keys import KEY
from airportweather import getWeatherFromCoord,CodeToCoord




Lat='40'
Long='74'
zz = getWeatherFromCoord(Lat,Long)

latitude, longitude = CodeToCoord('randomcode')
print(latitude)
print(longitude)