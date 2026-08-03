#Q1
'''
with open ('exercicio.txt', 'w', encoding = 'utf-8') as arquivo:
    arquivo.write('Maçã \nUva \nMelancia \nLaranja \nBanana')
    
with open('exercicio.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip()) # strip remove o \n do final
'''
#Q2
'''
with open ('compras.txt', 'w', encoding = 'utf-8') as arquivo:
    while True:
        item = input('Digite um item:')
        if item == 'sair':
            break

        arquivo.write(f'{item} \n')

with open('compras.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(linha.strip())
'''
#Q3
'''
from datetime import datetime
agora = datetime.now().strftime('%d/%m/%Y %H:%M')
while True:
    anotacao = input('Faça uma anotação:')
    if anotacao == 'sair':
        break
    with open ('diario.txt', 'a', encoding = 'utf-8') as arquivo:
        arquivo.write(f'{agora}\n{anotacao}\n')
'''
#Q4
'''
total_palavras = 0
with open('diario.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        palavras = linha.split()
        total_palavras += len(palavras)
        
    print(f'O arquivo tem: {len(linhas)} linhas')
    print(f'O arquivo tem: {total_palavras} palavras')
'''

















