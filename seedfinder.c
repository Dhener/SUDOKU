#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){
    int tamanhoNome;
    unsigned int seed;
    int i;
    int aleatorio[5];
    unsigned long append = 1;
    unsigned long append2 = 1;
    char incre[20];
    char incre2[20];
  
    while(1){
      append ++;
      append2 *= 32;
      sprintf(incre, "%d", append);
      sprintf(incre2, "%d", append2);
      char playerData[0xff] = "epic_dijkstra.";
      strcat(playerData, incre);
      strcat(playerData, incre2);
      seed = 0;
      tamanhoNome = strlen(playerData);
      
      for (i = 0; tamanhoNome = strlen(playerData), (long)i < tamanhoNome >> 2; i = i + 1) {
        seed = seed + *(int *)(playerData + (long)i * 4);
      }
      
      srand(seed);
      
      aleatorio[0] = rand() % 100;
      aleatorio[1] = rand() % 100;
      aleatorio[2] = rand() % 100;
      aleatorio[3] = rand() % 100;
      aleatorio[4] = rand() % 100;
      
      if((aleatorio[0] < 5 && aleatorio[1] < 5 && aleatorio[2] < 5 && aleatorio[3] < 5) ||
        (aleatorio[0] < 5 && aleatorio[1] < 5 && aleatorio[2] < 5 && aleatorio[4] < 5) ||
        (aleatorio[0] < 5 && aleatorio[1] < 5 && aleatorio[4] < 5 && aleatorio[3] < 5) ||
        (aleatorio[0] < 5 && aleatorio[4] < 5 && aleatorio[2] < 5 && aleatorio[3] < 5) ||
        (aleatorio[4] < 5 && aleatorio[1] < 5 && aleatorio[2] < 5 && aleatorio[3] < 5)
      ){
        printf("Seed %s success\n", playerData);
        printf("Valor gerado: %d\n", aleatorio[0]);
        printf("Valor gerado: %d\n", aleatorio[1]);
        printf("Valor gerado: %d\n", aleatorio[2]);
        printf("Valor gerado: %d\n", aleatorio[3]);

        FILE *file;
        file = fopen("seed.txt","w");
        if(file == NULL){
            printf("Error!");   
            exit(1);             
        }

        fprintf(file,"%s", playerData);
        fclose(file);

        break;
      }
    }

    return 0;
}
