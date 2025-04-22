palavra = 'yuri'
palavra = palavra.lower()

contagemErros = 0
dicaSolicitar = 0
print("Digite 0 quando quiser parar")
while True:
    sugestao = input("Digite sua sugestão: ")
    sugestao = sugestao.lower()

    contagemErros += 1

    if  contagemErros == 3:
        print(' ')
        print("Para dica, digite: 3")
        print(" ")


    contPalavras = 0;
    for i in palavra:
        contPalavras += 1

    espacosPalavra = "_ " * contPalavras

    if sugestao == '3':
        print(" ")
        print(f"Dica: {espacosPalavra}" )

    contDnv = 0
    for i in sugestao:
        for i2 in palavra:
            if i == i2:
                contDnv += 1

    if 2 <= contDnv < 4:
        print(f"{sugestao} está perto")
    elif contDnv >= 4:
        print(f"{sugestao} está muito perto")

    if sugestao == palavra:
        print(f"Você acertou! a palavra é --> {palavra} <--")
        break

    parada = 1
    if parada == 0:
        break
