#Listas
#Q1
'''
notas = [7.5, 8.0, 6.0, 9.5, 5.0]

a)
notas.append(8.5)
print(notas)

b)
notas[4] = 6.5
print(notas)


#c)
notas.sort(reverse=True)
print(notas)


#d)
print(max(notas))
print(min(notas
'''
#Q2
'''
nomes = ['Ana', 'Arthur', 'Laiza', 'Lucas', 'Thamis']

for i, nome in enumerate(nomes):
    print(f'{i+1}: {nome}')
'''
#Q3
'''
numeros = [3, 17, 8, 42, 5, 100, 23, 66, 11, 99]

pares = []

#a)
for num in numeros:
    if num%2 == 0:
        pares.append(num)

print(pares)

#b)
maioresQ20 = []
for num in numeros:
    if num > 20:
        maioresQ20.append(num)

print(maioresQ20)

#c
soma_total = sum(numeros)
print(soma_total)
'''
#Q4
'''
nums = list(range(1, 11))

#a)
print(nums [:4])

#b)
print(nums [7:])

#c)
print(nums [1: :2])
'''
#Q5
'''
turma = [['Ana',10.0], ['Arthur',9.0], ['Laiza', 3.0], ['Lucas', 3.5], ['Thamis', 3.0]]

for i, aluno in enumerate (turma):
    print(f'{turma[i][0]} tirou {turma[i][1]}')
'''
#Q6

lista_notas = [5.0, 7.0, 4.5, 9.0, 6.0, 3.0, 8.5]
aprov = []


def limpar_reprovados(lista_notas):
    for nota in lista_notas:
        if nota >= 6:
            aprov.append(nota)
    print(aprov)

limpar_reprovados(lista_notas)























