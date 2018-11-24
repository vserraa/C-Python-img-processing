#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	int var;
	clock_t start, atual;
	while(scanf("%d", &var) != EOF && var != -1){
		FILE *f = fopen("flag.bin", "wb");
		if(var == 1){
			fwrite(&var, sizeof(int), 1, f);
			fclose(f);
			start = clock();
			double elapsed;
			do{
				atual = clock();
				elapsed = (double)(atual-start)/CLOCKS_PER_SEC;
			}while(elapsed < 0.1);

			f = fopen("flag.bin", "wb");
			var = 0;
			fwrite(&var, sizeof(int), 1, f);
			fclose(f);

			start = clock();
			do{
				atual = clock();
				elapsed = (double)(atual-start)/CLOCKS_PER_SEC;
				printf("%lf\n", elapsed);
			}while(elapsed < 5);

			FILE *ans = fopen("number_dots.bin", "rb");
			fread(&var, sizeof(int), 1, ans);
			fclose(ans);
			printf("number of dots is = %d\n", var);
		}
		else{
			var = 0;
			fwrite(&var, sizeof(int), 1, f);
			fclose(f);
		}

	}

	return 0;
}