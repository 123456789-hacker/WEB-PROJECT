#include <iostream>
using namespace std;
int main()
{
	int bok1; 
	cout << "Podaj dlugosc boku prostokata ";
	cin >> bok1;
	//cout << "wczytano " << bok1 << endl;
	int bok2; 
	cout << "Podaj dlugosc drugiego boku ";
	cin >> bok2;
	//cout << "wczytano " << bok2 << endl;
	int pole = bok1 * bok2;
	cout << "Twoj prostokat ma pole rowne " << pole << endl;
	int obwod = bok1 + bok1 + bok2 + bok2;
	cout << "Twoj prostokat ma obwod rowne " << obwod << endl;	 
	system("pause");
	return 0;
}


