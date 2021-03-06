# -*- coding: utf-8 -*-
"""
# Introdução à linguagem Python

## Objetos

O Python entende o significado, ou melhor, o valor de algo, quando esse algo está contido por um objeto. Exemplo:
"""

meu_primeiro_objeto = 15

"""A partir de agora "meu_primeiro_objeto", para o Python, é um objeto com valor igual a 15. Podemos verificar isso declarando o objeto:"""

meu_primeiro_objeto

"""Podemos, inclusive, efetuar algumas operações com o nosso primeiro objeto:"""

15+2

"""É o mesmo que:"""

meu_primeiro_objeto + 2

"""## Operadores

### Soma
"""

2 + 2

"""### Subtração"""

3 - 1

"""### Multiplicação"""

4 * 5

"""### Divisão"""

12 / 3

"""### Exponenciação"""

7 ** 2

"""### Sequências"""

list(range(0, 10))

"""### Comparação de igualdade"""

3 == 3

"""### Comparação de diferença"""

5 != 0

"""### Maior que"""

2 > 9

"""### Menor que"""

1 < 8

"""### Maior ou igual"""

5 >= 5

"""### Menor ou igual"""

4 <= 1

"""## Objetos e operadores

Podemos utilizar esses operadores, tranquilamente, com o nosso primeiro objeto.

Deve-se haver o cuidado sobre o desejo de se sobrescrever objetos.
"""

meu_primeiro_objeto = 160

"""Em nível de código, o Python não vai te perguntar sobre a certeza de se querer fazer algo. Atenção a isso!

Também podemos guardar valores textuais em objetos:
"""

nome = usp

"""O Python reportou um erro. Por quê?"""

nome_1 = "usp"
nome_1

"""Ou:"""

nome_2 = 'usp'
nome_2

"""Podemos utilizar alguns operadores aprendidos anteriormente:"""

nome_1 == nome_2

nome_1 != nome_2

"""É possível guardar valores lógicos em objetos:"""

verdadeiro = nome_1 == nome_2
verdadeiro

falso = nome_1 != nome_2
falso

"""**Outros valores importantes:**"""

True

False

# Equivalente ao NULL
None

# Equivalente ao NA
import numpy as np
np.nan

# Equivalente a Inf
float('inf')
float('-inf')

import math
sum = math.inf

"""## Vetores

Podemos guardar bases de dados inteiras em objetos, porém, antes, devemos pensar sobre como guardar mais de uma informação em um objeto.
"""

# Equivalente ao c()
vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor

"""O exposto, de forma análoga, vale para valores textuais:"""

nomes = ["mariana", "pedro", "daniela"]
nomes

"""## Funções

Funções são tipos especiais de objetos no Python, cujo nome vem seguido de parênteses. Equivalem a ordens diretas à máquina.

Funções são algoritmos. Cada algoritmo possui suas próprias atribuições e carrega dentro de si seu processo decisório.

Vamos utilizar um exemplo para esclarecer o assunto:
"""

round(number=3.141592)

"""No comando anterior, não houve a criação de objeto algum. Houve a declaração de uma função cujo objetivo é o arredondamento numérico, em que "number" é um argumento da função.

Argumentos são complementos às ordens dadas. Imagine o seguinte caso:
"""

round()

"""Por que houve um erro?

Voltemos ao exemplo. Por que o R apenas transforma o valor de 3.141592 no valor inteiro 3?

Devemos complementar a ordem com um novo argumento:
"""

round(number = 3.141592, ndigits = 3)

"""Como saber quais os argumentos de uma dada função?"""

# Primeira maneira - NÃO FUNCIONA NO PYTHON REGULAR:
?round

# Segunda maneira, mais indicada
help(round)

# Terceira maneira, mais "específica"
import inspect
inspect.getfullargspec(round)

"""## Coerção

**Diferentemente do R, o Python não apresenta coerção de tipo!!!** Tipicamente, o Python não converte implicitamente um objeto para outro tipo de objeto.
"""

nomes_e_idades = ["mariana", 22, "pedro", 30, "daniela", 45]
nomes_e_idades

"""As observações que eram textos se mantiveram como textos, e as observações que eram números se mantiveram como números.

Podemos comprovar com a função type():
"""

# Tipo do objeto
print(type(nomes_e_idades))
# Tipo do primeiro item do objeto (no Python, indexação começa no ZERO!)
print(type(nomes_e_idades[0]))
# Tipo do segundo item do objeto (no Python, indexação começa no ZERO!)
print(type(nomes_e_idades[1]))

type(verdadeiro)

