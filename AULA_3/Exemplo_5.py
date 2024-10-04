nome = input("informe o nome do produto que você adquiriu")
quantidade = int(input("Informe a quantidade desejada: "))
valor = float(input("Informe o valor unitário" ))
total = valor * quantidade
print(f"O valor total a ser pago é R$ {total:.2f}")
if quantidade <= 5:
   desc = total * 0,98
elif quantidade > 5 and quantidade <= 10:
   desc = total * 0,97
else:
   desc = total * 0,95
   print(f"O valor total com desconto é R$ {desc:.2f}")

     