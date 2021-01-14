#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

void board(void);

int PlayerTurn(int);

int ifWin();

char position[9] = { '1','2','3','4','5','6','7','8','9' };

int main()
{
    printf("Welcome to this tic tac toe game\n");

    printf("player 1 - x | player 2 - o\n");

    int result;
    int turnCount = 1;
    int count = 0;
    int playerchoice;
    int turn;

    board();

    while (1)
    {
        bool won = false;

        if (turnCount > 2)
        {
            turnCount = 1;
        }

        turn = PlayerTurn(turnCount);

        printf("Player %i make your move: ", turn);

        scanf_s("%i", &playerchoice);

        for (int j = 0; j < 10; j++)
        {
            if (j == playerchoice - 1)
            {
                if (turnCount == 1)
                {
                    position[j] = 'x';
                    if (position[j] == 'x')
                    {
                        position[j] = 'x';
                        printf("invalid position");
                    }
                }
                else
                {
                    position[j] = 'o';
                }
                
            }
        }


        printf("\n");

        board();
        
        result = ifWin();

        if (result == 1)
        {
            won = true;
        }

        if (won)
        {
            if (turnCount == 1)
            {
                printf("player %i won", turnCount);
                break;
            }
            else
            {
                printf("player %i won", turnCount);
                break;
            }
        }

    
        turnCount++;
        count++;
        
        if (count == 9)
        {
            printf("Tie");
            break;
        }

    }
    
    return 0;
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

int PlayerTurn( int x)
{

    if (x == 1)
    {
        printf("Is player 1 turn\n");
        return 1;
    }
    else
    {
        printf("Is player 2 turn\n");
        return 2;
    }
}

int ifWin()
{
   
    if ((position[0] == 'x' && position[1] == 'x' && position[2] == 'x') || (position[0] == 'o' && position[1] == 'o' && position[2] == 'o'))
    {
        return 1;
    }
    else if ((position[3] == 'x' && position[4] == 'x' && position[5] == 'x') || (position[3] == 'o' && position[4] == 'o' && position[5] == 'o'))
    {
        return 1;
    }
    else if ((position[6] == 'x' && position[7] == 'x' && position[8] == 'x') || (position[6] == 'o' && position[7] == 'o' && position[8] == 'o'))
    {
        return 1;
    }
    else if ((position[0] == 'x' && position[3] == 'x' && position[6] == 'x') || (position[0] == 'o' && position[3] == 'o' && position[6] == 'o'))
    {
        return 1;
    }
    else if ((position[1] == 'x' && position[4] == 'x' && position[7] == 'x') || (position[1] == 'o' && position[4] == 'o' && position[7] == 'o'))
    {
        return 1;
    }
    else if ((position[2] == 'x' && position[5] == 'x' && position[8] == 'x') || (position[1] == 'o' && position[5] == 'o' && position[8] == 'o'))
    {
        return 1;
    }
    else if ((position[0] == 'x' && position[4] == 'x' && position[8] == 'x') || (position[0] == 'o' && position[4] == 'o' && position[8] == 'o'))
    {
        return 1;
    }
    else if ((position[2] == 'x' && position[4] == 'x' && position[6] == 'x') || (position[2] == 'o' && position[4] == 'o' && position[6] == 'o'))
    {
        return 1;
    }

}