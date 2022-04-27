# -*- coding: utf-8 -*-
"""
# Elaboração de gráficos em Python

Para a elaboração de gráficos, utilizaremos as funções do pacote **matplotlib, seaborn e plotly**.

De modo geral, a elaboração de um gráfico com esses pacotes não costuma ser uma tarefa difícil, desde que o aluno tenha em mente algumas coisas:

* Uma ideia clara de qual gráfico se quer elaborar;

* O entendimento de que as funções desses pacotes construirão um gráfico a partir de, necessariamente, um DataFrame (ou Series)

Obviamente, a depender das razões do discente, pode haver gráficos que dependerão de um nível alto de erudição no Python. Porém, para a maior das necessidades desse curso, o aluno encontrará soluções interessantes nos códigos abaixo.

Dito isso, vamos importar os pacotes necessários:
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns

"""## Gráfico de barras

Vamos carregar a base de dados que será utilizada para a construção de um gráfico de barras.
"""

# Para conseguir abrir os arquivos .RData da aula
!pip install pyreadr

import pyreadr

result = pyreadr.read_r('perfil_investidor.RData')

print(result.keys())
perfil_investidor = result["perfil_investidor"]
perfil_investidor.head(3)

"""Aplicando a sintaxe básica do matplotlib e do seaborn à base de dados:"""

# Necessário agrupar os valores de perfil usando value_counts()
fig, axes = plt.subplots(1, 1)
perfil_investidor['perfil'].value_counts().plot(kind='bar', ax=axes)
plt.show()

# Ou...
sns.countplot(data=perfil_investidor, x='perfil')

"""O primeiro gráfico, sem Seaborn, não apresenta os labels na ordem que desejamos. Para colocá-los em ordem, basta adicionar a ordem após o value_counts():"""

fig, axes = plt.subplots(1, 1)
perfil_investidor['perfil'].value_counts()[["Conservador", "Moderado", "Agressivo"]].plot(kind='bar', ax=axes)
plt.show()

"""Adicionando informações ao nosso gráfico:"""

fig, axes = plt.subplots(1, 1)
perfil_investidor['perfil'].value_counts()[["Conservador", "Moderado", "Agressivo"]].plot(kind='bar', ax=axes)
axes.set_title("Perfil dos Investidores do Banco X", size=16)
axes.set_xlabel("Perfil do Investidor")
axes.set_ylabel("Quantidade")
plt.show()

"""Adicionando detalhamentos ao gráfico:"""

fig, axes = plt.subplots(1, 1)
perfil_investidor['perfil'].value_counts()[["Conservador", "Moderado", "Agressivo"]].plot(kind='bar', ax=axes)
plt.suptitle("Perfil dos Investidores do Banco X", size=16)
plt.title("Banco X", size=12)
axes.set_xlabel("Perfil do Investidor")
axes.set_ylabel("Quantidade")
fig.text(.8, .05, "Período: 2021") # Alternativa para caption
plt.show()

"""Colocando os labels do eixo X na horizontal como no Seaborn:"""

fig, axes = plt.subplots(1, 1)
perfil_investidor['perfil'].value_counts()[["Conservador", "Moderado", "Agressivo"]].plot(kind='bar', ax=axes)
plt.suptitle("Perfil dos Investidores do Banco X", size=16)
plt.title("Banco X", size=12)
axes.set_xlabel("Perfil do Investidor")
plt.xticks(rotation=0)
axes.set_ylabel("Quantidade")
fig.text(.7, .02, "Período: 2021", size=12) # Alternativa para caption
plt.show()

"""Adicionando cores à plotagem:"""

fig, axes = plt.subplots(1, 1)
perfil_investidor['perfil'].value_counts()[["Conservador", "Moderado", "Agressivo"]].plot(kind='bar', ax=axes, color='darkorchid')
plt.suptitle("Perfil dos Investidores do Banco X", size=16)
plt.title("Banco X", size=12)
axes.set_xlabel("Perfil do Investidor")
plt.xticks(rotation=0)
axes.set_ylabel("Quantidade")
fig.text(.7, .02, "Período: 2021", size=12) # Alternativa para caption
plt.show()

"""Para verificar as cores possíveis de serem utilizadas no Matplotlib, pode-se acessar o seguinte endereço: https://matplotlib.org/3.5.0/gallery/color/named_colors.html

