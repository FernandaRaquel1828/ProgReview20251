n = int(input("digite um numero para que possamos calcular sua tabuada:"))
print(f'{"="*30} \nEssa é a tabuada de {n}')

for i in range(1,10):
    print(f"{n} x {i} = {n * i}")
print("="*30)