# API Design

For all USA Airports, Develop an API and module where we can get current conditions for the airport asked by the API and we can get current weather graphs (for example, the temperature for the last 24 hours) for specific period.  It does not have to be graphs but the data needed.
 -Use CB and CI
 -Develop examples using your API


 Deadline for completion of this project is February 5th, 2020. 
---------------
## Overview

The API allows you to get current and past weather conditions by entering the Airport Code (Present in airports.csv)


### Requirements

-airports.csv
-airportweather.py
-matplotlib
-requests

### Features

getAirportWeather(code)
getAirportConditions(code)
getPastData(code,Plotbool)

### Instructions 

Install requirements:
```
pip install -r requirements.txt
```

Include the module airportweather.py where you want to call the API:

```
from airportweather import *
```

Make calls to the api:

```
#example
myAirport = '00A'
fahrentemp=getAirportWeather(myAirport) 
conditions=getAirportConditions(myAirport)
temperatures_arr, conditions_arr = getPastData(myAirport,True)
```

GetAirportWeather returns the current temperature in Fahrenheit, of the airport given the Code
GetAirportWeather returns the current description of the condition in Fahrenheit, of the airport given the Code
getPastData returns arrays of past temperatures and conditions of the last 12 hours, and plots the data if you pass True


### Files
- .github/Workflows (CI/CD)
- .gitignore
- README.md (What you are currently reading)
- airports.csv (Contains information about airports such as code, coordinates ...)
- airportweather.py (contains main functions)
- api_tester.py (An example file showing use of API)
- requirements.txt
- tests.py (Tests of the functions in airportweather.py)

## Built With

* [Python]


## Authors

 * **Rachid Tak Tak** - [rachidtt](https://github.com/rachidtt)