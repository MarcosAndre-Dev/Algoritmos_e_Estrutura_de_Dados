

N = int(input())

for i in range(N):

    palavras = input().split()

    palavras.sort(key=len,reverse=True)

    print(" ".join(palavras))