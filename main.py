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
    
    
    return pares_ord

def gerar_caminhos(pares_ord):
    pontos_intermediarios = []
    for p in pares_ord:
        if p != 'R':
            pontos_intermediarios.append(p)

    caminhos_intermediarios = permutacoes_chaves(pontos_intermediarios)

    caminhos_completos = []
    for caminho in caminhos_intermediarios:
        caminhos_completos.append(['R'] + caminho + ['R'])

    return caminhos_completos

def melhor_caminho(caminhos, coordenadas):
    menor_distancia = 100000000000
    melhor = None

    for caminho in caminhos:
        dist = distancia_total(caminho, coordenadas)
        if dist < menor_distancia:
            menor_distancia = dist
            melhor = caminho

    return melhor, menor_distancia


pares_ord = pontos(file)
caminhos = gerar_caminhos(pares_ord)
melhor, dist = melhor_caminho(caminhos, pares_ord)

print(f"Melhor caminho:: {melhor}")
print(f"Distância total: {dist}")