Adicionando bordas:
"""

fig, axes = plt.subplots(1, 1)
perfil_investidor['perfil'].value_counts()[["Conservador", "Moderado", "Agressivo"]].plot(
    kind='bar', ax=axes, color='darkorchid', edgecolor='black')
plt.suptitle("Perfil dos Investidores do Banco X", size=16)
plt.title("Banco X", size=12)
axes.set_xlabel("Perfil do Investidor")
plt.xticks(rotation=0)
axes.set_ylabel("Quantidade")
fig.text(.7, .02, "Período: 2021", size=12) # Alternativa para caption
plt.setp(axes.patches, linewidth=1)
plt.show()

"""Para modificar o fundo dos gráficos, há algumas opções:"""

fig, axes = plt.subplots(1, 1)
perfil_investidor['perfil'].value_counts()[["Conservador", "Moderado", "Agressivo"]].plot(
    kind='bar', ax=axes, color='darkorchid', edgecolor='black')
plt.suptitle("Perfil dos Investidores do Banco X", size=16)
plt.title("Banco X", size=12)
axes.set_xlabel("Perfil do Investidor")
plt.xticks(rotation=0)
axes.set_ylabel("Quantidade")
fig.text(.7, .02, "Período: 2021", size=12) # Alternativa para caption
plt.setp(axes.patches, linewidth=1)
fig.set_facecolor("lightgrey")
axes.set_facecolor("lightgrey")
plt.show()

with plt.style.context('ggplot'):
  fig, axes = plt.subplots(1, 1)
  perfil_investidor['perfil'].value_counts()[["Conservador", "Moderado", "Agressivo"]].plot(
      kind='bar', ax=axes, color='darkorchid', edgecolor='black')
  plt.suptitle("Perfil dos Investidores do Banco X", size=16)
  plt.title("Banco X", size=12)
  axes.set_xlabel("Perfil do Investidor")
  plt.xticks(rotation=0)
  axes.set_ylabel("Quantidade")
  fig.text(.7, .02, "Período: 2021", size=12) # Alternativa para caption
  plt.setp(axes.patches, linewidth=1)
  plt.show()

"""Adicionando labels nos valores:"""

fig, axes = plt.subplots(1, 1)
perfil_investidor['perfil'].value_counts()[["Conservador", "Moderado", "Agressivo"]].plot(
    kind='bar', ax=axes, color='darkorchid', edgecolor='black')
plt.suptitle("Perfil dos Investidores do Banco X", size=16)
plt.title("Banco X", size=12)
axes.set_xlabel("Perfil do Investidor")
plt.xticks(rotation=0)
axes.set_ylabel("Quantidade")
fig.text(.7, .02, "Período: 2021", size=12) # Alternativa para caption
plt.setp(axes.patches, linewidth=1)
fig.set_facecolor("lightgrey")
axes.set_facecolor("lightgrey")
for p in axes.patches:
    axes.annotate(p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()-1.2), ha='center', va='center',
                  xytext=(0, 10), textcoords='offset points')
plt.show()

"""Reposicionando labels:"""

fig, axes = plt.subplots(1, 1, figsize=(9,6))
perfil_investidor['perfil'].value_counts()[["Conservador", "Moderado", "Agressivo"]].plot(
    kind='bar', ax=axes, color='darkorchid', edgecolor='black')
plt.suptitle("Perfil dos Investidores do Banco X", size=16)
plt.title("Banco X", size=12)
axes.set_xlabel("Perfil do Investidor")
plt.xticks(rotation=0)
axes.set_ylabel("Quantidade")
fig.text(.7, .02, "Período: 2021", size=12) # Alternativa para caption
plt.setp(axes.patches, linewidth=1)
fig.set_facecolor("lightgrey")
axes.set_facecolor("lightgrey")
for p in axes.patches:
    axes.annotate(p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()/2-1), ha='center', va='center',
                  xytext=(0, 10), textcoords='offset points')
plt.show()

"""Rotacionando o gráfico:"""

fig, axes = plt.subplots(1, 1, figsize=(9,6))
perfil_investidor['perfil'].value_counts()[["Agressivo", "Moderado", "Conservador"]].plot(
    kind='barh', ax=axes, color='darkorchid', edgecolor='black')
plt.suptitle("Perfil dos Investidores do Banco X", size=16)
plt.title("Banco X", size=12)
axes.set_xlabel("Perfil do Investidor")
plt.xticks(rotation=0)
axes.set_ylabel("Quantidade")
fig.text(.7, .02, "Período: 2021", size=12) # Alternativa para caption
plt.setp(axes.patches, linewidth=1)
fig.set_facecolor("lightgrey")
axes.set_facecolor("lightgrey")
for p in axes.patches:
    axes.annotate(p.get_width(), (p.get_width()+1.3, p.get_y()+0.15), ha='center', va='center',
                  xytext=(0, 10), textcoords='offset points')
plt.show()

"""## Histograma

