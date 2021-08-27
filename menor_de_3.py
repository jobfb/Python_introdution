#fazer um programa q leia 3 numero inteiros e diga qual é o menor caso haja repetição mostrar apenas 1 vez

numero1 =  int
numero2 = int
numero3 = int
menorNumero = int



numero1 = int(input("digite o primeiro numero:"))
numero2 = int(input("digite o segundo numero:"))
numero3 = int(input("digite o terceiro numero:"))

if numero1 < numero2 and numero1 < numero3 :
    menorNumero = numero1
elif numero2 < numero3:
    menorNumero = numero2
else :
    menorNumero = numero3


print(f"O menor numero é {menorNumero}")