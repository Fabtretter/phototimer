from datetime import datetime

import requests


class exposureCalc:

	def get_exposure(self, sunrise, sunset, time):
		if(time >=self.sunrise and time <=self.sunset):
			return 'auto'
		return 'night'
		
	#One hour either side of sunrise/set
	def take_shot(self, sunrise, sunset, time):
		if (time >= sunrise and time <= sunset):
			return True
		return False

	def isBetweenSunriseAndSunset(time):
		r = requests.get('https://api.sunrise-sunset.org/json?lat=48.26667&lng=12.41667&formatted=0')
		data = r.json()

		results = data["results"]
		sunrise = results["civil_twilight_begin"]
		sunset = results["civil_twilight_end"]

		sunrisetime = datetime.fromisoformat(sunrise)
		sunsettime = datetime.fromisoformat(sunset)

		return sunrisetime < time < sunsettime
