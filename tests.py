import pytest
from airportweather import *


def test_getWeatherFromCoord_lat():
	with pytest.raises(ValueError):
		getWeatherFromCoord('100','50')

def test_getWeatherFromCoord_long():
	with pytest.raises(ValueError):
		getWeatherFromCoord('10','500')

def test_getWeatherFromCoord_string():
	assert getWeatherFromCoord('a','z')==False

def test_getPastWeatherCoord_lat():
	with pytest.raises(ValueError):
		getPastWeather('100','50')

def test_getPastWeather_long():
	with pytest.raises(ValueError):
		getPastWeather('10','500')

def test_getPastWeather_string():
	assert getPastWeather('a','z')==False

def test_CodeToCoord():
	latitude,longitude = CodeToCoord('90MO')
	assert latitude =='38.389198303222656'
	assert longitude =='-93.76799774169922'

	with pytest.raises(KeyError):
		CodeToCoord('randomcode')