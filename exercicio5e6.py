'''
nome = input("qual o seu nome? ")
print(f"Prazer em te conhecer {nome:=^20}!!!! ")

n1=int(input("um valor: "))
n2=int(input("outro valor: "))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print(f'a soma é {s},o produto é {m} e a divisão é {d:.3f}',end="")
print(f'divisao inteira {di} e a potencia {e}')
'''
n= int(input("digite um numero: "))
#print(f'o antecessor de {n} é {n -1}, seu sucessor é {n+1}\n o dobro de {n} é {n*2}, o triplo {n*3}, a raiz quadrada é {n**(1/2)}')
print(f"{pow(n, (1/2)):.0f}")