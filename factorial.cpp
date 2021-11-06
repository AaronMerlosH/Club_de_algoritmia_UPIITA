#include <iostream>
#include <cstdlib>
#include <stdio.h>

/*

Programa para sacar un factorial usndo recursividad

CLUB ALGORITMIA UPIITA

Aaron Merlos

*/

int factorial(int numero){
    using namespace std;
	if(numero==0){
		return 1;
	}
	return numero*factorial(numero-1);
}

int num;
int main() {
    using namespace std;
    
    cout<<"\t**PROGRAMA DE FACTORIAL USANDO RECURSIVIDAD***\n\n"<<endl;
    
	cout<<"Ingrese el numero del que desea recibir su factorial: ";
	cin>>num;
	cout<<"\n\nEl factorial de "<<num<<" es: "<<factorial(num)<<endl;
	
	return 0;
}

