import random

user = int(input("Digite um numero para acertar "))
micr = random.randint(0,10)

while user != micr:
	user = int(input("Errou, Tente novamente: "))

print("Parabens, vc conseguiu achar meu numero")
