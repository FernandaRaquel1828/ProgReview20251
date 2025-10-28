dias = int(input("quantos dias alugados? "))
km = int(input("quantos km rodados? "))

diastotais = dias * 60
kmtotais = km * 0.15

print(f"valor a ser pago é R${diastotais + kmtotais:.2f} ")

