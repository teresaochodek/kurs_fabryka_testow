import requests
import datetime
import time


while True:
    start = datetime.datetime.now()
    try:
        currency = {'base': 'EUR', 'symbols': 'PLN'}
        r = requests.get('https://api.ratesapi.io/api/latest', params=currency)
        duration = datetime.datetime.now() - start
        data = r.json()
        rate = data['rates']['PLN']
    except:
        rate = None
        duration = datetime.datetime.now() - start

    print("------------------------------------------")
    if rate is None:
        print("Błąd pozyskiwania danych")
    else:
        print('Kurs Euro:', rate)
    print('Data i godzina:', str(start))
    print('Czas wykonania zapytania:', str(duration.microseconds/1000) + 'ms')

    time.sleep(15)

