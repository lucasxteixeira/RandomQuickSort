import random

def quickSort ( inicio, fim, vetor ) :

    print vetor

    if inicio >= fim :
        return

    randomPivot = random.randint( inicio, fim - 1 )
    vetor[inicio], vetor[randomPivot] = vetor[randomPivot], vetor[inicio]

    print vetor

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

    print vetor
    print

    quickSort ( inicio, esquerda-1, vetor )

    print

    quickSort ( direita, fim, vetor)

    return vetor
        


print (quickSort(0,11,[30,5,7,3,8,4,1,9,0,6,20]))