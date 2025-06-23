import requests
def currency_update():
    url = "https://v6.exchangerate-api.com/v6/27b32ba567b7b5e366ca4809/latest/USD"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            Rs = data['conversion_rates']['PKR']
            dubai = data['conversion_rates']['AED']
            Euro = data['conversion_rates']['EUR']
            Japan = data['conversion_rates']['JPY']
            chinese = data['conversion_rates']['CNY']
            indian = data['conversion_rates']['INR']

            print(Rs)
        else:
            print("status code failed",response.status_code)
    except Exception as e:
        print(e)
    
currency_update()



