#Q11
'''
contato = {
    'nome': 'João',
    'telefone': 123456789,
    'email': 'joao@gmail.com',
    'cidade': 'Viçosa-MG'
}

#a)
print(contato.items())

#b)
contato['instagram'] = 'joaomataporco_'
print(contato.items())

#c)
del contato['telefone']
print(contato.items())

#d)
if 'email' in contato:
    print(f'Email está no dicionário e é: {contato['email']}')

else:
    print('Não tem email cadastrado no dicionário contato!')
'''
#Q12
'''
frase = 'a rata roeu a roupa do rei de roma'

palavras = frase.split()

program = {}

for palavra in palavras:
    if palavra in program:
        program[palavra] += 1

    else:
        program[palavra] = 1

print(program)
'''
#Q13
'''
turma = {
    'Arthur': [9.0, 8.7, 10.0],
    'Ana Luiza': [8.0, 8.5, 7.0],
    'Lucas': [4.0, 7.0, 8.0],
    'Thamirys': [4.0, 5.0, 7.0]
}

for aluno in turma:
    media = (turma[aluno][0] + turma[aluno][1] + turma[aluno][2])/3
    situacao = 'Reprovado'
    if media >= 6.0:
        situacao = 'Aprovado'
    
    print(f'{aluno} - Média: {media} - {situacao}')
'''
#Q14
'''
info1 = {'nome': 'Notebook', 'preco': 3500.00}
info2 = {'marca': 'TechBrand', 'estoque': 15}

marged = info1 | info2
produto = marged

produto['preco'] = 3200.00
 

print(produto)
'''
#Q15
'''
Deus me livre
'''



