"""Da mesma maneira, também não há uma hierarquia básica de valores no Python como há no R.

## Variáveis categóricas

O R identifica suas variáveis categóricas como pertencentes à classe **factor**. O Python não apresenta um equivalente direto nativo, mas é possível chegar em um resultado similar com a biblioteca Pandas. Vamos criar um objeto que contenha o seguinte exemplo de variável categórica policotômica:
"""

tipo_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
tipo_sanguineo

type(tipo_sanguineo)

"""Para transformamos os valores internos ao objeto "tipo_sanguineo" em categorias, realizaremos o seguinte procedimento:"""

import pandas as pd
s = pd.Series(tipo_sanguineo, dtype="category")
s

type(s)

"""Observação:"""

tipo_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "A+", "A+"]
s = pd.Series(tipo_sanguineo, dtype="category")
s

"""Ainda há 8 níveis (categorias) após a modificação!

Para a utilização dos valores declarados em técnicas direcionadas a variáveis nominais, o procedimento acima basta e está completo.

Para o caso de variáveis ordinais, o trabalho deve ser estendido. Vamos criar um objeto com novas categorias:
"""

nivel_escolarizacao = ["fundamental", "médio", "graduação"]
s = pd.Series(nivel_escolarizacao, dtype="category")
s

"""Observe as categorias. Não é essa a ordem comumente aceita. Como faremos para o Python entender a ordem fundamental, médio, graduação?

Com o Pandas, é possível resolver essa questão de algumas maneiras:
"""

# Primeira maneira
nivel_esc = pd.Categorical(nivel_escolarizacao, categories=nivel_escolarizacao, ordered=True)
nivel_esc

# Segunda maneira
from pandas.api.types import CategoricalDtype
s = pd.Series(nivel_escolarizacao)
cat_type = CategoricalDtype(categories=nivel_escolarizacao, ordered=True)
s = s.astype(cat_type)
s

"""E se tivéssemos recebido uma base de dados cujos rótulos para as categorias fossem números? Vamos assumir o exemplo de que em dada base o valor "0" equivale a "não"; o valor "1" equivale a sim; e o valor "99" equivale a "talvez"."""

respostas = [0, 1, 1, 1, 99, 0, 99, 0, 0, 0, 1, 99]
respostas = pd.Series(respostas)
cat_type = CategoricalDtype(categories=[0, 99, 1], ordered=True)
respostas = respostas.astype(cat_type)
respostas

respostas = respostas.cat.rename_categories({0: "não", 99: "talvez", 1: "sim"})
respostas

"""## Juntando objetos para a criação de bases de dados"""

empresas = ["Empresa A", np.nan, "Empresa C", "Empresa D", "Empresa E"]
funcionarios = [100, 5000, 230, 12000, 1700]
presenca_bolsa = [False, True, np.nan, True, True]
sede_brasil = [np.nan, 0, 1, 0, 0]
diretor_executivo = [np.nan, "daniel", "carlos", "carla", "solange"]

"""Antes de juntarmos os vetores, devemos verificar se seus comprimentos são iguais:"""

print(len(empresas))
print(len(funcionarios))
print(len(presenca_bolsa))
print(len(sede_brasil))
print(len(diretor_executivo))

dados = pd.DataFrame(list(zip(empresas, funcionarios, presenca_bolsa, sede_brasil, diretor_executivo)),
                     columns=['empresas', 'funcionarios', 'presenca_bolsa', 'sede_brasil', 'diretor_executivo'])
dados

"""Para alterar os nomes das variáveis da nova base de dados, basta alterar os nomes no parâmetro *columns*! Também é possível realizar o seguinte procedimento:"""

dados.columns = ['companies', 'employees', 'stock_exchange', 'brazil_hq', 'ceo']
dados

"""## Salvando objetos carregados no R

Para salvar objetos, independentemente de sua classe (e.g. gráficos, bases de dados, modelos de machine learning, arquivos pdf, arquivos do Microsoft Office, etc.), **não há um equivalente ao formato .RData em Python!** Pode-se, como substituto, salvar dados no formato **Pickle**:
"""

dados.to_pickle("./dados.pkl")

"""Caso quiséssemos carregar os objetos salvos num outro momento, deveríamos utilizar a função read_pickle()."""

dados_df = pd.read_pickle("./dados.pkl")  
dados_df

"""## Carregando e salvando arquivos de alguns softwares/formatos mais utilizados

### Carregando e salvando .csv
"""

bicicletas = pd.read_csv('bicicletas.csv', delimiter=';')
bicicletas

"""**Observação**: nesse momento, em R, seria necessário instalar e carregar o pacote **readr**. Em Python, não será necessário, mas caso seja, utilizar **!pip install \<package\>** para instalar um pacote e **import \<package\>** para utilizá-lo.

Caso quiséssemos salvar o nosso dataframe 'dados' em formato *.csv:
"""

