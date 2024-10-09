# Lista para armazenar os dados dos habitantes
dados_habitantes = []

# Coleta de dados
while True:
    print("\nDigite os dados do habitante (ou 'sair' para finalizar):")
    sexo = input("Sexo (masculino/feminino): ").lower()
    cor_olhos = input("Cor dos olhos (azuis/verde/castanho): ").lower()
    cor_cabelos = input("Cor dos cabelos (louros/castanhos/pretos): ").lower()
    idade = input("Idade: ")

    if idade.lower() == 'sair':
        break

    try:
        idade = int(idade)
    except ValueError:
        print("Idade deve ser um número. Tente novamente.")
        continue

    dados_habitantes.append((sexo, cor_olhos, cor_cabelos, idade))

# Verifica se há dados coletados
if dados_habitantes:
    # a) Maior, menor idade e média das idades
    idades = [hab[3] for hab in dados_habitantes]
    maior_idade = max(idades)
    menor_idade = min(idades)
    media_idades = sum(idades) / len(idades)

    # b) Quantidade de mulheres entre 18 e 35 anos
    quantidade_mulheres_18_35 = sum(1 for hab in dados_habitantes if hab[0] == 'feminino' and 18 <= hab[3] <= 35)

    # c) Quantidade de indivíduos com olhos verdes e cabelos louros
    quantidade_olhos_verdes_cabelos_louros = sum(1 for hab in dados_habitantes if hab[1] == 'verde' and hab[2] == 'louros')

    # Exibir resultados
    print(f"\nMaior idade: {maior_idade}")
    print(f"Menor idade: {menor_idade}")
    print(f"Média das idades: {media_idades:.2f}")
    print(f"Quantidade de mulheres entre 18 e 35 anos: {quantidade_mulheres_18_35}")
    print(f"Quantidade de indivíduos com olhos verdes e cabelos louros: {quantidade_olhos_verdes_cabelos_louros}")
else:
    print("Nenhum dado foi coletado.")
