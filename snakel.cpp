#include <stdio.h>

int main() {
	int num = 0;
	int p = 1;
	int pm = -1;
	
	scanf("%d", &num);
	int l[num][num];
	int x = num-1;
	
	for(int i = 0; i < num; i++) {
		for(int j = 0; j < num; j++) {
			l[x+j*pm][i] = p;
			p += 1;
		}
		x += (num-1) * pm;
		pm = pm * -1;
	}
	
	for(int pl = 0; pl < num; pl++) {
		for(int ppl = 0; ppl < num; ppl++) {
			printf("%d ",l[pl][ppl]);
		}
		printf("\n");
	}
	
	return 0;
}
