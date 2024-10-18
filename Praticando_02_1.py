# O Ministro da Saúde, entrou em contato com você e te solicitou um auxílio, para obter as seguintes informações
# sobre os dados da vacinação da covid nos últimos quatro anos:
populacoes = [30000000, 25000000, 10000000, 5000000]
vacinados = [213317639, 214477744, 215574303, 216687971]  
populacao_vacinada = [30000000, 25000000, 10000000, 5000000]
populacao_total = [213317639, 214477744, 215574303, 216687971]
total_vacinados = sum(populacao_vacinada)
media_vacinados = total_vacinados / len(populacao_vacinada)
total_populacao = sum(populacao_total)
media_populacao = total_populacao / len(populacao_total)
taxa_vacinacao_anual = [(vacinados / total) * 100 for vacinados, total in zip(populacao_vacinada, populacao_total)]
print("Total de pessoas vacinadas:", total_vacinados)
print("Média de pessoas vacinadas:", media_vacinados)
print("Total da população do Brasil:", total_populacao)
print("Média da população do Brasil:", media_populacao)
print("Taxa de vacinação anual (%):", taxa_vacinacao_anual)
for ano, taxa in enumerate(taxa_vacinacao_anual, start=1):
    print(f"Taxa de vacinação no ano {ano}: {taxa:.2f}%")