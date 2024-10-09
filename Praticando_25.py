#Faça um programe que pergunte quanto um funcionário recebe por hor e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário, sabendo que são descontados 11% do IRRF, imposto de renda, 8 % para INSS 
#E 5% para sindicato faça um programa que nos dê
#a) salário bruto.
#b) quanto pagou ao IRRF.
#c) quanto pagou ao INSS.
#d) quanto pagou ao sindicato.
#e) o salário líquido.


salario_por_hora = float(input("Digite o valor que o funcionário recebe por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_bruto = salario_por_hora * horas_trabalhadas
irrf = salario_bruto * 0.11  # Imposto de Renda (11%)
inss = salario_bruto * 0.08   # INSS (8%)
sindicato = salario_bruto * 0.05  # Sindicato (5%)
salario_liquido = salario_bruto - (irrf + inss + sindicato)
print(f"\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do IRRF: R$ {irrf:.2f}")
print(f"Desconto do INSS: R$ {inss:.2f}")
print(f"Desconto do Sindicato: R$ {sindicato:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
