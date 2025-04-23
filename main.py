import time
import random

print("Seu jogo está iniciando...\n")

time.sleep(2.5)
print("Seu jogo foi iniciado!\n")


contagemErros = 0
dicaSolicitar = 0

print("Digite:\n"
      "0 -> PARAR\n"
      "3 -> DICA\n")

nomes = ["yuri","joao", "maria", "josé"]
animais = ["girafa","cachorro"]
objeto = ["copo", "computador"]

arrays = [nomes, animais, objeto]
choice = random.choice(arrays)

palavra = random.choice(choice)
palavra = palavra.lower()

if palavra in nomes:
    print("A palavra é um nome!")
elif palavra in animais:
    print("A palavra é um animal!")
elif palavra in objeto:
    print("A palavra é um objeto!")

time.sleep(1)
while True:
    sugestao = input("Digite sua sugestão: ")
    sugestao = sugestao.lower()

    contagemErros += 1

    contPalavras = 0;
    for i in palavra:
        contPalavras += 1

    espacosPalavra = "_ " * contPalavras

    if sugestao == '3':
        print(" ")
        print(f"Dica: {espacosPalavra}" )

    contEqual = 0

    arrayPalavra = []
    arraySugestao = []

    for i in palavra:
        arrayPalavra.append(i)

    for i2 in sugestao:
        arraySugestao.append(i2)

    for i in range(len(sugestao)):
        if arrayPalavra[i] == arraySugestao[i]:
            contEqual += 1

    if contEqual >= 3:
        print(f"{sugestao} está muito perto!")


    if sugestao == palavra:
        print(f"Você acertou! a palavra é --> {palavra} <--")
        break

    parada = 1
    if parada == 0:
        break
