#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

int comparison(const char *string1,const char *string2);

int calculateWin(int x, int y);

int main(void) 
{
    printf("Cachipun de 2 jugadores \n");
    
    int ronda = 1;
    int player1Score = 0;
    int player2Score = 0;

    while(1)
    {
        char array[3][10] = {"tijeras", "piedra", "papel"};
        
        char player1Choice[9];
        bool player1Win;
        char player1[9];
        int player1Number = 1;

        char player2Choice[9];
        bool player2Win;
        char player2[9];
        int player2Number = 2;

        printf("Ronda numero %i: \n",ronda);
        
        printf("Jugador 1 \n");
        printf("Piedra, Papel o Tijeras: ");
        scanf("%s", &player1Choice);

        printf("Jugador 2\n");
        printf("Piedra, Papel o Tijeras: ");
        scanf("%s", &player2Choice);

        for (int i = 0; i < 3; i++)
        {
           
            if (strcmp(player1Choice,array[i]) == 0)
            {
                strcpy(player1,array[i]);
            }
            else if (strcmp(player2Choice,array[i]) == 0)
            {
                strcpy(player2,array[i]);
            }

        }

        printf("%s\n",player1);
        printf("%s\n",player2);

        int result = comparison(player1,player2);

        if (player1Win = calculateWin(result,player1Number))
        {
            player1Score++;
        }

        else if (player2Win = calculateWin(result,player2Number))
        {
            player2Score++;
        }

        printf("Puntaje del jugador 1: %i\n",player1Score);
        printf("Puntaje del jugador 2: %i \n",player2Score);

        if (player1Score == 3)
        {
           printf("Jugador 1 Ganó");
        }
        else if (player2Score == 3)
        {
           printf("Jugadoe 2 ganó");
        }

        ronda++;
    }
}

int comparison(const char *string1,const char *string2)
{

    if (strcmp(string1,"piedra") == 0)
    {

        if (strcmp(string2,"piedra") == 0)
        {
            return 1;
        }
        else if (strcmp(string2,"papel") == 0)
        {
            return 0;
        }
        else if (strcmp(string2,"tijeras") == 0)
        {
            return 2;
        }  
    }

    else if (strcmp(string1,"papel") == 0)
    {

        if (strcmp(string2,"piedra") == 0)
        {
            return 2;
        }
        else if (strcmp(string2,"papel") == 0)
        {
            return 1;
        }
        else if (strcmp(string2,"tijeras") == 0)
        {
            return 0;
        }  
    }

    else if (strcmp(string1,"tijeras") == 0)
    {

        if (strcmp(string2,"piedra") == 0)
        {
            return 0;
        }
        else if (strcmp(string2,"papel") == 0)
        {
            return 2;
        }
        else if (strcmp(string2,"tijeras") == 0)
        {
            return 1;
        }  
    }
}

int calculateWin(int x, int y)
{
    if (y == 1)
    {
        if (x == 2)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    else if (y == 2)
    {
        if ( x == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
        
    }
}