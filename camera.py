from datetime import datetime

import fileutils


class exposureCalc:

	def get_exposure(self, sunrise, sunset, time):
		if (time >= sunrise and time <= sunset):
			return 'auto'
		return 'night'
		
	#One hour either side of sunrise/set
	def take_shot(self, sunrise, sunset, time):
		if (time >= sunrise and time <= sunset):
			return True
		return False

	def isBetweenSunriseAndSunset(time):

		with open(fileutils.getConfigFileName(time), "r") as twilightConfig:
			data = twilightConfig.readlines()

		sunrise = data["civil_twilight_begin"]
		sunset = data["civil_twilight_end"]

		sunrise_time = datetime.fromisoformat(sunrise)
		sunset_time = datetime.fromisoformat(sunset)

		return sunrise_time < time < sunset_time
