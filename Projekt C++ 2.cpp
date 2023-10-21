#include <iostream>
using namespace std;
int main() {
int surname, name;
cout << "Prosze podac z ilu liter skada sie nazwisko";
cin >> surname;
cout << surname * surname << endl; // mnozenie - gwiazdka - asterisk  
cout << "Prosze podac z ilu liter sklda sie imie.: ";
cin >> name;
if (name - surname) {
    cout << name  - surname << endl;
}
return 0;
}
