import random

def valorMedio ( vetor, inicio, fim ):

    pivot1 = random.randint( inicio, fim - 1 )
    pivot2 = random.randint( inicio, fim - 1 )
    pivot3 = random.randint( inicio, fim - 1 )

    if vetor[pivot1] > vetor[pivot2] and vetor[pivot1] > vetor[pivot3]:
        return pivot1

    elif vetor[pivot2] > vetor[pivot1] and vetor[pivot2] > vetor[pivot3]:
        return pivot2

    else:
        return pivot3


def medianRandomQuickSort ( inicio, fim, vetor ) :


    if inicio >= fim :
        return

    medio = valorMedio( vetor, inicio, fim )

    vetor[inicio], vetor[medio] = vetor[medio], vetor[inicio]


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

    medianRandomQuickSort ( inicio, esquerda-1, vetor )

    medianRandomQuickSort ( direita, fim, vetor)

    return vetor
