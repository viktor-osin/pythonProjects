import pyowm

owm = pyowm.OWM('API....', language='ru') 

place = input("В каком городе, стране:")

observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]
print("В городе " + place + " сейчас: " + w.get_detailed_status())       
print("Температура: "+ str(temp))      