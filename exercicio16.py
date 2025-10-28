('''
import math
num = float(input("digite um numero: "))
raiz = math.sqrt(num)
print(f'a raiz de {num} é igual a {raiz:.0f}')
''')

#outra forma de utilizar modulo

from math import sqrt,floor
num = float(input("digite um numero: "))
raiz = sqrt(num)
print(f'a raiz de {num} é igual a {raiz}')
