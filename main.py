# Objetivo: Dada uma lista de emails, remover todos os duplicados.

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# # emails_unicos = list(set(emails))
# emails_unicos = list(emails)


# print(emails_unicos)

# Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

# num_list = [1,2,3,4,5,6,7,8]
# lista = list(num_list)
# soma : int = 0
# for i in lista:
#     soma = soma + int(i)
# print(soma)    

# Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.

def eh_primo(n: int) -> bool:
    """Retorna True se n for primo, caso contrário, False."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Checa divisores até a raiz quadrada de n
    i = 5
    while i * i <= n:
        print(n)
        print(i)
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  # Pula múltiplos de 2 e 3
    
    return True

# Testes
# print(eh_primo(2))   # True
# print(eh_primo(11))  # True
# print(eh_primo(25))  # False
print(eh_primo(1009))  # True
