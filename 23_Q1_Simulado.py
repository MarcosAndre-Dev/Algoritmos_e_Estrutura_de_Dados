# Você está desenvolvendo um pequeno editor de texto que registra as últimas operações realizadas pelo usuário.

# Cada operação possui um número inteiro que representa uma ação realizada no sistema.

# O programa deverá permitir que o usuário execute as seguintes operações:

# - 1 X → adiciona a operação X à pilha;
# - 2 → desfaz a última operação realizada;
# - 3 → mostra a última operação existente na pilha;
# - 0 → encerra o programa.

# Restrições

# É obrigatório utilizar uma lista Python como pilha.
# A inserção deverá ser realizada utilizando append().
# A remoção deverá ser realizada utilizando pop().
# É proibido utilizar queue, deque ou qualquer biblioteca de estrutura de dados.
# É proibido utilizar remove() para retirar elementos.
# É proibido utilizar sort() ou sorted().
# A operação de consulta (3) não pode remover o elemento da pilha.
# O programa deverá tratar corretamente a tentativa de executar 2 quando a pilha estiver vazia.
# O programa deverá tratar corretamente a tentativa de executar 3 quando a pilha estiver vazia.
# Não é permitido utilizar max() ou min().
# Não é permitido utilizar clear() para esvaziar a pilha.
# A pilha deverá funcionar segundo o princípio LIFO — Last In, First Out.
# Não é permitido utilizar classes.
# Não é permitido criar funções utilizando def.
# O programa deverá continuar aceitando operações até que o usuário informe 0.

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