while True: 

    try: 
        expressao = input()

        pilha = []
        correta = True

        for caractere in expressao:

            if caractere == '(':
                pilha.append(caractere)

            elif caractere == ')':

                if len(pilha) == 0:
                    correta = False
                    break

                pilha.pop()

        if correta and len(pilha) == 0: 
            print("Correct")
        else: 
            print("Incorrect")

    except EOFError:
        break