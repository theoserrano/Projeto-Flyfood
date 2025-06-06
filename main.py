file = open("matriz.txt", "r")

def permutacoes_chaves(lista_chaves):
    if len(lista_chaves) == 0:
        return [[]]
    
    resultado = []
    for i in range(len(lista_chaves)):
        elemento = lista_chaves[i]
        restantes = lista_chaves[:i] + lista_chaves[i+1:]
        for perm in permutacoes_chaves(restantes):
            resultado.append([elemento] + perm)
    
    return resultado

def distancia_total(caminho, coordenadas):
    total = 0
    for i in range(len(caminho) - 1):
        x1, y1 = coordenadas[caminho[i]]
        x2, y2 = coordenadas[caminho[i + 1]]
        total += abs(x1 - x2) + abs(y1 - y2)
    return total

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

