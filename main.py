def permutacoes_n_digitos(n):
    digitos = [str(i) for i in range(n)]
    pilha = [("", digitos)]
    resultado = []

    while pilha:
        prefixo, restantes = pilha.pop()

        if len(prefixo) == n:
            resultado.append(prefixo)
        else:
            for i in range(len(restantes)):
                novo_prefixo = prefixo + restantes[i]
                novo_restante = restantes[:i] + restantes[i+1:]
                pilha.append((novo_prefixo, novo_restante))

    return resultado

# Exemplo:
res = permutacoes_n_digitos(4)
print(res)
print("Total:", len(res))  # Deve imprimir 24 (4!)

