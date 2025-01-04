#Import requests to obtain api's website. I used weatherapi for this program
import requests
from plyer import notification

API_KEY = 'API_KEY' #replace API_KEY with your given API key

#Create a function with the city's name as a parameter
def get_weather(city):
    
    #Use forecast.json for url. Use current.json for current weather
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}"
    
    #Gets the data through the url using the imported requests
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        #Extract data
        forecast_day = data['forecast']['forecastday'][0]
        
        #Extracts forecast
        day_forecast = forecast_day['day']
        day_temp_c = day_forecast['avgtemp_c']
        day_temp_f = day_forecast['avgtemp_f']
        day_condition = day_forecast['condition']['text']
        day_precip = day_forecast['daily_chance_of_rain']
        night_temp_f = day_forecast['mintemp_f']
        
       
        #Prepares a notification message
        message = (f"City: {city}\n"
                   f"Daytime: {day_temp_f}°F, Nighttime: {night_temp_f}°F\n"
                   f"Condition: {day_condition}\n"
                   f"Chance of Precipitation: {day_precip}%\n\n"
                   )

        #Displays the notification
        notification.notify(
            title=f"Weather Update: {city}",
            message=message,
            timeout=10 
        )
    else:
        print(f"Error fetching data from API. Status code: {response.status_code}")




#Example usage:
#get_weather("New York")
