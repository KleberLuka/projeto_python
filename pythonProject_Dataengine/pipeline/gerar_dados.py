#gera os dados falsos com a biblioteca faker

from faker import Faker
import pandas as pd

fake = Faker('pt_BR')
def gerar_dados(qtd):
    return pd.DataFrame([{
        'nome': fake.name(),
        'email': fake.email(),
        'idade': fake.random_int(min=18, max=45),
        'cidade': fake.city(),
        'pais': fake.country()
    } for _ in range(qtd)])

df1 = gerar_dados(3500)
df2 = gerar_dados(3500)
df3 = gerar_dados(3500)

df1.to_csv('data/dados1.csv', index=False)
df2.to_parquet('data/dados2.parquet', index=False)
df3.to_feather('data/dados3.feather')

