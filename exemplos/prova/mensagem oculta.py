#Kamilly Santana Alves Ferreira
#Mensagem oculta

while True: #primeiro coloquei um while true para fazer um loop, caso o usuario digite uma frase com mais de 50 caracteres o loop vai voltar para ele digitar uma frase meno
    palavra = input('Informe uma palavra(pode conter outros caracteres): ') #digitar a palavra
    palavra2 = input('Informe uma palavra(pode conter outros caracteres): ')
    palavra3 = input('Informe uma palavra(pode conter outros caracteres): ')
    palavra4 = input('Informe uma palavra(pode conter outros caracteres): ')

    contarPalavras = len(palavra) #aqui eu coloquei para ele contar quantos caracteres tem na frase
    contarPalavras2 = len(palavra2)
    contarPalavras3 = len(palavra3)
    contarPalavras4 = len(palavra4)

    if contarPalavras > 30: # pra justamente fazer a verifição aqui
        print('muitos caracteres') #se for maior que 30 printa muitos caracteres e volta pra digita tudo de novo
    elif contarPalavras2 > 30:
        print('muitos caracteres')
    elif contarPalavras3 > 30:
        print('muitos caracteres')
    elif contarPalavras4 > 30:
        print('muitos caracteres')
    else: #se os caracteres não saiu do limite sai do loop
        break

armPalavras = (palavra, palavra2, palavra3, palavra4) #aqui eu armazei essas palavras em uma tupla
print(armPalavras[0][0]) #depois printei a inicial de cada uma delas
print(armPalavras[1][0])
print(armPalavras[2][0])
print(armPalavras[3][0])
