#include <iostream>
#include <cstdlib>
#include <stdio.h>

/*

Programa para obtener un algoritmo minimo de solucion para torre de Hanoi

CLUB ALGORITMIA UPIITA

Aaron Merlos

*/
using namespace std;

void Hanoi(int disco, char origen, char destino, char auxiliar){
	if(disco==1){
		cout<<" Mueve el disco 1 del poste "<<origen<<" al poste "<<destino<<endl;
		return;
	}
	
	Hanoi(disco-1, origen, auxiliar, destino);
	cout<<" Mueve el disco "<<disco<<" del poste "<<origen<<" al poste "<<destino<<endl;
	Hanoi(disco-1, auxiliar, destino, origen);
	
	
}

int main(){
	
	cout<<"\t***ALGORITMO MINIMO TORRE DE HANOI***"<<endl;
	cout<<"\n\nPara el algoritmo se usara la siguiente nomenclatura:\n\tPoste de origen = 'A'\n\tPoste auxiliar = 'B'\n\tPoste de destino = 'C'"<<endl;
	int discos;
	cout<<"\nIntroduzca el numero de discos de su torre de Hanoi: ";
	cin>>discos;
	cout<<"\n\n\tEl algoritmo minimo para "<<discos<<" discos es el siguiente: \n"<<endl;
	Hanoi(discos, 'A', 'B', 'C');
	return 0;
	
}

