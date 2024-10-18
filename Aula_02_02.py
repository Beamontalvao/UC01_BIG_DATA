# código usando séries
import pandas as pd 
media = pd.Series([80,90,10,20,30,40,70,100,30,50])
ap = media[media >= 70]
rp = media[media < 70]
print("medias maiores que 70")
print(ap)
print("medias menores que 70")
