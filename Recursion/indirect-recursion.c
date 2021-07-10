#include <stdio.h>
// function prototype
void funB(int n);

void funA(int n){
	if (n>0){
		printf("%d", n);
		funB(n-1);
	}
}

// function defination
void funB(int n){
	if (n>1){
		printf("%d", n);
		funA(n/2);

	}
}

int main(){
	funA(10)
	return 0;
}