import sys
from math import pi

a = "haslo"
inp = input("Wpisz hasło: ")

if a == inp:
    print("Gratulacje, hasło jest poprawne")
    b = float(input("Wybierz, co chcesz obliczyć: \n(1) kwadratu \n(2) prostokątu \n(3) trójkąta \n(4) rombu\n(5) koła \n(6) wyłączyć aplikację: "))
else:
    print("Hasło jest złe!")

if b == 1:
    kw = float(input("Podaj bok kwadratu: "))
    print(f"Pole wynosi {kw*kw}")
elif b == 2:
    pr = float(input("Podaj pierwszy bok prostokąta: "))
    pr2 = float(input("Podaj drugi bok prostokąta: "))
    print(f"Pole wynosi {pr*pr2}")
elif b == 3:
    tr = float(input("Podaj podstawę: "))
    tr2 = float(input("Podaj wysokość: "))
    print(f"Pole wynosi {tr * tr2 / 2}")
elif b == 4:
    rb = float(input("Podaj pierwszą przekątną: "))
    rb2 = float(input("Podaj drugą przekątną: "))
    print(f"Pole wynosi {rb * rb2 / 2}")
elif b == 5:
    ko = float(input("Podaj promień: "))
    print(f"Pole wynosi {pi * ko * ko }")
elif b == 6:
    sys.exit()
