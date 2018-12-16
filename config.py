##############Camera settings##############
config = {}
config["flip_horizontal"] = False
config["flip_vertical"] = False
config["metering_mode"] = "matrix"

config["base_path"] = "./pictures"
config["height"] = 1536
config["width"] = 2048
config["quality"] = 35

##############Time settings##############

# possible values are: twilight, always, config
# Always: dont check for times at all, just shoot a picture
# Twilight: use twilight times from your config folder. Make a picture if current time is between sunrise and sunset.
# Config: use "am" and "pm" from the configuration
config["mode"] = "twilight"

config["am"] = 400
config["pm"] = 2000

config["twilight_times_path"] = "twiligth_times"
# possible values are: always, never, config.
# Always: no twilight file found => take a picture anyway
# Never: no twilight file found => dont take a picture
# Config: no twilight file found => use "am" and "pm"
config["twilight_fallback_mode"] = "always"

# possible values are: sunrisesunset
# SunriseSunset: use: https://sunrise-sunset.org/api and corresponding config generator
config["init_config_mode"] = "sunrisesunset"
