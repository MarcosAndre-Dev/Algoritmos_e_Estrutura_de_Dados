N = int(input())

for caso in range(N):
    texto = input()
    frequencia = {}

    for caractere in texto:
        codigo = ord(caractere)

        if codigo not in frequencia:
            frequencia[codigo] = 0

        frequencia[codigo] += 1

    caracteres = list(frequencia.keys())

    caracteres.sort(
        key=lambda codigo: (frequencia[codigo], -codigo)
    )
    for codigo in caracteres:
        print(codigo, frequencia[codigo])

    if caso < N - 1:
        print()