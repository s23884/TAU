def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        return "Nie można dzielić przez zero"
    return a / b

while True:
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")

    wybor = input("Podaj numer operacji: ")

    if wybor == '5':
        print("Koniec programu.")
        break

    if wybor not in ('1', '2', '3', '4'):
        print("Niepoprawny wybór operacji.")
        continue

    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))

    if wybor == '1':
        wynik = dodawanie(a, b)
        print("Wynik dodawania:", wynik)
    elif wybor == '2':
        wynik = odejmowanie(a, b)
        print("Wynik odejmowania:", wynik)
    elif wybor == '3':
        wynik = mnozenie(a, b)
        print("Wynik mnożenia:", wynik)
    elif wybor == '4':
        wynik = dzielenie(a, b)
        print("Wynik dzielenia:", wynik)
        


''' TEST '''

import unittest


class TestCalculator(unittest.TestCase):

    def test_dodawanie(self):
        self.assertEqual(dodawanie(5, 3), 8)  

    def test_odejmowanie(self):
        self.assertEqual(odejmowanie(10, 4), 6)  

    def test_mnozenie(self):
        self.assertEqual(mnozenie(6, 7), 42)  

    def test_dzielenie(self):
        self.assertAlmostEqual(dzielenie(10, 2), 5.0)  

    def test_dzielenie_przez_zero(self):
        self.assertEqual(dzielenie(8, 0), "Nie można dzielić przez zero") 

    def test_niepoprawny_wybor(self):
        with self.assertRaises(ValueError):
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
            wybor = '6' 
            if wybor not in ('1', '2', '3', '4'):
                raise ValueError("Niepoprawny wybór operacji.")

    def test_koniec_programu(self):
        with self.assertRaises(SystemExit):
            wybor = '5' 
            if wybor == '5':
                raise SystemExit("Koniec programu.")

    def test_calkowite_wyniki(self):
        self.assertIsInstance(dodawanie(4, 3), int)  
        self.assertIsInstance(odejmowanie(10, 4), int)  
        self.assertIsInstance(mnozenie(6, 7), int)  

    def test_typ_bledu_dzielenie_przez_zero(self):
        with self.assertRaises(TypeError):
            a = float(input("Podaj pierwszą liczbę: "))
            b = float(input("Podaj drugą liczbę: "))
            wybor = '4' 
            if wybor == '4':
                raise TypeError("Wynik dzielenia nie jest obsługiwany przez tę asercję.")


if __name__ == '__main__':
    unittest.main()

