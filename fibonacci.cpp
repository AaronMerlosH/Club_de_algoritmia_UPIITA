#include <iostream>
#include <cstdlib>
#include <stdio.h>

/*

Programa para obtener serie Fibonacci usando recursividad

CLUB ALGORITMIA UPIITA

Aaron Merlos

*/

int fibonacci(int posicion){
    using namespace std;
	if(posicion==0){
		return 0;
	}
	else if(posicion==1){
	    return 1;
	}
	return fibonacci(posicion-1)+fibonacci(posicion-2);
}

int pos;
int main() {
    using namespace std;
    
    cout<<"\t**PROGRAMA SERIE DE FIBONACCI USANDO RECURSIVIDAD***\n\n"<<endl;
    
	cout<<"Ingrese la posicion que desea obtener de la serie de fibonacci: ";
	cin>>pos;
	cout<<"\n\nEl valor correspondiente a la serie Fibonacci con la posicion "<<pos<<" es: "<<fibonacci(pos)<<endl;
	
	return 0;
}


