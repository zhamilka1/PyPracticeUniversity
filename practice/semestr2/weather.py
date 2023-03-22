import urllib.request as getWeather
import json
def getWeatherInCity(city = "Moscow"):
    data = getWeather.urlopen(configureUrl(city)).read().decode()
    return data

def configureUrl(city):
    baseUrl = 'https://api.openweathermap.org/data/2.5/weather?'
    units = 'metric'
    language = 'ru'
    appId = 'c341e34f9b7c327502cde34aa7817c5f'
    result = baseUrl + makeParams('q', city) + makeParams('units', units) + makeParams('lang', language) + makeParams('appId', appId)
    return result

def makeParams(keyName, data):
    result = str('&'+keyName+'='+data)
    return result


def createLog(weather):
    file = open('logs.txt', encoding="UTF-8", mode="w")
    file.write(str(f"Temp:{weather['main']['temp']},{weather['weather'][0]['description']} Vlaga:{weather['main']['humidity']} Wind speed: {weather['wind']['speed']} Pressure: {weather['main']['pressure']}"))

weather = json.loads(getWeatherInCity())
print(f" Temp:{weather['main']['temp']},{weather['weather'][0]['description']} Vlaga:{weather['main']['humidity']} Wind speed: {weather['wind']['speed']} Pressure: {weather['main']['pressure']}")
createLog(weather)