Vamos utilizar alguns dados sobre os municípios de São Paulo para essa nova demanda:
"""

result = pyreadr.read_r('dados_sp.RData')

print(result.keys())
dados_sp = result["dados_sp"]
dados_sp.head(3)

"""Aplicando sintaxes básicas do Matplotlib e Seaborn:"""

fig, axes = plt.subplots(1, 1)
dados_sp.hist(column='idh', ax=axes)
plt.show()

# Ou:
sns.histplot(data=dados_sp, x="idh")

"""Colorindo o gráfico:"""

fig, axes = plt.subplots(1, 1)
dados_sp.hist(column='idh', ax=axes, color='darkorchid')
plt.show()

"""Alterando o plano de fundo:"""

fig, axes = plt.subplots(1, 1)
dados_sp.hist(column='idh', ax=axes, color='darkorchid')
fig.set_facecolor("lightgrey")
axes.set_facecolor("lightgrey")
plt.show()

"""Adicionando contornos, título e nome dos eixos e removendo as linhas de grid:"""

fig, axes = plt.subplots(1, 1)
dados_sp.hist(column='idh', ax=axes, color='darkorchid', edgecolor='black')
axes.get_figure().gca().set_title("") # Importante para remover o título automático!!
fig.set_facecolor("lightgrey")
axes.set_facecolor("lightgrey")
plt.suptitle("IDH", size=20)
axes.set_xlabel("IDH dos Municípios de SP")
axes.set_ylabel("Frequência")
axes.grid(False)
plt.setp(axes.patches, linewidth=1)
plt.show()

"""Alterando a quantidade de caixas do histograma:"""

fig, axes = plt.subplots(1, 1, figsize=(9,6))
dados_sp.hist(column='pib', ax=axes, color='darkorchid', edgecolor='black', bins=100)
axes.get_figure().gca().set_title("") # Importante para remover o título automático!!
fig.set_facecolor("lightgrey")
axes.set_facecolor("lightgrey")
plt.suptitle("PIB", size=20)
axes.set_xlabel("PIB dos Municípios de SP")
axes.set_ylabel("Frequência")
axes.grid(False)
plt.setp(axes.patches, linewidth=1)
plt.show()

"""## Gráfico de Pontos

