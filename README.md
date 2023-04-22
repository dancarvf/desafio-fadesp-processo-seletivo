# Desafio Técnico.

## Objetivos
### Objetivo 1: Baixe a base de dados completa e carregue dentro de DataFrame do pandas.	
Importar a biblioteca necessária para carregar os dados da URL dentro de um DataFrame da biblioteca Pandas __(DESAFIO 1)__
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

__Os Dados foram carregados com sucesso diretamente do GitHub__
	 
  	
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
### Objetivo 4:
### Objetivo 5:

 



