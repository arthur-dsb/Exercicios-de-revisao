import numpy as np

#Q1
'''
a = np.arange(1, 11) #cria uma lista "a" de 1 a 10
print(a) #exibe a lista a: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a.shape) #exibe quantas dimensões o vetor tem: 1
print(a[::2]) #exibe o fatiamento da lista "a", em que vai do começo ao fim pulando de 2 em 2
print(a[::-1]) #exibe o fatiamento da lista "a", em que vai do começo ao fim pulando de -1 em -1
print(a.sum()) #xibe a soma de todos os elementos da lista "a"
print(a.mean()) #exibe a média da lista "a"
print(a[a > 5]) #exibe uma lista que contém só os elementos maiores que 5 da lista "a"
print(a[a % 3 == 0]) #exibe uma lista que contém só os elementos múltiplos de 3 da lista "a"
'''
#Q2
'''
notas = [7.5, 6.0, 8.5, 7.0]
notas_array = np.array(notas)
#a)
print(f"Média anual: {notas_array.mean()}") #7.25

#b)
print(f"Menor nota: {notas_array.min()}")
print(f"Maior nota: {notas_array.max()}")

#c)
filtro = notas_array > notas_array.mean()
print(notas_array[filtro])

#d)
print(np.round(notas_array))

'''
#Q3
'''
#a)
precos = [19.90, 35.50, 42.00, 8.90, 120.00, 55.00]
precos_array = np.array(precos)
print(precos_array)

#b)
novos_precos = precos_array *0.85 
print(novos_precos)

#c)
filtro = novos_precos > 30
print(novos_precos[filtro])

#d)
print(np.sum(novos_precos))
'''
#Q4
'''
import numpy as np

# Objetivo: criar um array de temperaturas e analisar
temperaturas = np.array([22, 25, 19, 30, 28, 21]) #retirar aspas duplas

media = temperaturas.sum() / len(temperaturas)
print("Média:", media)
 
acima_media = temperaturas[temperaturas > media]
print("Acima da média:", acima_media)
 
# Converter Celsius para Fahrenheit
fahrenheit = temperaturas * 9/5 + 32
print("Em Fahrenheit:", fahrenheit)
'''

















