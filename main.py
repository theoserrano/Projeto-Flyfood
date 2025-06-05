file = open("matriz.txt", "r")

def permutacoes_chaves(lista_chaves):
    pilha = [([], lista_chaves)]
    resultado = []

    while pilha:
        caminho_atual, restantes = pilha.pop()

        if not restantes:
            resultado.append(caminho_atual)
        else:
            for i in range(len(restantes)):
                nova_chave = restantes[i]
                novo_caminho = caminho_atual + [nova_chave]
                novo_restante = restantes[:i] + restantes[i+1:]
                pilha.append((novo_caminho, novo_restante))

    return resultado

def pontos(file):
    pares_ord = {}
    l, c = map(int, file.readline().split(" "))

    for i in range(l):
        linha = file.readline().strip().split(" ")
        if len(linha) == c:
            for colun in range(c):
                valor = linha[colun].strip()
                if valor != '0':
                    pares_ord[valor] = (i, colun)
        else:
            raise ValueError("Número inconsistente de colunas na linha.")
    
    pontos_intermediarios = [p for p in pares_ord.keys() if p != 'R']

    caminhos_intermediarios = permutacoes_chaves(pontos_intermediarios)
    
    caminhos_completos = [['R'] + caminho + ['R'] for caminho in caminhos_intermediarios]

    return caminhos_completos, pares_ord
    

print(pontos(file))

# Exemplo:
# res = permutacoes_n_digitos(4)
# print(res)
# print("Total:", len(res))  # Deve imprimir 24 (4!)

