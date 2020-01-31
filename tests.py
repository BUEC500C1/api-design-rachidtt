import pytest
from airportweather import getWeatherFromCoord


def test_getWeatherFromCoord():
	with pytest.raises(ValueError):
		getWeatherFromCoord(100,50)

	with pytest.raises(ValueError):
		getWeatherFromCoord(10,500)


