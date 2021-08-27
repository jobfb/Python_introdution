#leia uma quantidade indeterminada de duplas de valores inteiros X e Y.
# Escreva para cada X e Y uma mensagem que indique se esses valores foram digitados em ordema crescente ou decrescente    
# O programa deve finalizar quando os  dois valores forem iguais.

X =  int
Y = int


X = int(input("digite um valor:"))
Y = int(input("digite outro valor :"))

while X!= Y:
    if X>Y:
        print("Os valores foram digitados em ordem crescente")
    else:
        print("Os valores foram digitados em ordem decrescente")
    print("caso queira continuar insira novos valores, para cancelar a repetição insira o mesmo valor em ambos espaços")
    X = int(input("digite um valor:"))
    Y = int(input("digite outro valor :"))

print("fim ")   