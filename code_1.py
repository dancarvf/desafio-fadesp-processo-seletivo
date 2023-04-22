# importar bibliotecas necessárias
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import seaborn as sns
url = 'https://raw.githubusercontent.com/jralbbuquerque/desafio-fadesp-processo-seletivo/master/data/dataset_desafio_fadesp.csv'
df = pd.read_csv(url, encoding='iso-8859-1')
print((df))
df.isnull().sum()
print(df.isnull().sum())
df.duplicated().sum()
print(df.duplicated().sum())
media = df['Sales'].mean()
mediana = df['Sales'].median()
desvio_padrao = df['Sales'].std()
variancia = df['Sales'].var()
minimo = df['Sales'].min()
maximo = df['Sales'].max()

# Exibir as medidas descritivas calculadas
print('Média: {:.2f}'.format(media))
print('Mediana: {:.2f}'.format(mediana))
print('Desvio Padrão: {:.2f}'.format(desvio_padrao))
print('Variância: {:.2f}'.format(variancia))
print('Mínimo: {:.2f}'.format(minimo))
print('Máximo: {:.2f}'.format(maximo))
plt.figure()
df.boxplot(column='Sales')

# Adicionar um título e rótulos aos eixos x e y
plt.title('Boxplot da coluna Sales')
plt.xlabel('Sales')
plt.ylabel('Valores')

# Exibir o boxplot
plt.show()
# Quantidade de produtos por região
df_region_qtd = df.groupby('Region')['Quantity'].sum()
ax = df_region_qtd.plot(kind="bar")
ax.set_xlabel('Região')
ax.set_ylabel('Quantidade de Produtos')
ax.set_title('Quantidade de produtos por região')
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.yaxis.offsetText.set_visible(False)
ax.set_yticklabels(['{:.0f}'.format(x/1) for x in ax.get_yticks()])
plt.show()
# Vendas por região
df_region_sales = df.groupby('Region')['Sales'].sum()
ax = df_region_sales.plot(kind="bar")
ax.set_xlabel('Região')
ax.set_ylabel('Valor de Venda (em milhões)')
ax.set_title('Vendas por região')
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.yaxis.offsetText.set_visible(False)
ax.set_yticklabels(['{:.2f}'.format(x/1000000) for x in ax.get_yticks()])
plt.show()
# Lucro por região
df_region_prft = df.groupby('Region')['Profit'].sum()
ax = df_region_prft.plot(kind="bar")
ax.set_xlabel('Região')
ax.set_ylabel('Lucro (em milhares)')
ax.set_title('Lucro por região')
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.yaxis.offsetText.set_visible(False)
ax.set_yticklabels(['{:.2f}'.format(x/1000) for x in ax.get_yticks()])
plt.show()
# Quantidade de produtos por Pais
df_country_qtd = df.groupby('Country')['Quantity'].sum()
ax = df_country_qtd.plot(kind="bar")
ax.set_xlabel('País')
ax.set_ylabel('Quantidade de Produtos')
ax.set_title('Quantidade de produtos por País')
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.yaxis.offsetText.set_visible(False)
ax.set_yticklabels(['{:.0f}'.format(x/1) for x in ax.get_yticks()])
plt.show()
# Vendas por Pais
df_country_sales = df.groupby('Country')['Sales'].sum()
ax = df_country_sales.plot(kind="bar")
ax.set_xlabel('País')
ax.set_ylabel('Valor de Venda (em milhões)')
ax.set_title('Vendas por País')
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.yaxis.offsetText.set_visible(False)
ax.set_yticklabels(['{:.2f}'.format(x/1000000) for x in ax.get_yticks()])
plt.show()
# Lucro por Pais - É possível verificar que há paises que houveram Loss
df_country_prft = df.groupby('Country')['Profit'].sum()
ax = df_country_prft.plot(kind="bar")
ax.set_xlabel('Páis')
ax.set_ylabel('Lucro (em milhares)')
ax.set_title('Lucro pore País')
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.yaxis.offsetText.set_visible(False)
ax.set_yticklabels(['{:.2f}'.format(x/1000) for x in ax.get_yticks()])
plt.show()
# Paises que houveram Loss
df_country_loss = df.groupby('Country')['Profit'].sum()
df_negative_profit = df_country_loss[df_country_loss < 0]
ax = df_negative_profit.plot(kind="bar")
ax.set_xlabel('País')
ax.set_ylabel('Loss (em milhares)')
ax.set_title('Países com Loss')
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.yaxis.offsetText.set_visible(False)
ax.set_yticklabels(['{:.2f}'.format(x/1000) for x in ax.get_yticks()])
plt.show()
# Os produtos mais vendidos por continente (top10)
df_region_product = df.groupby(['Region', 'Product Name'])[
    'Quantity'].sum().reset_index()
df_sorted = df_region_product.sort_values(
    ['Quantity'], ascending=[False]).head(10).reset_index(drop=True)
print(df_sorted)
# Os produtos mais vendidos por Pais (top10)
df_country_product = df.groupby(['Country', 'Product Name'])[
    'Quantity'].sum().reset_index()
df_sorted = df_country_product.sort_values(
    ['Quantity'], ascending=[False]).head(10).reset_index(drop=True)
print(df_sorted)
# Os produtos mais vendidos por Estado (top10)
df_state_product = df.groupby(['State', 'Product Name'])[
    'Quantity'].sum().reset_index()
df_sorted = df_state_product.sort_values(
    ['Quantity'], ascending=[False]).head(10).reset_index(drop=True)
print(df_sorted)
# Os produtos mais vendidos por Cidade (top10)
df_city_product = df.groupby(['City', 'Product Name'])[
    'Quantity'].sum().reset_index()
df_sorted = df_city_product.sort_values(
    ['Quantity'], ascending=[False]).head(10).reset_index(drop=True)
print(df_sorted)

# Vizualização de alguns dados
# gráfico de dispersão entre Sales e descontos.
plt.scatter(df['Sales'], df['Discount'])
plt.xlabel('Vendas')
plt.ylabel('Desconto')
plt.title('Relação entre Vendas e Desconto')
plt.show()
# Vendas com shipping cost
plt.scatter(df['Sales'], df['Shipping Cost'])
plt.xlabel('Vendas')
plt.ylabel('Shipping Cost')
plt.title('Relação entre Vendas e Custo de Envio')
plt.show()
