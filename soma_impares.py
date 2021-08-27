# faça um programa que leia 2 calores inteiros X e Y(em qualquer ordem) .Em seguida calcule e mostre a soma dos inteiros entre eles

x = int
y = int
soma = int
guard = int

(print(f"digite dois numeros:"))

x = int(input())
y = int(input())

if x > y:
    guard = x
    x = y
    y = guard

soma = 0
for i in range (x, y):
    if i % 2 != 0:
        soma = soma + i 

print(f"A SOMA É :{soma} ")