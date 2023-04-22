# Desafio Técnico.

## Objetivos
### Objetivo 1: Baixe a base de dados completa e carregue dentro de DataFrame do pandas.	
Importar a biblioteca necessária para carregar os dados da URL dentro de um DataFrame da biblioteca Pandas 
```python
import pandas as pd
```
Utilizar o link que contem os dados em CSV com separação por "," e abrir com a função "pd.read_csv"
```python
url = 'https://raw.githubusercontent.com/jralbbuquerque/desafio-fadesp-processo-seletivo/master/data/dataset_desafio_fadesp.csv'
df = pd.read_csv(url,encoding='iso-8859-1')
```
Verificar se o carregamento foi bem sucedido
```python
print(df)
```
```
       Row ID         Order ID  Order Date Ship Date       Ship Mode Customer ID     Customer Name  ...                                     Product Name    Sales Quantity Discount    Profit Shipping Cost Order Priority
0       42433     AG-2011-2040    1/1/2011  6/1/2011  Standard Class    TB-11280   Toby Braunhardt  ...                              Tenex Lockers, Blue  408.300        2      0.0  106.1400         35.46         Medium       
1       22253    IN-2011-47883    1/1/2011  8/1/2011  Standard Class    JH-15985       Joseph Holt  ...                         Acme Trimmer, High Speed  120.366        3      0.1   36.0360          9.72         Medium       
2       48883     HU-2011-1220    1/1/2011  5/1/2011    Second Class      AT-735     Annie Thurman  ...                          Tenex Box, Single Width   66.120        4      0.0   29.6400          8.17           High       
3       11731  IT-2011-3647632    1/1/2011  5/1/2011    Second Class    EM-14140      Eugene Moren  ...                      Enermax Note Cards, Premium   44.865        3      0.5  -26.0550          4.82           High       
4       22255    IN-2011-47883    1/1/2011  8/1/2011  Standard Class    JH-15985       Joseph Holt  ...                       Eldon Light Bulb, Duo Pack  113.670        5      0.1   37.7700          4.70         Medium       
...       ...              ...         ...       ...             ...         ...               ...  ...                                              ...      ...      ...      ...       ...           ...            ...       
51285   32593   CA-2014-115427  31-12-2014  4/1/2015  Standard Class    EB-13975        Erica Bern  ...  Cardinal Slant-D Ring Binder, Heavy Gauge Vinyl   13.904        2      0.2    4.5188          0.89         Medium       
51286   47594     MO-2014-2560  31-12-2014  5/1/2015  Standard Class     LP-7095         Liz Preis  ...          Wilson Jones Hole Reinforcements, Clear    3.990        1      0.0    0.4200          0.49         Medium       
51287    8857   MX-2014-110527  31-12-2014  2/1/2015    Second Class    CM-12190  Charlotte Melton  ...           Hon Color Coded Labels, 5000 Label Set   26.400        3      0.0   12.3600          0.35         Medium       
51288    6852   MX-2014-114783  31-12-2014  6/1/2015  Standard Class    TD-20995     Tamara Dahlen  ...           Hon Legal Exhibit Labels, Alphabetical    7.120        1      0.0    0.5600          0.20         Medium       
51289   36388   CA-2014-156720  31-12-2014  4/1/2015  Standard Class    JM-15580     Jill Matthias  ...                              Bagged Rubber Bands    3.024        3      0.2   -0.6048          0.17         Medium       
```

__Os Dados foram carregados com sucesso diretamente do GitHub__ __(DESAFIO 1)__
	 
  	
### Objetivo 2: Realize um processo limpeza nos dados removendo ou substituindo os valores nulos quando necessário, e eliminando dados duplicados e inconsistentes caso exista algum. 

