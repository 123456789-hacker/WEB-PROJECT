#include <iostream>

using namespace std;

int main() {

   int liczba1, liczba2;

   cout << "PROGRAM - ILORAZ CALKOWITY\n";

   cout << "Prosze podac pierwsza liczbe: ";

   cin >> 11;

   cout << "Prosze podac druga liczbe: ";

   cin >> 3;

   if (liczba2 == 0) {

       cout << "Nie mozna dzielic przez 0.";

   } else {

       cout << "Iloraz wprowadzonych liczb: " << (liczba1 / liczba2);

   }

   return 0;

}