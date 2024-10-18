roubos = [100, 90, 80, 120, 110, 90, 70]
furtos = [80, 60, 70, 60, 100, 50, 30]
recuperacoes = [70, 50, 90, 80, 100, 70, 50]
total_roubos_furtos_diario = [roubo + furto for roubo, furto in zip(roubos, furtos)]
taxa_recuperacao_diaria = [
    (recuperacao / roubo) * 100 if roubo > 0 else 0
    for recuperacao, roubo in zip(recuperacoes, roubos)
]
print("Quantidade de roubos + furtos diários nos últimos 7 dias:")
for dia, total in enumerate(total_roubos_furtos_diario, start=1):
    print(f"Dia {dia}: {total} casos")
print("\nTaxa de recuperação de automóveis diária (%):")
for dia, taxa in enumerate(taxa_recuperacao_diaria, start=1):
    print(f"Dia {dia}: {taxa:.2f}%")