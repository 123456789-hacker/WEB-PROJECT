#include <iostream>
using namespace std;
int main()
{
	float dana;
	cout << "podaj liczbe rzeczywista ";
	cin >> dana;
	// oblicz dwa ilorazy tej liczby przez 11
	cout << dana << "/11 = " << dana/11 << endl;  // dla a = 5 0.454545
	cout << "11/" << dana << " = " << 11/dana << endl;	//  2.2
	// dla liczb calkowitych
	int a;
	cout << "podaj liczbe calkowita ";
	cin >> a;
	// oblicz dwa ilorazy tej liczby przez 11
	cout << a << "/11 = " << 1.*a/11 << endl;  // dla a = 5 0.454545
	cout << "11./" << a << " = " << 11./a << endl;	//  2.2
	
	system("pause");
	return 0;
}

