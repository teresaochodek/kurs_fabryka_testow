import requests
import datetime
import time
import json


# napisz funkcje, która uderza w endpoint
# r = requests.get('https://api.ratesapi.io/api/latest?base=EUR&symbols=PLN')


currency = {'base': 'EUR' , 'symbols': 'PLN'}
r = requests.get('https://api.ratesapi.io/api/latest' , params=currency)
#time.sleep(1)
# r = requests.get('https://api.ratesapi.io/api')
data = r.json()
rate = data['rates']['PLN']
date = r.json()
#date = datetime.now()
date = date['date']
start = datetime.datetime.now()
duration = datetime.datetime.now() - start

# zabezpieczenie przed bledem
# mierzenie czasu trwania zapytania i date zapytania oraz wypisac na ekran

# petla z interwalem 15 s

#print(r.url)
#print(r.text)
print('Kurs Euro:' ,  data['rates']['PLN'])
print('Data i godzina:' , str(start))
print('Czas wykonania zapytania:' , str(duration.microseconds)  + 'ms')

