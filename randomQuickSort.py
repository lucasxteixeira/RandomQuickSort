import random

def randomQuickSort( inicio, fim, vetor ) :

    if inicio >= fim :
        return

    randomPivot = random.randint( inicio, fim - 1 )
    vetor[inicio], vetor[randomPivot] = vetor[randomPivot], vetor[inicio]

    pivot = inicio
    esquerda = inicio + 1
    direita = fim

    while esquerda < direita :
        
        if vetor [ esquerda ] > vetor [ pivot ] :

            direita = direita - 1

            if vetor[esquerda] > vetor[direita] and vetor[direita] < vetor[pivot]:
        
                vetor [ esquerda ], vetor [ direita ] = vetor [ direita ], vetor [ esquerda ]
            
        else:
            esquerda += 1

    vetor [ esquerda - 1 ], vetor [ pivot ] = vetor [ pivot ], vetor [ esquerda - 1 ]

    randomQuickSort ( inicio, esquerda-1, vetor )
    
    randomQuickSort ( direita, fim, vetor)

    return vetor
