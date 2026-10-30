pilha = []

qtd_paginas = 0
ultimo = 0

while True:

    paginas = input().split()

    if not paginas:
        continue

    comparacao_paginas = int(paginas[0])

    if comparacao_paginas == 0:
        break
    elif comparacao_paginas == 1:
        pilha.append(int(paginas[1]))
    elif comparacao_paginas == 2:
        if len(pilha) > 0:
            pilha.pop()
        else:
            print("Nenhuma página para voltar")
    elif comparacao_paginas == 3:
        if len(pilha) > 0:
            ultimo = pilha[-1]
            print(ultimo)
        else:
            print("Nenhuma página aberta")
    