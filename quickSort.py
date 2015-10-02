def quickSort( inicio, fim, vetor ) :

    if inicio >= fim :
        return

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

    quickSort ( inicio, esquerda-1, vetor )
    
    quickSort ( direita, fim, vetor)

    return vetor
