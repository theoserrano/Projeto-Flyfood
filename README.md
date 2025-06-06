# Projeto-Flyfood
# Caminho Ótimo na Matriz

Este projeto lê uma matriz a partir de um arquivo texto (`matriz.txt`), onde cada célula pode conter um ponto identificado por um valor diferente de zero. O programa calcula o melhor caminho que começa e termina no ponto `'R'` passando por todos os demais pontos, minimizando a distância total percorrida.

---

## Descrição

O código:

- Lê uma matriz de dimensão `L x C` do arquivo `matriz.txt`.
- Identifica as posições dos pontos diferentes de `'0'`, incluindo um ponto especial `'R'`.
- Gera todas as permutações possíveis dos pontos intermediários.
- Calcula o custo (distância Manhattan) para cada caminho que inicia e termina no ponto `'R'`.
- Encontra o caminho de menor distância total.
- Exibe o melhor caminho e a distância correspondente.

---

## Formato do arquivo `matriz.txt`

- A primeira linha contém dois números inteiros separados por espaço: número de linhas (L) e colunas (C).
- As próximas L linhas contêm C valores separados por espaço, representando a matriz.
- Exemplo:

3 4
R 0 1 0
0 0 0 2
3 0 0 0
