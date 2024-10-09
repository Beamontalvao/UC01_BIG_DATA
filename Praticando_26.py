# O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um
# programa que armazene em um vetor um conjunto indeterminado de temperaturas, ao final
# informe a menor, a maior e a média das temperaturas.

temperaturas = []

# Loop para coletar as temperaturas
while True:
    entrada = input("Digite uma temperatura (ou 'sair' para finalizar): ")
    
    if entrada.lower() == 'sair':
        break  # Encerra o loop se o usuário digitar 'sair'
    
    try:
        temperatura = float(entrada)  # Converte a entrada para float
        temperaturas.append(temperatura)  # Adiciona a temperatura à lista
    except ValueError:
        print("Por favor, insira um número válido ou 'sair' para finalizar.")

if temperaturas:
    menor_temperatura = min(temperaturas)
    maior_temperatura = max(temperaturas)
    media_temperaturas = sum(temperaturas) / len(temperaturas)

    print(f"\nMenor temperatura: {menor_temperatura:.2f}°C")
    print(f"Maior temperatura: {maior_temperatura:.2f}°C")
    print(f"Média das temperaturas: {media_temperaturas:.2f}°C")
else:
    print("Nenhuma temperatura foi registrada.")
