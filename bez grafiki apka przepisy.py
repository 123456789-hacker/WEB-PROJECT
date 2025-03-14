import json
import os

PLIK_PRZEPISY = "przepisy.json"

def wczytaj_przepisy():
    if os.path.exists(PLIK_PRZEPISY):
        with open(PLIK_PRZEPISY, "r", encoding="utf-8") as plik:
            return json.load(plik)
    return {}

def zapisz_przepisy(przepisy):
    with open(PLIK_PRZEPISY, "w", encoding="utf-8") as plik:
        json.dump(przepisy, plik, indent=4, ensure_ascii=False)

def dodaj_przepis():
    nazwa = input("Podaj nazwę przepisu: ")
    skladniki = input("Podaj składniki (oddzielone przecinkami): ").split(",")
    instrukcje = input("Podaj instrukcje: ")

    przepisy = wczytaj_przepisy()
    przepisy[nazwa] = {"składniki": [s.strip() for s in skladniki], "instrukcje": instrukcje}
    zapisz_przepisy(przepisy)
    print(f"Przepis '{nazwa}' został dodany!")

def wyswietl_przepisy():
    przepisy = wczytaj_przepisy()
    if not przepisy:
        print("Brak zapisanych przepisów.")
        return
    for nazwa, dane in przepisy.items():
        print(f"\n📌 {nazwa}\nSkładniki: {', '.join(dane['składniki'])}\nInstrukcje: {dane['instrukcje']}")

def wyszukaj_przepis():
    nazwa = input("Podaj nazwę przepisu do wyszukania: ")
    przepisy = wczytaj_przepisy()
    if nazwa in przepisy:
        dane = przepisy[nazwa]
        print(f"\n📌 {nazwa}\nSkładniki: {', '.join(dane['składniki'])}\nInstrukcje: {dane['instrukcje']}")
    else:
        print(f"Przepis '{nazwa}' nie został znaleziony.")

def usun_przepis():
    nazwa = input("Podaj nazwę przepisu do usunięcia: ")
    przepisy = wczytaj_przepisy()
    if nazwa in przepisy:
        del przepisy[nazwa]
        zapisz_przepisy(przepisy)
        print(f"Przepis '{nazwa}' został usunięty.")
    else:
        print(f"Nie znaleziono przepisu o nazwie '{nazwa}'.")

def menu():
    while True:
        print("\n📖 MENU")
        print("1. Dodaj przepis")
        print("2. Wyświetl wszystkie przepisy")
        print("3. Wyszukaj przepis")
        print("4. Usuń przepis")
        print("5. Wyjście")
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            dodaj_przepis()
        elif wybor == "2":
            wyswietl_przepisy()
        elif wybor == "3":
            wyszukaj_przepis()
        elif wybor == "4":
            usun_przepis()
        elif wybor == "5":
            print("Zamykanie programu...")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    menu()
