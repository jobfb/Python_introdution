#fazer um prgrama capaz de ler base e altura do retangulo, e mostrar: area, perimetro e diagonal com 4 casas decimais
import math
base = float
altura = float
perimetro = float
area = float
diagonal = float

base = float(input("Base do retangulo : "))
altura  = float(input("Altura do retangulo: "))

area = base * altura
perimetro = 2*(base + altura)
diagonal = math.sqrt(base**2 + altura **2)
print(f"A area do retangulo é : {area:.4f}")
print(f"O perimetro do retangulo é : {perimetro:.4f}")
print(f"A diagonal do retangulo é : {diagonal:.4f}")



