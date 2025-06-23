import requests


def weather_update(API_KEY, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    try:
        
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            loca = data['location']['name']
            resion = data['location']['region']
            temp = data['current']['temp_c']
            wind = data['current']['wind_kph']
            humidity = data['current']['humidity']
            feel = data['current']['feelslike_c']
            cloud = data['current']['cloud']
            print(loca)
            print(resion)
            print(temp)
            print(wind)
            print(humidity)
            print(feel)
            print(cloud)
        else:
            print("status_code failed",response.status_code)
    except Exception as e:
        print(e)

API_KEY = '6cb4a793abe5469d945133309251406' 
city = input("enter a city")
weather_update(API_KEY, city)