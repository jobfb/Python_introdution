#Fça um programa que armazene N numeros reais em um vetor, Em seguida  :
#imprima todos os elemnentos do vetor
#Mostra na tela a soma dos elementos do vetor
#Mostre a media dos elementos 

N: int
soma = float
media = float

N = int(input("Quantos numeros voce vai digitar? "))
vet: float = [0 for x in range(N)]
for i in range(0, N):
 vet[i] = float(input("Digite um numero: "))


print()

print("NUMEROS DIGITADOS:")
for i in range(0, N):
 print(f"{vet[i]:.2f}")

print()

soma = 0
for i in range(0,N):
    soma = soma + vet[i]
print(F"SOMA É :{soma:.2f}")

print()

media =  soma / N
print(F"A MEDIA É :{media:.2f}")
