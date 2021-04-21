import requests
import datetime
import time


def get_currency_to_pln(currency="EUR"):
    currency = {'base': currency, 'symbols': 'PLN'}
    r = requests.get('https://api.ratesapi.io/api/latest', params=currency)
    data = r.json()
    return data['rates']['PLN']


def get_eur_to_pln_time():
    start = datetime.datetime.now()
    try:
        rate = get_currency_to_pln()
        duration = datetime.datetime.now() - start
    except:
        rate = None
        duration = datetime.datetime.now() - start
    return rate, duration


while True:
    date = datetime.datetime.now()
    rate, duration = get_eur_to_pln_time()

    print("------------------------------------------")
    if rate is None:
        print("Błąd pozyskiwania danych")
    else:
        print('Kurs Euro:',  rate)
    print('Data i godzina:', str(date))
    print('Czas wykonania zapytania:', str(duration.microseconds/1000) + 'ms')

    time.sleep(15)

