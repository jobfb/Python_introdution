#fazer um programa q leia o nome e a idade de 2 pessoas.E ao final mostrar os nomes e a idade media entre eles com 1 casa decimal
nome1 = str
nome2 = str
idade1 = int
idade2 = int
media = float


nome1 = input(f"digite o nome de uma pessoa:")
idade1 = int(input(f"agora sua idade :"))
nome2 = input(f"digite o nome de outra pessoa:")
idade2 = int(input("agora digite a idade da segunda pessoa:"))
media = (idade1 + idade2) /2

print(f"A idade media de {nome1} e {nome2} é de {media:.2f}")