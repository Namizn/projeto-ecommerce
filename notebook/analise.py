import pandas as pd
import matplotlib.pyplot as plt
import os

# caminho
base_dir = os.path.dirname(__file__)
caminho = os.path.join(base_dir, '..', 'data', 'data.csv')

df = pd.read_csv(caminho, encoding='ISO-8859-1')

# remover nulos importantes
df = df.dropna(subset=['InvoiceNo', 'Quantity', 'UnitPrice', 'Country'])

# criar coluna de receita
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# converter data
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])


# 1. faturamento total
total = df['Revenue'].sum()
print("Faturamento total:", total)


# 2. países que mais compram
pais = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(10)
print("\nTop países:")
print(pais)

pais.plot(kind='bar')
plt.title('Top Países por Receita')
plt.tight_layout()
plt.show()


# 3. produtos mais vendidos
produtos = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
print("\nTop produtos:")
print(produtos)

produtos.plot(kind='bar')
plt.title('Top Produtos Vendidos')
plt.tight_layout()
plt.show()


# 4. vendas por mês
df['Month'] = df['InvoiceDate'].dt.to_period('M')
mes = df.groupby('Month')['Revenue'].sum()

mes.plot(kind='line')
plt.title('Receita ao longo do tempo')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()