Verificar se há algum valor em branco em alguma linha
```python
df.isnull().sum()
print(df.isnull().sum())
```
Com a verificação dos valores nulos, temos:
```
[51290 rows x 24 columns]
Row ID                0
Order ID              0
Order Date            0
Ship Date             0
Ship Mode             0
Customer ID           0
Customer Name         0
Segment               0
City                  0
State                 0
Country               0
Postal Code       41296
Market                0
Region                0
Product ID            0
Category              0
Sub-Category          0
Product Name          0
Sales                 0
Quantity              0
Discount              0
Profit                0
Shipping Cost         0
Order Priority        0
dtype: int64
```
Há na coluna "Postal Code" 41296 valores nulos. Por se tratar de uma quantidade significativa dos dados, e tratando-se de uma variável de menor importância, será desconsiderado a retirada das linhas contendo os valores nulos, dessa forma, mantendo-se os dados como estão em relação a valores nulos. Lembrando que, como nenhum objetivo irá requerer o uso da coluna código postal, não será realizado alteração por essa razão.

Verificar se há valores duplicados
```python
df.duplicated().sum()  
print(df.duplicated().sum()
``` 
A verificação de valores repetidos foi:
```
0
```
Ou seja, não há valores duplicados. __Logo não será necessário limpar, eliminar dados duplicados ou substituir para os fins dessa atividade.__

Com os dados já adequados para a continuação da atividade, será realizado o armazenamento do dataset em um banco de dados chave-valor SQLite __(DESAFIO 2)__:

Importar a biblioteca apropriada:
```
import sqlite3
```
Criar conexão com banco de dados e armazenar o DF na tabela:
```
conn = sqlite3.connect('database.db')
df.to_sql('dataset', conn, if_exists='replace', index=False)
``` 
Realizar uma consulta SQL da tabela:
```
consulta = "SELECT Region FROM dataset"
df_resultado = pd.read_sql_query(consulta, conn)
print(df_resultado)
```
O retorno da consulta foi:
```       Region
0       Africa
1      Oceania
2         EMEA
3        North
4      Oceania
...        ...
51285     West
51286   Africa
51287  Central
51288    North
51289     West
```


### Objetivo 3: Utilize técnicas de visualização de dados para explorar a distribuição dos dados.

Das medidas das variáveis dos dados, é possível realizar algumas vizualizações importantes, como uma análise geral das vendas totais a partir de um gráfico de boxplot:
```
plt.figure()
df.boxplot(column='Sales')

# Adicionar um título e rótulos aos eixos x e y
plt.title('Boxplot da coluna Sales')
plt.xlabel('Sales')
plt.ylabel('Valores')

# Exibir o boxplot
plt.show()
```


__Img1__

A partir do boxplot, é possível verificar que há uma grande variabilidade dos dados de Sales com um grande número de outliers superiores. 

Também é possível identificar a região com maior quantidade de produtos vendidos, maiores valores totais de vendas e maior lucro:
```
#Quantidade de produtos por região
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
#Lucro por região
df_region_prft = df.groupby('Region')['Profit'].sum()
ax = df_region_prft.plot(kind="bar")
ax.set_xlabel('Região')
ax.set_ylabel('Lucro (em milhares)')
ax.set_title('Lucro por região')
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.yaxis.offsetText.set_visible(False)
ax.set_yticklabels(['{:.2f}'.format(x/1000) for x in ax.get_yticks()])
plt.show()
```
IMG2, IMG3 e IMG4

Também podemos realizar a mesma análise com relação aos Paises:

```
#Quantidade de produtos por Pais
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
#Lucro por Pais - É possível verificar que há paises que houveram Loss
df_country_prft = df.groupby('Country')['Profit'].sum()
ax = df_country_prft.plot(kind="bar")
ax.set_xlabel('Páis')
ax.set_ylabel('Lucro (em milhares)')
ax.set_title('Lucro pore País')
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.yaxis.offsetText.set_visible(False)
ax.set_yticklabels(['{:.2f}'.format(x/1000) for x in ax.get_yticks()])
plt.show()
```
IMG5 IMG6 e IMG 7

Percebesse que em alguns países houve um prejuizom, dessa forma, é válido verificar qual o coportamento do prejuizo a partir do gráfico:

```
#Paises que houveram Loss
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
```
IMG 8



### Objetivo 4: Identifique os produtos mais vendidos e analise sua distribuição geográfica.

