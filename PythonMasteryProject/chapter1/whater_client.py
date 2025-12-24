# modules and global variables
from abc import ABC ,abstractmethod
import requests

# abstract class
class WeatherAbstract(ABC):
    
    @abstractmethod
    def get_current_weather(self,lat,lon):
        pass
        
    
    
    
    
#openweather class
class OpenWeatherProvider(WeatherAbstract):
    base_url = "https://pro.openweathermap.org/data/2.5/forecast/climate?lat={lat}&lon={lon}&appid={API key}"
    
    def __init__(self,api_key):
        self.api_key = api_key
    def get_current_weather(self, lat, lon):
        params = { 
            "latitude" : lat,
            "longitude" : lon,
            "appid" : self.api_key
        }
        response = requests.get(self.base_url,params=params)
        return response.json()


# openmeteo class

class OpenMeteoProvider(WeatherAbstract):
    base_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&current=temperature_2m,relative_humidity_2m"
    
 
    def get_current_weather(self, lat, lon):
        params = { 
            "latitude" : lat,
            "longitude" : lon,
            "current" : "temperature_2m,relative_humidity_2m"
        }
        response = requests.get(self.base_url,params=params)
        normalize_data = response.json()
        return normalize_data

 
# running the applications
# provider = OpenMeteoProvider()
provider = OpenWeatherProvider("e3c1ec36065ae95f26fb9eaa746165b3")
print(provider.get_current_weather(lat= 36.712795 , lon= 52.667686))


