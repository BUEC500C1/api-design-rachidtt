import pytest
from airportweather import getWeatherFromCoord


def test_getWeatherFromCoord_lat():
	with pytest.raises(ValueError):
		getWeatherFromCoord('100','50')

def test_getWeatherFromCoord_long():
	with pytest.raises(ValueError):
		getWeatherFromCoord('10','500')
		
def test_getWeatherFromCoord_string():
	assert getWeatherFromCoord('a','z')==False