Para esse desafio, utilizaremos dados sobre os bairros da capital de São Paulo:
"""

atlas_ambiental = pd.read_csv("atlas_ambiental.csv", encoding='latin')
atlas_ambiental.head(3)

"""Aplicando a sintaxe básica de Matplotlib e Seaborn:"""

fig, axes = plt.subplots(1, 1)
atlas_ambiental.plot(kind='scatter', x='renda', y='escolaridade', ax=axes)
plt.show()

# Ou:
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade")

"""Estratificando informações com o argumento size:"""

fig, axes = plt.subplots(1, 1)
atlas_ambiental.plot(kind='scatter', x='renda', y='escolaridade',
                     s=(atlas_ambiental.idade**2)/5, ax=axes)
plt.show()

# Ou:
fig, axes = plt.subplots(1, 1)
p = sns.scatterplot(data=atlas_ambiental, x='renda', y='escolaridade', size='idade',
                    palette='GnBu', sizes=(20, 200), ax=axes)
sns.move_legend(p, bbox_to_anchor=(1, 1.02), loc='upper left')
plt.show()

"""Estratificando informações com o argumento color:"""

fig, axes = plt.subplots(1, 1, figsize=(12,6))
scatter = axes.scatter(x=atlas_ambiental.renda, y=atlas_ambiental.escolaridade,
                     s=(atlas_ambiental.idade**2)/4, c=atlas_ambiental.favel>6, cmap='viridis')

# produce a legend with the unique colors from the scatter
legend1 = axes.legend(*scatter.legend_elements(),
                    loc="upper right", title="Favelização", bbox_to_anchor=(1.11, 1))
axes.add_artist(legend1)

# produce a legend with a cross section of sizes from the scatter
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
labels = [int(''.join(char for char in string if char.isdigit())) for string in labels]
labels = [int((label*4)**0.5) for label in labels]
legend2 = axes.legend(handles, labels, loc="upper right", title="Idade", bbox_to_anchor=(1.1, 0.7))

axes.set_xlabel("Renda")
axes.set_ylabel("Escolaridade")
plt.show()

# Ou:
fig, axes = plt.subplots(1, 1)
p = sns.scatterplot(data=atlas_ambiental, x='renda', y='escolaridade', size='idade',
                    hue=atlas_ambiental.favel>6, palette='GnBu', sizes=(20, 200), ax=axes)
sns.move_legend(p, bbox_to_anchor=(1, 1.02), loc='upper left')
plt.show()

"""Estratificando informações com o argumento marker:"""

fig, axes = plt.subplots(1, 1, figsize=(8,8))
p = sns.scatterplot(data=atlas_ambiental, x='renda', y='escolaridade', size='idade',
                    hue=atlas_ambiental.favel>6, style=atlas_ambiental.mortalidade>18,
                    palette='GnBu', sizes=(20, 300), ax=axes)
plt.title("Indicadores dos Distritos do Município de São Paulo", size=20)
axes.set_xlabel("Renda", size=14)
axes.set_ylabel("Escolaridade", size=14)

handles, labels  =  axes.get_legend_handles_labels()
axes.legend(handles, ['Favelização>6', 'False', 'True', 'Idade', '21', '24', '27', '30', '33', '36', 'Mortalidade>18', 'False', 'True'],
            loc='lower right')

sns.move_legend(p, bbox_to_anchor=(1, 0.8), loc='upper left')

plt.show()

"""Traçando uma linha de tendências:"""

fig, axes = plt.subplots(1, 1, figsize=(8,8))
p = sns.scatterplot(data=atlas_ambiental, x='renda', y='escolaridade', size='idade',
                    hue=atlas_ambiental.favel>6, style=atlas_ambiental.mortalidade>18,
                    palette='GnBu', sizes=(20, 300), ax=axes)
sns.regplot(data=atlas_ambiental, x="renda", y="escolaridade", scatter=False, ax=axes)

plt.title("Indicadores dos Distritos do Município de São Paulo", size=20)
axes.set_xlabel("Renda", size=14)
axes.set_ylabel("Escolaridade", size=14)

handles, labels  =  axes.get_legend_handles_labels()
axes.legend(handles, ['Favelização>6', 'False', 'True', 'Idade', '21', '24', '27', '30', '33', '36', 'Mortalidade>18', 'False', 'True'],
            loc='lower right')

sns.move_legend(p, bbox_to_anchor=(1, 0.8), loc='upper left')

plt.show()

# Ou:
fig, axes = plt.subplots(1, 1, figsize=(8,8))
p = sns.scatterplot(data=atlas_ambiental, x='renda', y='escolaridade', size='idade',
                    hue=atlas_ambiental.favel>6, style=atlas_ambiental.mortalidade>18,
                    palette='GnBu', sizes=(20, 300), ax=axes)
sns.regplot(data=atlas_ambiental, x="renda", y="escolaridade", scatter=False, lowess=True, ax=axes)

plt.title("Indicadores dos Distritos do Município de São Paulo", size=20)
axes.set_xlabel("Renda", size=14)
axes.set_ylabel("Escolaridade", size=14)

handles, labels  =  axes.get_legend_handles_labels()
axes.legend(handles, ['Favelização>6', 'False', 'True', 'Idade', '21', '24', '27', '30', '33', '36', 'Mortalidade>18', 'False', 'True'],
            loc='lower right')

sns.move_legend(p, bbox_to_anchor=(1, 0.8), loc='upper left')

plt.show()

"""Aproveitando o assunto “tendências”, vamos seguir explorando as capacidades do Python com uma nova base de dados sobre a corrupção no mundo (Fisman & Miguel, 2007):"""

result = pyreadr.read_r('fisman_miguel.RData')

print(result.keys())
fisman_miguel = result["fisman_miguel"]
fisman_miguel.head(3)

"""Notem que seria interessante plotar, por exemplo, o número de violações de trânsito em função do índice de corrupção do país. Vamos tentar?"""

fig, axes = plt.subplots(1, 1, figsize=(8,8))
p = sns.scatterplot(data=fisman_miguel, x='corruption', y='violations', ax=axes)
sns.regplot(data=fisman_miguel, x="corruption", y="violations", scatter=False, lowess=True, ax=axes)

axes.set_xlabel("Corruption", size=14)
axes.set_ylabel("Violations", size=14)

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x']+.02, point['y'], str(point['val']))

label_point(fisman_miguel.corruption, fisman_miguel.violations, fisman_miguel.code, plt.gca()) 

plt.show()

"""Note que há dois problemas principais:

