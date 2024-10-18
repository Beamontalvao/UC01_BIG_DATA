# O Gerente de uma loja pediu o seu auxílio para que a cada 7 dias, calculasse a média do valor vendido, o maior
# valor vendido e o menor valor vendido de seus 3 vendedores/as. Pediu para que fosse algo automatizado, pois como ele está em
# fase de expansão, nos próximos meses mais 4 vendedores serão contratados e sua análise deve estar pronta para isso.

import pandas as pd

# Dados de vendas
vendas = {
    "Maria": [800, 700, 1000, 900, 1200, 600, 600],
    "João": [900, 500, 1100, 1000, 900, 500, 700],
    "Manuel": [700, 600, 900, 1200, 900, 700, 400],
}

# Criar um DataFrame
df = pd.DataFrame(vendas)

# Calcular as estatísticas
estatisticas = {
    "média": df.mean(),
    "maior": df.max(),
    "menor": df.min(),
}

# Converter as estatísticas para um DataFrame
estatisticas_df = pd.DataFrame(estatisticas)

# Exibir os resultados
print("Resultados de vendas dos últimos 7 dias:")
print(estatisticas_df)