Para identificar os produtos mais vendidos no contexto de distribuição geográfica, foram agrupados em df por localização geográfica e o 'Product Name' e calculado pela soma de 'Quantity'. Após essa verificação, foram agrupados em um novo df de forma decrecente os primeiros 10 da lista para determinar os 10 produtos mais vendidos por reigão:
- __Por região__
```
df_region_product = df.groupby(['Region', 'Product Name'])['Quantity'].sum().reset_index()
df_sorted = df_region_product.sort_values(['Quantity'], ascending=[False]).head(10).reset_index(drop=True)
print(df_sorted)
```
Logo temos como os produtos mais vendidos por Região:
```
    Region                           Product Name  Quantity
0     East                                Staples       267
1  Central                                Staples       249
2     West                                Staples       216
3    South                                Staples       144
4  Central   Sanford Pencil Sharpener, Easy-Erase        96
5  Central          Eldon File Cart, Single Width        91
6  Central      Cardinal Binding Machine, Economy        74
7  Central                 Ibico Index Tab, Clear        73
8  Central  Stockwell Paper Clips, Assorted Sizes        70
9  Central        Cardinal Binding Machine, Clear        68
```
- __Por País__
```
df_country_product = df.groupby(['Country', 'Product Name'])['Quantity'].sum().reset_index()
df_sorted = df_country_product.sort_values(['Quantity'], ascending=[False]).head(10).reset_index(drop=True)
print(df_sorted)
```
Logo, temos como produtos mais vendidos por Páis:
```
 Country                                       Product Name  Quantity
0  United States                                            Staples       876
1  United States                         KI Adjustable-Height Table        74
2  United States                            Avery Non-Stick Binders        71
3  United States                            Storex Dura Pro Binders        71
4  United States  GBC Premium Transparent Covers with Diagonal L...        67
5  United States         Situations Contoured Folding Chairs, 4/Set        64
6  United States                 Chromcraft Round Conference Tables        61
7  United States                        Eldon Wave Desk Accessories        61
8  United States    Global Wood Trimmed Manager's Task Chair, Khaki        59
9  United States  Wilson Jones Turn Tabs Binder Tool for Ring Bi...        59
```
- __Por Estado__
```
df_state_product = df.groupby(['State', 'Product Name'])['Quantity'].sum().reset_index()
df_sorted = df_state_product.sort_values(['Quantity'], ascending=[False]).head(10).reset_index(drop=True)
print(df_sorted)
```
Logo, temos como produtos mais vendidos por Estado:
```
             State                       Product Name  Quantity
0        California                            Staples       162
1          New York                            Staples       125
2             Texas                            Staples       109
3          Illinois                            Staples        66
4              Ohio                            Staples        47
5      Pennsylvania                            Staples        46
6           Florida                            Staples        37
7        California  Eldon Shelf Savers Cubes and Bins        29
8  National Capital  Advantus Stacking Tray, Erganomic        28
9        California       4009 Highlighters by Sanford        27
```
- __Por Cidade__
```
df_city_product = df.groupby(['City', 'Product Name'])['Quantity'].sum().reset_index()
df_sorted = df_city_product.sort_values(['Quantity'], ascending=[False]).head(10).reset_index(drop=True)
print(df_sorted)
```
Logo, temos como produtos mais vendidos por Cidade:
```
          City                  Product Name  Quantity
0  New York City                       Staples        92
1    Los Angeles                       Staples        65
2        Houston                       Staples        61
3  San Francisco                       Staples        50
4   Philadelphia                       Staples        42
5        Chicago                       Staples        40
6       Columbus                       Staples        32
7    Tegucigalpa     Acco Binder Covers, Clear        25
8    Mexico City  Cisco Smart Phone, Full Size        25
9         Manila   Acco Binder Covers, Durable        23
```
___Dessa forma, temos os produtos mais vendidos e suas distribuições geográficas__

### Objetivo 5: Analise a relação entre as vendas e outras variáveis, como o tempo de entrega e o preço dos produtos.

 



