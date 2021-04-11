print("witaj w kalkulatorze")
a = int(input('podaj pierwsza liczbe: '))
b = int(input('podaj druga liczbe: '))
c = int(input('wybierz rodzaj działania: 1 - dodawanie, 2 - odejmowanie, 3 - mnożenie, 4 - dzielenie: '))
if (c == 1):
    wynik = a + b
elif (c == 2):
    wynik = a - b
elif (c == 3):
    wynik = a * b
elif (c == 4):
    wynik = a / b
else:
    print('zly wybor')
print('wynik działania to: ', wynik)
