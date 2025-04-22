palavra = 'Yurizinho'
palavra = palavra.upper()

contagemErros = 0
print("Digite 0 quando quiser parar")
while True:
    sugestao = input("Digite sua sugestão: ")
    sugestao = sugestao.upper()

    contagemErros += 1

    contPalavras = 0;
    for i in palavra:
        contPalavras += 1

    espacosPalavra = "_ " * contPalavras

    if contagemErros > 3:
        print(f"Dica {espacosPalavra}" )

    if sugestao == palavra:
        print(f"Você acertou! a palavra é {palavra}")
        break

    parada = 1
    if parada == 0:
        break