dados.to_csv('dados.csv', index=False)

"""### Carregando e salvando .xlsx"""

stricto_2018 = pd.read_excel('stricto_2018.xlsx')
stricto_2018

dados.to_excel("dados.xlsx")

"""### Carregando e salvando SPSS"""

!pip install pyreadstat

bolsa_estudos = pd.read_spss("bolsa_estudos.sav")
bolsa_estudos

import pyreadstat
pyreadstat.write_sav(dados, "dados.sav")

"""### Carregando e salvando Stata"""

vestibular = pd.read_stata('vestibular.dta')
vestibular

vestibular.to_stata('vestibular2.dta')

"""### Carregando .csv online"""

covid = pd.read_csv("https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv/data.csv",
                    encoding='utf-8')
covid.head(5)

"""## Introdução à manipulação de dados

Para ver a documentação ou buscar ajuda a respeito de algum pacote:
"""

help(pd)

"""O Pandas não possui bases de dados internas. Para obter uma base sample, podemos utilizar um pacote como o Statsmodels:"""

import statsmodels.api as sm

mtcars = sm.datasets.get_rdataset("mtcars", "datasets", cache=True).data
mtcars = pd.DataFrame(mtcars)
mtcars.head(5)

"""Se você está aqui é porque se interessa por dados, e pode ser que as bases de dados que você utiliza sejam extensas! Assim, vamos utilizar as funções head() e tail():"""

mtcars.head(5)

mtcars.tail(3)

"""Outra função interessante é a função info()"""

# Equivalente a str()
mtcars.info()

count_row = mtcars.shape[0]
print(count_row)
count_col = mtcars.shape[1]
print(count_col)
number_of_rows = len(mtcars)
print(number_of_rows)
mtcars_shape = mtcars.shape
print(mtcars_shape)

"""Podemos, ainda, ter acesso aos nomes das variáveis da base de dados com o auxílio da propriedade **columns**:"""

mtcars.columns

"""Podemos acessar uma variável da nossa base de dados com colchetes ou ponto:"""

mtcars['mpg'].head(3)

mtcars.cyl.head(3)

"""Também podemos acessar uma variável com o uso da função iloc[]:"""

mtcars.iloc[:, 10].head(3)

"""Podemos acessar as observações também com iloc[]:"""

mtcars.iloc[1, :]

"""Assim, é possível acessar valores específicos ao combinarmos o aprendido:"""

mtcars.iloc[2, 1]

"""Podemos, ainda, combinar as posições com o nome das variáveis:"""

mtcars.iloc[1]['mpg']

mtcars[['mpg', 'cyl', 'disp']].head(3)

"""Para filtrar valores, podemos também usar colchetes ou também a função **query()**.
Vamos supor que a intenção seja que o Python filtre todos os carros cujo valor para a variável mpg seja igual a 21:
"""

mtcars[mtcars['mpg'] == 21]

mtcars.query('mpg == 21')

"""Nesse momento é oportuno apresentar dois novos operadores:
* & significa "e"
* | significa "ou".

Por exemplo, carros cujo valor para a variável mpg seja igual a 21 E com a variável qsec menor do que 17:
"""

mtcars[(mtcars['mpg']==21) & (mtcars['qsec']<17)]

"""Carros cujo valor para a variável mpg seja igual a 21 OU com a variável qsec menor do que 17:"""

mtcars[(mtcars['mpg']==21) | (mtcars['qsec']<17)]

"""### Criando e excluindo variáveis em uma base de dados"""

mtcars['var_nova'] = np.nan
mtcars.head(3)

"""Para excluir uma coluna de nossa base de dados, utilizamos o comando **del**:"""

del mtcars['var_nova']
mtcars.head(3)

"""### Editando valores das observações

Podemos utilizar as funções **iat/at**:
"""

mtcars.iat[1, 1] = 82

mtcars.iloc[1, :]

"""Caso houvesse um padrão de repetição para uma determinada substituição, podemos usar a função replace (em substituição ao gsub, no R):"""

mtcars['cyl'] = mtcars['cyl'].replace(6, 8)
mtcars.head(5)

"""Vamos salvar as 3 primeiras observaçoes do dataset mtcars num objeto novo:"""

exemplo = mtcars.iloc[0:3,:]
exemplo

"""Agora vamos, propositalmente, repetir as observações da base de dados obtida por 3 vezes, usando a função **concat()**:"""

# Equivalente a rbind() no R
exemplo_final = pd.concat([exemplo, exemplo, exemplo])
exemplo_final

"""Aplicando a função **drop_duplicates()**:"""

# Equivalente a unique() no R
exemplo_final = exemplo_final.drop_duplicates()
exemplo_final
