import numpy as np
'''=====NUMPY====='''
notas = [7.5, 8.0, 6.5, 9.0, 7.0]
notas_array = np.array(notas)

print(type(notas))        # <class 'list'>
print(type(notas_array))  # <class 'numpy.ndarray'>
print(notas_array)         # [7.5 8.  6.5 9.  7. ]

print(notas_array + 1)

# De 0 até 9
a = np.arange(10)
print(a)  # [0 1 2 3 4 5 6 7 8 9]
 
# De 2 até 10 (sem incluir 10), de 2 em 2
b = np.arange(2, 10, 2)
print(b)  # [2 4 6 8]
 
# Funciona com decimais!
c = np.arange(0, 1, 0.2)
print(c)  # [0.  0.2 0.4 0.6 0.8]

'''=====LINSPACE====='''

# 5 números entre 0 e 1 (incluindo ambos)
d = np.linspace(0, 1, 5)
print(d)  # [0.   0.25 0.5  0.75 1.  ]
 
# 4 números entre 0 e 10
e = np.linspace(0, 10, 4)
print(e)  # [ 0.          3.33333333  6.66666667 10.        ]



'''!!!DICA!!!
Dica: Use arange quando sabe o passo (de quanto em quanto).
Use linspace quando sabe a quantidade de pontos que quer.












