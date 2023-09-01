#include <iostream>
using namespace std;
//name - ANIA = 4
//surname - BUESCHER = 8
int main()
{

   int name, surname;

    cout << "Proszę podać z ilu liter składa się nazwisko.: ";

   cin >> name;

   cout << "Proszę podać  ilu liter składa się imie.: ";

   cin >> surname;

   {

    cout <<"Suma liter imienia i nazwiska wynosi:";
    cout << name + surname << endl;
   }
   
   {
    cout <<"Różnica między liczbą liter nazwiska a imienia";
    cout << name - surname << endl; // odejmowanie
   }
   {
       cout <<"Iloczyn liczby liter imienia i nazwiska";
       cout << name * surname << endl; // mno¿enie - gwiazdka - asterisk  
   }
   {
       cout <<"Kwadrat liter imienia";
       cout << name * name << endl; // mno¿enie - gwiazdka - asterisk
       cout <<"Kwadrat liter nazwiska";
       cout << surname * surname << endl; // mno¿enie - gwiazdka - asterisk
       int  n = 64;
       int  s = 16;
       cout <<"Suma kwadratów liczby liter imienia i nazwiska";
       cout << n + s << endl; // suma kwadratów
   }
   {
      cout <<"Suma liter imienia i nazwiska wynosi:";
      cout << name + surname << endl;
      int ns2 = 12;
      cout <<"Kwadrat ich sumy";
      cout << ns2 * ns2 << endl; 
   }
   {
      cout <<"Różnica między liczbą liter nazwiska a imienia";
      cout << name - surname << endl; // odejmowanie  
      int ns1 = 8;
      cout <<"Kwadrat ich różnicy";
      cout << ns1 * ns1 << endl; 
   }
   {
      cout <<"Sześcian liczby 4";
      int a = 4;
      int b = 4;
      int c = 4;
      cout << a * b * c << endl; //sześcian 4
      cout <<"Sześcian liczby 8";
      int a1 = 8;
      int b1 = 8;
      int c1 = 8;
      cout << a1 * b1 * c1 << endl; // sześcian 8 
      cout <<"Suma sześcianów licz 4 i 8:";
      int a2 = 464;
      int a3 = 8512;
      cout << a2 + a3 << endl;
   }
   {
      cout <<"Różnica sześcianów licz 4 i 8";
      int a2 = 464;
      int a3 = 8512;
      cout << a3 - a2 << endl; // Różnica sześcianów
   }
   return 0;
 
}
