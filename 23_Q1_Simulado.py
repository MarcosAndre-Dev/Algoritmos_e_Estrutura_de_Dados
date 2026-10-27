pilha = []
#Aqui estou definindo a lista que vou utilizar nesse problema

while True:
#Aqui começo a repetição.

    programa = input().split()
    #Lendo o que o usuário digitar

    if not programa:
        continue
    #Este if serve para casos do usuário digitar um enter sem nada, o programa irá continuar

    comparacao = int(programa[0])
    #Estou tranformando o primeiro str em inteiro para fazer a comparação no while

    if comparacao == 1:
        pilha.append(int(programa[1]))
    #Esta comparação vê o comando e adiciona o número que o usuário digitar

    elif comparacao == 2:
        if len(pilha) > 0:
            pilha.pop()
        else:
            print("Pilha vazia!")
    #Esta vê se a lista está vazia, se não estiver ela ela remove o ultimo elemento

    elif comparacao == 3:
        if len(pilha) == 0:
            print("Pilha vazia!")
        else:
            ultimo = pilha[-1]
            print(ultimo)
    #Esta também vê se está vazia, se estive ela printa lista vazia, se não, ela mostra o ultimo item
    elif comparacao == 0:
        break
    #Acaba o programa se o numero digitado for = a 0.