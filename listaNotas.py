import random
notas = [random.random() * 10 for i in range(5)]
notas = [round(nota, 1) for nota in notas]

media = sum(notas) / len(notas)
media = round(media, 2)

if media >= 7:
	print("Parabens sua média foi: ", media)
else:
	print("Desculpe, você não passou. Sua nota foi: ", media)

#print(media)
