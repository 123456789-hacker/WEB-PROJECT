import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

PLIK_PRZEPISY = "przepisy.json"

# Funkcje do obsługi pliku JSON
def wczytaj_przepisy():
    if os.path.exists(PLIK_PRZEPISY):
        with open(PLIK_PRZEPISY, "r", encoding="utf-8") as plik:
            return json.load(plik)
    return {}

def zapisz_przepisy(przepisy):
    with open(PLIK_PRZEPISY, "w", encoding="utf-8") as plik:
        json.dump(przepisy, plik, indent=4, ensure_ascii=False)

# Funkcja dodawania przepisu
def dodaj_przepis():
    nazwa = simpledialog.askstring("Dodaj przepis", "Podaj nazwę przepisu:")
    if not nazwa:
        return
    
    skladniki = simpledialog.askstring("Dodaj przepis", "Podaj składniki (oddzielone przecinkami):")
    instrukcje = simpledialog.askstring("Dodaj przepis", "Podaj instrukcje:")
    
    if not skladniki or not instrukcje:
        messagebox.showerror("Błąd", "Musisz podać składniki i instrukcje!")
        return
    
    przepisy = wczytaj_przepisy()
    przepisy[nazwa] = {"składniki": [s.strip() for s in skladniki.split(",")], "instrukcje": instrukcje}
    zapisz_przepisy(przepisy)
    messagebox.showinfo("Sukces", f"Przepis '{nazwa}' został dodany!")
    wyswietl_przepisy()

# Funkcja wyświetlania wszystkich przepisów
def wyswietl_przepisy():
    przepisy = wczytaj_przepisy()
    lista_przepisow.delete(0, tk.END)  # Czyścimy listę
    for nazwa in przepisy:
        lista_przepisow.insert(tk.END, nazwa)

# Funkcja wyszukiwania przepisu
def wyszukaj_przepis():
    nazwa = simpledialog.askstring("Wyszukaj przepis", "Podaj nazwę przepisu:")
    przepisy = wczytaj_przepisy()
    if nazwa in przepisy:
        przepis = przepisy[nazwa]
        messagebox.showinfo(f"Przepis: {nazwa}", f"Składniki: {', '.join(przepis['składniki'])}\n\nInstrukcje: {przepis['instrukcje']}")
    else:
        messagebox.showwarning("Nie znaleziono", f"Przepis '{nazwa}' nie istnieje.")

# Funkcja usuwania przepisu
def usun_przepis():
    nazwa = lista_przepisow.get(tk.ACTIVE)
    if not nazwa:
        messagebox.showwarning("Błąd", "Nie wybrano przepisu!")
        return
    
    przepisy = wczytaj_przepisy()
    if nazwa in przepisy:
        del przepisy[nazwa]
        zapisz_przepisy(przepisy)
        messagebox.showinfo("Sukces", f"Przepis '{nazwa}' został usunięty.")
        wyswietl_przepisy()
    else:
        messagebox.showwarning("Błąd", f"Przepis '{nazwa}' nie istnieje.")

# Tworzenie GUI
root = tk.Tk()
root.title("📖 Przepisy Kulinarne")
root.geometry("400x500")

# Nagłówek
naglowek = tk.Label(root, text="📖 Przepisy Kulinarne", font=("Arial", 16, "bold"))
naglowek.pack(pady=10)

# Lista przepisów
lista_przepisow = tk.Listbox(root, width=50, height=10)
lista_przepisow.pack(pady=10)
wyswietl_przepisy()

# Przyciski
btn_dodaj = tk.Button(root, text="➕ Dodaj Przepis", command=dodaj_przepis)
btn_dodaj.pack(pady=5)

btn_wyszukaj = tk.Button(root, text="🔍 Wyszukaj Przepis", command=wyszukaj_przepis)
btn_wyszukaj.pack(pady=5)

btn_usun = tk.Button(root, text="🗑 Usuń Przepis", command=usun_przepis)
btn_usun.pack(pady=5)

btn_wyjdz = tk.Button(root, text="❌ Wyjście", command=root.quit)
btn_wyjdz.pack(pady=10)

# Uruchomienie aplikacji
root.mainloop()