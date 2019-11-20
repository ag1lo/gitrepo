#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sumuj_liczby():
    """
    Funkcja pobiera liczby od użytkownika, dopóki ich suma nie przekroczy wartości 75. Na koniec drukuje sumę liczb.
    """
    
    suma=0
    while suma<75:
        liczba1 = int(input("Podaj liczbę: "))
        liczba2 = int(input("Podaj liczbę: "))
        suma=suma+liczba1+liczba2
    
    print(suma)


def main(args):
    sumuj_liczby()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
