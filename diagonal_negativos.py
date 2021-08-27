#Fazer um programa para ler um numero inteiro N (no maximo 10 ) e uma matriz quadrada de ordem N contendo numeros inteiros
#Em seguida mostrar a diagonal principal
#Dizer quantos valores negativos a matriz possui 


N: int
neg: int

N = int(input("Qual a ordem da matriz? "))
mat: int = [[0 for x in range(N)] for x in range(N)]
for i in range(0, N):
    for j in range(0, N):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))


print("Diagonal principal:")
for i in range(0,N):
    print(f"{mat[i][i]}")

neg = 0 
print()
for i in range(0, N):
    for j in range(0, N): 
        if mat[i][j] < 0:
            neg = neg + 1 

print(f" O TOTAL DE NUMERO NEGATIVOS É : {neg}") 