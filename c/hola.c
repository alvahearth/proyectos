#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <stdbool.h>

struct Choices
{
    char firstChoice[7];
    char SecondChoice[7];
    char ThirdChoice[8];
};

int comparison(const char *string1,const char *string2);
int calculateWin(int, int);
int Win(int x);
int Loss(int x);

int main()
{

    int cpuScore = 0;
    int playerScore = 0;
    int turnCount = 1;
    srand(time(NULL));

    struct Choices Cpu;

    // Cpu choices
    strcpy(Cpu.firstChoice, "piedra");
    strcpy(Cpu.SecondChoice, "papel");
    strcpy(Cpu.ThirdChoice, "tijeras");

    printf("Cachipun\n");

    printf("tienes que obtener 3 puntos para ganar el juego\n");

    while (1)
    {
        bool win = false;
        bool loss = false;
        int random_number;
        char player[8];
        int playerNumber = 1;
        bool playerWin;
        char cpu[8];
        int cpuChoice;
        int cpuNumber = 2;
        bool cpuWin;
        
        printf("ronda numero %i\n", turnCount);

        printf("Piedra, Papel o Tijeras: ");

        scanf("%s", player);

        random_number = rand() % 3;
        
        if (random_number == 0)
        {
            strcpy(cpu,Cpu.firstChoice);
        }
        else if (random_number == 1)
        {
            strcpy(cpu,Cpu.SecondChoice); 
        }
        else if (random_number == 2)
        {
            strcpy(cpu,Cpu.ThirdChoice);
        }

        int result = comparison(player,cpu);

        if (playerWin = calculateWin(result,playerNumber))
        {
            playerScore++;
        }

        else if (cpuWin = calculateWin(result,cpuNumber))
        {
            cpuScore++;
        }

        printf("%s vs %s\n", player, cpu);

        win = Win(playerScore);
        loss = Loss(cpuScore);

        if (win)
        {
            printf("Ganaste\n");
            break;
        }

        if (loss)
        {
            printf("Perdiste\n");
            break;
        }

        printf("Jugador: %i\n",playerScore);
        printf("Cpu: %i\n",cpuScore);
        turnCount++;
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

int Win(int x)
{
    if (x == 3)
    {
        return true;
    }
    else
    {
        return false;
    }
    return false;
    
}

int Loss(int x)
{
    if (x == 3)
    {
        return true;
    }
    else
    {
        return false;
    }
    return false;   
}
