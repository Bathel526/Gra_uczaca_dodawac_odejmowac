from random import choice
import sys

def generate_question():
    while True:
        liczby_1 = range(6, 11)

        liczba_1 = choice(liczby_1)
        liczba_2 = choice(liczby_1)
        dzialania = ('+', '-')
        dzialanie = choice(dzialania)

        if dzialanie == '-' and liczba_1 >= liczba_2:
            wynik = liczba_1 - liczba_2
            break
        elif dzialanie == '+':
            wynik = liczba_1 + liczba_2
            break
        else:
            continue
    return liczba_1, liczba_2, dzialanie, wynik

def get_zuza_answer(liczba_1, liczba_2, dzialanie):
    while True:
        prompt = f"Podaj wynik działania {liczba_1}{dzialanie}{liczba_2}:\n"
        wynik_zuzy = input(prompt)
        if wynik_zuzy == 'q':
            sys.exit()
        else:
            try:
                wynik_zuzy = int(wynik_zuzy)
            except ValueError:
                print("Musisz wpisac liczbe !!!")
                continue
            else:
                return wynik_zuzy

def run_quiz():
    points = 0
    attempts = 10

    print('Jezeli chcesz wyjsc nacisnij: "q" i "ENTER"\n')
    for attempt in range(attempts):
        print(f"Zadanie {attempt+1}.")

        liczba_1, liczba_2, dzialanie, wynik = generate_question()
        user_answer = get_zuza_answer(liczba_1, liczba_2, dzialanie)

        if user_answer == wynik:
            points += 1

    print(f"Twoj wynik to {points}/{attempts}")

run_quiz()