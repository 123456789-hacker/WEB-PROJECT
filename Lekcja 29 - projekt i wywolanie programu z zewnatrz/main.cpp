#include <iostream>
#include <string>
#include <string.h>
using namespace std;

int main(int argc, char *argv[])
{
    int a = 5;
    if (a == 10)
      return EXIT_FAILURE;
      
    /*
       argc = arguments counter
       argv = arguments value    
    */
    
    char arg[] = {'a', 'b', 'c'};
    char *arg2 = "ciag znakow";
    char *arg3[] = {"ciag znakow a",  "ciag znakow b", "ciag znakow c"};
    
    string napis = arg3[0];
    
    //cout << napis << endl;
    
    
  /*  cout << argc;
    cout << "wartosc: " << argv[0] << endl;
    */
    
    while(argc--)
    {
       
       if (strcmp(*argv, "aa") == 0)
         cout << "chcesz aaa to masz AAAAAAAA " << endl;
         
       cout << *argv++ << endl;
       
    }
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
