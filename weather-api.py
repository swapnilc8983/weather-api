import requests, json
import datetime 

api_key = "34ccab2ea1e81110b9ce50ce9f53f8e8"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

complete_url = base_url + "appid=" + api_key + "&q=" + 'Pune' 
  

response = requests.get(complete_url) 

data = response.json()

current_date = datetime.datetime.now()

day = int(current_date.strftime("%d"))

# day = 2 Testing 

if day > 1:
   for i in range(2,day):
       if (day % i) == 0:
           print(day,"Date Is Not Prime So No Date")
           break
   else:
       print(day," Date is prime number")
       print(data)
else:
   print(day,"Date Is Not Prime So No Date")