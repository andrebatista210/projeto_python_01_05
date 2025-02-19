lista_de_numeros: list = [40, 50, 60, 70, 0, -408593, 1, 50]

def ordena_numeros(numeros: list) -> list:

    numeros = numeros[:]
    
    # Algoritmo de ordenação (Bubble Sort)
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] > numeros[j]:
                numeros[i], numeros[j] = numeros[j], numeros[i]
    
    return numeros  # Retorna a lista ordenada

# Chamando a função e imprimindo o resultado
numeros_ordenados = ordena_numeros(lista_de_numeros)
print(numeros_ordenados)
