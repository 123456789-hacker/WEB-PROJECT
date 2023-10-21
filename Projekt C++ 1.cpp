#include <iostream>
using namespace std;
int main() {
int name,surname;
cout << "Prosze podac z ilu liter skada sie nazwisko.:";
cin >> surname;
cout << "Prosze podac z ilu liter sklda sie imie.: ";
cin >> name;
if(name>surname){
cout<<name<<endl;
}else{
cout<<surname<<endl;
}
if(name==surname){
cout<<"Liczby sa rowne"<<endl;
}

return 0;
}

