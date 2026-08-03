#EXEMPLOS
import csv
#escreve no arquivo csv
'''
dados = [
    ['nome','nota', 'turma'],
    ['Ana',10.0,'1E'],
    ['Arthur', 8.5,'1E'],
    ['Lucas', 8.5, '1E']
]

with open('turma.csv', 'w', encoding = 'utf-8', newline = '') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)
'''
#lê o arquivo csv
'''
with open('turma.csv', 'r', encoding = 'utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
'''
#Q5
'''
dados = [
    ['nome', 'nota1', 'nota2'],
]


alunos = 0
while alunos < 3:
    nome = input('Diga o nome do aluno:')
    n1 = int(input('Diga a nota do aluno:'))
    n2 = int(input('Diga outra nota do aluno:'))

    dados.append([nome, n1, n2])
    alunos +=1
    
with open('turma.csv', 'w', encoding = 'utf-8', newline = '') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in dados:
        escritor.writerow(linha)
'''
#Q6
'''
notas = [
    ['nome', 'nota1', 'nota2', 'nota3'],
    ['Ana', 7.5, 8.0, 9.0],
    ['Beto', 5.0, 6.0, 4.5],
    ['Carla', 9.0, 9.5, 10.0],
    ['Diego', 6.0, 7.0, 5.5]
    ]

with open('notas.csv', 'w', encoding = 'utf-8', newline = '') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in notas:
        escritor.writerow(linha)

with open('notas.csv', 'r', encoding = 'utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        nome = linha['nome']
        n1 = float(linha['nota1'])
        n2 = float(linha['nota2'])
        n3 = float(linha['nota3'])
        media = (n1+n2+n3)/3
        if media >= 6:
            status = 'Aprovado'
        else:
            status = 'Reprovado'
        print(f'nome:{nome} média:{media} {status}')
'''
#Q7 - incompleto
'''
notas = [
    ['nome', 'nota1', 'nota2', 'nota3'],
    ['Ana', 7.5, 8.0, 9.0],
    ['Beto', 5.0, 6.0, 4.5],
    ['Carla', 9.0, 9.5, 10.0],
    ['Diego', 6.0, 7.0, 5.5]
    ]

with open('notas_com_media.csv', 'w', encoding = 'utf-8', newline = '') as arquivo:
    escritor = csv.writer(arquivo)
    for linha in notas:
        escritor.writerow(linha)

notas_com_media = [
    ['nome', 'nota1', 'nota2', 'nota3', 'media'],
    ]

with open('notas_com_media.csv', 'r', encoding = 'utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        nome = linha['nome']
        n1 = float(linha['nota1'])
        n2 = float(linha['nota2'])
        n3 = float(linha['nota3'])
        media = (n1+n2+n3)/3

        notas_com_media.append(['nome', n1, n2, n3, media])

        print(f'nome:{nome} média:{media}')
'''















