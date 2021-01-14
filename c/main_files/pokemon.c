#include <stdlib.h>
#include <stdio.h>


int main(void) {
  int pikachu_salud = 100;
  int squirtle_salud = 100;
  int pikachu_ataque = 30;
  int squirtle_ataque = 35;
  int turno = 0;

  while (pikachu_salud >= 0 || squirtle_salud >= 0) {
    if (turno == 0) {
      printf("*********\n");
      printf("*turno 0*\n");
      printf("*********\n");
      printf("---------------------------------------\n");
      printf("salud de pikachu = %d\n",pikachu_salud);
      printf("salud de squirtle = %d\n",squirtle_salud);
      printf("---------------------------------------\n");
      printf("pikachu ataca\n");
      squirtle_salud = squirtle_salud - pikachu_ataque;
      printf("salud de squirtle = %d\n", squirtle_salud);
      turno = turno + 1;

    } else if (turno == 1) {
      printf("*********\n");
      printf("*turno 1*\n");
      printf("*********\n");
      printf("salud de pikachu = %d\n",pikachu_salud);
      printf("salud de squirtle = %d\n",squirtle_salud);
      printf("squirtle ataca\n");
      pikachu_salud = pikachu_salud - squirtle_ataque;
      printf("salud de pikachu = %d\n", pikachu_salud);
      turno = turno - 1;
    }
  }
  printf("-----------------------------------------\n");
  printf("resultado final\n");
  printf("salud de pikachu = %d\n", pikachu_salud);
  printf("salud de squirtle = %d\n",squirtle_salud);
  printf("-----------------------------------------\n");

  if (pikachu_salud >= squirtle_salud) {
    printf("pikachu gana\n");
      } else {
    printf("squirtle gana\n");
   }
  return 0;
}