1) Há muitos países sem violações reportadas, ou com um baixo número de violações, e países com um número alto de violações reportadas, o que deixaria o gráfico com problemas de escala;

2) Haveria uma dupla contagem, porque os países foram verificados antes e depois da imposição da nova lei de NY.

Vamos tentar mitigar o primeiro problema, padronizando os valores da variável violations:
"""

fig, axes = plt.subplots(1, 1, figsize=(8,8))

fisman_miguel['log_violations'] = np.log(fisman_miguel['violations'] + 1)
p = sns.scatterplot(data=fisman_miguel, x='corruption', y='log_violations', ax=axes)
sns.regplot(data=fisman_miguel, x="corruption", y='log_violations', scatter=False, lowess=True, ax=axes)

axes.set_xlabel("Corruption", size=14)
axes.set_ylabel("Violations", size=14)

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        ax.text(point['x']+.02, point['y'], str(point['val']))

label_point(fisman_miguel.corruption, fisman_miguel.log_violations, fisman_miguel.code, plt.gca()) 

plt.show()

"""Agora, podemos tentar mitigar o segundo problema utilizando o gráfico **relplot** do seaborn:"""

# fig, axes = plt.subplots(1, 1, figsize=(8,8))

fisman_miguel['log_violations'] = np.log(fisman_miguel['violations'] + 1)
p = sns.relplot(data=fisman_miguel, x='corruption', y='log_violations', col='post')

p.data = fisman_miguel
p.map(sns.regplot, 'corruption', 'log_violations', color='r', ci=None, scatter=False, lowess=True)

for i in [0, 1]:
  for idx, row in fisman_miguel.iterrows():
      x = row.corruption
      y = row.log_violations
      text = row.code
      if (row.post=='no' and i==0) or (row.post=='yes' and i==1):
          p.axes[0, i].text(x+.05, y, text, horizontalalignment='left')

plt.show()

"""Note um terceiro problema não identificado anteriormente: a sobreposição de labels. Podemos tentar resolver a situação em R com a função geom_text_repel(), do pacote ggrepel. Porém, no Python, não há uma solução bem estabelecida para resolver o problema. Pode-se tentar utilizar o pacote [adjustText](https://github.com/Phlya/adjustText), mas não vou aplicá-lo aqui.

## Gráfico de Linhas

Para os nossos gráficos de linhas, vamos utilizar dados da atual pandemia no Brasil, Índia, Rússia e Estados Unidos da América:
"""

result = pyreadr.read_r('covid_110521.RData')

print(result.keys())
covid_110521 = result["covid_110521"]
covid_110521.head(3)

"""Aplicando a sintaxe básica do Matplotlib/Seaborn:"""

fig, axes = plt.subplots(1, 1)
for idx, gp in covid_110521.groupby('country'):
    gp.plot(x='t', y='cumulative_cases', ax=axes, label=idx)
axes.set_ylabel("cumulative_cases")
plt.show()

# Ou:
sns.lineplot(data=covid_110521, x="t", y="cumulative_cases", hue="country")

"""Adicionando informações e deixando o gráfico mais elegante:"""

fig, axes = plt.subplots(1, 1)
sns.lineplot(data=covid_110521, x="t", y="cumulative_cases", hue="country", ax=axes)
axes.set_xlabel("Tempo em dias desde o primeiro caso oficial do Sars-Cov-2 reportado")
axes.set_ylabel("Casos cumulativos")
plt.legend(title='País')
plt.show()

"""O gráfico anterior poderia ser mais informativo, visto que, por exemplo, compara países com tamanhos populacionais distintos. Portanto, a magnitude das infecções também é distinta. Uma possibilidade de suavização da situação poderia ser a padronização da variável ‘cumulative_cases’. No gráfico a seguir, padronizamos os casos cumulativos de cada país numa escala log10:"""

covid_110521["log_ccases"] = np.log10(covid_110521["cumulative_cases"])

"""O gráfico resultante é o seguinte:"""

fig, axes = plt.subplots(1, 1, figsize=(10,6))
sns.lineplot(data=covid_110521, x="t", y="log_ccases", hue="country", ax=axes)
axes.set_xlabel("Tempo em dias desde o primeiro caso oficial do Sars-Cov-2 reportado")
axes.set_ylabel("Log10 Casos cumulativos")
plt.legend(title='País')
plt.show()

"""Por mais que dê para se extrair alguns insights interessantes do gráfico anterior, alguém poderia dizer que seria melhor, por exemplo, utilizar uma proporção da população infectada em razão do tempo passado:"""

covid_110521["pop_ccases"] = covid_110521['cumulative_cases'] / covid_110521['pop']

"""A seguir, o resultado visual:"""

fig, axes = plt.subplots(1, 1, figsize=(10,6))
sns.lineplot(data=covid_110521, x="t", y="pop_ccases", hue="country", ax=axes)
axes.set_xlabel("Tempo em dias desde o primeiro caso oficial do Sars-Cov-2 reportado")
axes.set_ylabel("% Pop. Infectada")
plt.legend(title='País')
plt.show()

"""Ainda assim, os gráficos não trazem uma informação importante: os valores dos casos cumulativos por dia e por país. Em regra, podemos utilizar o padrão axes.text() para isso:"""

fig, axes = plt.subplots(1, 1, figsize=(10,6))
p = sns.lineplot(data=covid_110521, x="t", y="cumulative_cases", hue="country", ax=axes)

for idx, row in covid_110521.iterrows():
      x = row.t
      y = row.cumulative_cases
      text = row.cumulative_cases
      axes.text(x+.05, y, text, horizontalalignment='left')

axes.set_xlabel("Tempo em dias desde o primeiro caso oficial do Sars-Cov-2 reportado")
axes.set_ylabel("Casos Cumulativos")
plt.legend(title='País')
plt.show()

"""Está caótico, certo? E se alterássemos o ângulo de exibição das labels?"""

fig, axes = plt.subplots(1, 1, figsize=(10,6))
p = sns.lineplot(data=covid_110521, x="t", y="cumulative_cases", hue="country", ax=axes)

for idx, row in covid_110521.iterrows():
      x = row.t
      y = row.cumulative_cases
      text = row.cumulative_cases
      axes.text(x+.05, y, text, horizontalalignment='left', rotation=45)

axes.set_xlabel("Tempo em dias desde o primeiro caso oficial do Sars-Cov-2 reportado")
axes.set_ylabel("Casos Cumulativos")
plt.legend(title='País')
plt.show()

"""Podemos tentar utilizar outro espaçamento para esses labels:"""

fig, axes = plt.subplots(1, 1, figsize=(10,6))
p = sns.lineplot(data=covid_110521, x="t", y="cumulative_cases", hue="country", ax=axes)

for idx, row in covid_110521.iterrows():
      x = row.t
      y = row.cumulative_cases
      text = row.cumulative_cases
      if x%20==0:
          axes.text(x+.05, y, text, horizontalalignment='left')

axes.set_xlabel("Tempo em dias desde o primeiro caso oficial do Sars-Cov-2 reportado")
axes.set_ylabel("Casos Cumulativos")
plt.legend(title='País')
plt.show()

"""Em casos extremos, como no exemplo apresentado, talvez seja melhor omitir as labels e deixar o gráfico interativo com o usuário da informação. Podemos fazer isso com o pacote ‘plotly’:"""

fig = px.line(covid_110521, x="t", y="cumulative_cases", color="country", labels={"country": "País"})
fig.update_layout(xaxis_title='Tempo em dias desde o primeiro caso oficial do Sars-Cov-2 reportado',
                  yaxis_title='Casos Cumulativos')
fig.show()

"""Agora basta passar o mouse pelo gráfico para ter acesso às informações necessárias!

Caso quiséssemos fazer uma análise diária, bastaria mudar a variável de interesse:
"""

fig = px.line(covid_110521, x="t", y="daily_cases", color="country", labels={"country": "País"})
fig.update_layout(xaxis_title='Tempo em dias desde o primeiro caso oficial do Sars-Cov-2 reportado',
                  yaxis_title='Casos Diários')
fig.show()

"""## Mapas de Calor

Nosso principal exemplo para gráficos de calor será a respeito da relação entre variáveis. Entre variáveis métricas, essas relações se chamam correlações, cuja fórmula do coeficiente de correlação de Pearson segue a seguir:

$\rho = \frac{\sum_{i=1}^{n}(X_{i}-\bar{X}).(Y_{i}-\bar{Y})}{\sqrt{\sum_{i=1}^{n}(X_{i}-\bar{X})^2}.\sqrt{\sum_{i=1}^{n}(Y_{i}-\bar{Y})^2}}$

Assim, primeiro, vamos observar alguns gráficos correlacionais utilizando algumas possibilidades em Python:
"""

atlas_ambiental.columns

"""Vamos remover, primeiro, a primeira coluna do dataset, gerada involuntariamente na conversão do arquivo .RData (utilizado no script em R) para .csv:"""

del atlas_ambiental['Unnamed: 0']
atlas_ambiental.columns

sns.pairplot(atlas_ambiental, height=3)

"""Para criarmos um gráfico de calor a respeito das correlações da nossa base de dados, o primeiro passo é estabelecer uma Matriz de Correlações. Podemos fazer isso utilizando a função corr() do pacote pandas:"""

corr = atlas_ambiental.corr() # Calcula matriz de correlação

corr.style.background_gradient(cmap='coolwarm') # Plot da matriz de correlação

plt.matshow(corr)

fig, axes = plt.subplots(1, 1, figsize=(12,9))
sns.heatmap(corr, cmap="Blues", annot=True)
fig.show()

"""Podemos também aplicar o plotly aqui:"""

fig = px.imshow(corr, text_auto=True, aspect='auto', color_continuous_scale='Blues')
fig.show()

"""## Boxplot

No Python, para construir alguns boxplots, não precisamos utilizar as bases de dados no formato long como no R:

"""

fig, axes = plt.subplots(1, 1)
atlas_ambiental.iloc[:,1:].boxplot(ax=axes)
plt.show()

# Ou:
fig, axes = plt.subplots(1, 1)
sns.boxplot(data=atlas_ambiental.iloc[:,1:], palette="Blues", ax=axes)
fig.show()

"""A visualização ficou diferente do esperado, não é? Você consegue dizer a razão disso?

O problema está na comparação de variáveis com tipos distintos de magnitude.

Podemos resolver a situação padronizando as variáveis com o procedimento zscores, por exemplo:

$zX_{i}=\frac{X_{i}-\bar{X}}{\sigma}$
"""

atlas_padronizado = atlas_ambiental.iloc[:,1:]
atlas_padronizado.copy(deep=True) # Criando cópia completa e não só uma referência ao dataset original

for col in atlas_padronizado.columns:
    if atlas_padronizado[col].dtype != 'object':
        atlas_padronizado[col] = (atlas_padronizado[col] - atlas_padronizado[col].mean())/atlas_padronizado[col].std(ddof=0)
atlas_padronizado.head(3)

# Ou:
from sklearn.preprocessing import scale

atlas_padronizado2 = atlas_ambiental.iloc[:,2:]
atlas_padronizado2.copy(deep=True)

atlas_padronizado2 = pd.DataFrame(scale(atlas_padronizado2), index=atlas_padronizado2.index, columns=atlas_padronizado2.columns)
atlas_padronizado2.head(3)

"""Vamos tentar, mais uma vez, utilizar a sintaxe básica do seaborn para a construção de boxplots:"""

fig, axes = plt.subplots(1, 1, figsize=(8,6))
sns.boxplot(data=atlas_padronizado.iloc[:,1:], palette="Blues", ax=axes)
fig.show()

"""Podemos deixar o gráfico mais elegante nomeando os eixos:"""

fig, axes = plt.subplots(1, 1, figsize=(8,6))
sns.boxplot(data=atlas_padronizado.iloc[:,1:], palette="Blues", ax=axes)
axes.set_xlabel("Variáveis", size=14)
axes.set_ylabel("Valores padronizados", size=14)
fig.show()

"""Por fim, também podemos deixar os boxplots interativos utilizando o pacote plotly:"""

fig = px.box(atlas_padronizado2)
fig.update_layout(xaxis_title='Variáveis',
                  yaxis_title='Valores Padronizados')
fig.show()

