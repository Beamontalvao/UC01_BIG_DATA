# O programa deverá escrever a idade e o tempo trabalhado do empregado , acompanhado da seguinte mensagem: Apto a aposentadoria ou Inapto a aposentadoria.
try:
  idade = int(input("Informe é a Idade: "))
  tempo = int(input("Informe o tempo de trabalhado: "))
except ValueError:
     print("Verifique os dados informados")
else:
  if Idade >= 65:
     print("Apto para aposentadoria")
  elif Tempo >= 30
     print("Apto para aposentadoria")
  elif Idade >= 60 and tempo >= 25:
     print("apto para aposentadoria")
  else:
     print("Inapto a aposentadoria")



