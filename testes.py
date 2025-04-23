palavra = 'yuri'
sugestao = 'yurizin'

count = 0

arrayPalavra = []
arraySugestao = []

for i in palavra:
    arrayPalavra.append(i)

for i2 in sugestao:
    arraySugestao.append(i2)

for i in range(len(sugestao)):
    if arrayPalavra[i] == arraySugestao[i]:
        print("Igual")
        count += 1