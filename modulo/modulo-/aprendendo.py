import math #biblioteca de matematica inteira

raiz = math.sqrt(3249) #sqrt retorna a raiz quadrada do x
print(raiz)

# from math import sqrt
# raiz = sqrt (3249) - Importa apenas o sqrt em vez de importar a biblioteca inteira, é mais leve

import Uteis

gato = Uteis.desenhar_gato()
print(gato)

#pacote:
#organizador dos códigos

from googletrans import Translator
tradutor = Translator()
texto = input('Digite um texto: ')
ingles = tradutor.translate(texto,dest='en')
print('Texto em ingles: ', ingles.text)

