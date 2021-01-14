#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

/* Creamos el tablero de juego*/
void board(void);

/* Esta función se encarga de determinar al jugador ganador*/
int ifWin();

/* Las posiciones del tablero y lo declaramos afuera de main para que pueda ser visto en cualquier parte de nuestro programa*/
char position[9] = { '1','2','3','4','5','6','7','8','9' };

int main()
{
    printf("Juego del gato\n");

    printf("Jugador1 - x | Jugador2 - o\n");

    int result;
    int turnCount = 1;
    int count = 0;
    int playerchoice;
    int turn;

    board();

    while (1)
    {
        bool won = false;
 
        /* Este condicional se encarga de seleccionar al jugador actual*/
        if (turnCount > 2)
        {
            turnCount = 1;
        }

        printf("Turno del jugador %i: ", turnCount);

        /* Guardamos la posición del usuario en una variable*/
        scanf("%i", &playerchoice);

        /* Creamos un bucle para verificar si la posición ya ha sido tomada o no*/
        for (int j = 0; j < 10; j++)
        {
            if (j == playerchoice - 1)
            {
                if (turnCount == 1)
                {
                    if (position[j] == 'o')
                    {
                        printf("invalid position");
                        position[j] = 'o';
                        turnCount--;
                    }
                    else
                    {
                        position[j] = 'x';
                    }
                }
                else
                {
                    if (position[j] == 'x')
                    {
                        printf("invalid position");
                        position[j] = 'x';
                        turnCount--;
                    }
                    else
                    {
                        position[j] = 'o';
                    }
                }
            }
        }
 
        /* Volvemos a mostrar el tablero ahora con la posición del jugador en el */
        board();
        
        /* Con esta función revisaremos si alguién ya ganó*/
        won = ifWin();

        /* Y este bloque determina que jugador ganó*/
        if (won)
        {
            printf("Jugador %i ganó\n", turnCount);
            break;
        }

        turnCount++;
        count++;
        
        /* Este condicional imprimirá empate y se cerrará el bucle si el tablero se llena y no hay un ganador*/
        if (count == 9)
        {
            printf("Empate");
            break;
        }
    }
}

void board(void)
{
 
    printf(" _____________");
    printf("\n");
    printf("|             |");
    printf("\n");
    printf("|");
    printf("  %c ", position[0]);
    printf("  %c ", position[1]);
    printf("  %c ", position[2]);
    printf(" |");
    printf("\n");

    printf("|");
    printf("  %c ", position[3]);
    printf("  %c ", position[4]);
    printf("  %c ", position[5]);
    printf(" |");
    printf("\n");

    printf("|");
    printf("  %c ", position[6]);
    printf("  %c ", position[7]);
    printf("  %c ", position[8]);
    printf(" |");
    printf("\n");

    printf("|_____________|");
    printf("\n");

}

int ifWin()
{
   
    if ((position[0] == 'x' && position[1] == 'x' && position[2] == 'x') || (position[0] == 'o' && position[1] == 'o' && position[2] == 'o'))
    {
        return true;
    }
    else if ((position[3] == 'x' && position[4] == 'x' && position[5] == 'x') || (position[3] == 'o' && position[4] == 'o' && position[5] == 'o'))
    {
        return true;
    }
    else if ((position[6] == 'x' && position[7] == 'x' && position[8] == 'x') || (position[6] == 'o' && position[7] == 'o' && position[8] == 'o'))
    {
        return true;
    }
    else if ((position[0] == 'x' && position[3] == 'x' && position[6] == 'x') || (position[0] == 'o' && position[3] == 'o' && position[6] == 'o'))
    {
        return true;
    }
    else if ((position[1] == 'x' && position[4] == 'x' && position[7] == 'x') || (position[1] == 'o' && position[4] == 'o' && position[7] == 'o'))
    {
        return true;
    }
    else if ((position[2] == 'x' && position[5] == 'x' && position[8] == 'x') || (position[1] == 'o' && position[5] == 'o' && position[8] == 'o'))
    {
        return true;
    }
    else if ((position[0] == 'x' && position[4] == 'x' && position[8] == 'x') || (position[0] == 'o' && position[4] == 'o' && position[8] == 'o'))
    {
        return true;
    }
    else if ((position[2] == 'x' && position[4] == 'x' && position[6] == 'x') || (position[2] == 'o' && position[4] == 'o' && position[6] == 'o'))
    {
        return true;
    }
    return false;

}