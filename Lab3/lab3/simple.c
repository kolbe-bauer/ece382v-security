#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *fptr;

	fptr = fopen("data/simple.txt","w");

	if(fptr == NULL)
	{
		printf("Error!");
		exit(1);
	}

	fprintf(fptr,"Hello World!");
	fclose(fptr);

	FILE *fptr2 = fopen("data/secret.txt","r");
	if(fptr2 == NULL)
	{
		printf("Secret can't be read!");
		exit(1);
	}
	char buff[255];
	fgets(buff, 255, (FILE*)fptr2);
	printf("%s\n",buff);
	fclose(fptr2);

	return 0;
}
