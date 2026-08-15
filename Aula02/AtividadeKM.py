while True: 
    n, k, m = map(int, input().split())

    if n == 0 and k == 0 and m == 0: 
        break

    pessoas = list(range(1, n + 1))

    ativas = [True] * n

    pos_k = 0
    pos_m = n - 1

    quantidade = 0
    resultado = []

    while quantidade < n:
        contador = k

        while contador > 0:
            if ativas[pos_k]:
                contador -= 1
            if contador > 0:
                pos_k = (pos_k + 1) % n

        pessoa_k = pessoas[pos_k]

        contador = m

        while contador > 0:
            if ativas[pos_m]:
                contador -= 1
            if contador > 0:
                pos_m = (pos_m - 1) % n

        pessoa_m = pessoas[pos_m]

        if pessoa_k == pessoa_m: 

            resultado.append(str(pessoa_k))

            ativas[pos_k] = False

            quantidade += 1
        else:
            resultado.append(str(pessoa_k))
            resultado.append(str(pessoa_m))

            ativas[pos_k] = False
            ativas[pos_m] = False
            quantidade += 2
        pos_k = (pos_k + 1) % n
        pos_m = (pos_m - 1) % n
    print("  ,".join(resultado))
