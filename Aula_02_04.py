import pandas as pd
temperaturas = [21.1,32.5,16.1,40.4,28.0,30.8,22.0]
media_temperatura = sum(temperaturas) / len(temperaturas)
print(f"A Temperatura media dos ultimos 7 dias é: {media_temperatura:.2f}°c")