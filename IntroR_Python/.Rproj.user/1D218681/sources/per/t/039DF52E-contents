
# Introdução à linguagem R ------------------------------------------------

# Tenha em mente que: 1) no R, tudo é um objeto; 2) o R é uma maneira de se
# "comunicar" com uma máquina e, por assim ser, seja explícito(a), direto(a) e 
# literal; e 3) o R, em sua forma pura, entende a linguagem R e só.


# Assim, não adianta tentar comandar nada em linguagem humana, independente-
# mente do idioma. Portanto, as espécies de declarações a seguir não funcio-
# narão:


Olá, R #português
Hi R #inglês
Ni hao #chinês

# O R não sabe/entende o que você quis dizer com os comandos anteriores.
# Não sabe, porque, lembre-se, no R tudo é um objeto! Dessa forma, podemos
# dizer que o R não veio sabendo/entendendo o que deve ser "Olá, R", "Hi R" 
# ou "Ni hao". Também podemos dizer que ninguém ensinou ao R, ainda, o que
# essas expressões em idioma humano devem significar.

# O R entende o significado, ou melhor, o valor de algo, quando esse algo
# está contido por um objeto. Exemplo:

meu_primeiro_objeto <- 15

# A partir de agora "meu_primeiro_objeto", para o R, é um objeto com valor 
# igual a 15. Podemos verificar isso declarando o objeto: 

meu_primeiro_objeto

# Podemos, inclusive, efetuar algumas operações com o nosso primeiro objeto:

15 + 2 #é o mesmo que:

meu_primeiro_objeto + 2


# Aqui é oportuno falar sobre alguns operadores da linguagem R:

2 + 2   #soma
3 - 1   #subtração
4 * 5   #multiplicação
12 / 3  #divisão
7 ^ 2   #exponenciação
0:100   #sequências

3 == 3  #comparação de igualdade
5 != 0  #comparação de diferenças
2 > 9   #maior do que
1 < 8   #menor do que
5 >= 5  #maior ou igual
4 <= 1  #menor ou igual

# Podemos utilizar esses operadores, tranquilamente, com o nosso primeiro
# objeto.

# Com o R, há que se haver o cuidado sobre o desejo de se sobrescrever
# objetos.

meu_primeiro_objeto <- 160

# Em nível de código, o R nunca vai te perguntar sobre a certeza de se 
# querer fazer algo. Atenção a isso!

# Também podemos guardar valores textuais em objetos:

nome <- usp

# O R reportou um erro. Por quê?

nome_1 <- "usp"

nome_1

#ou

nome_2 <- 'usp'

nome_2

# Podemos utilizar alguns operadores aprendidos anteriormente:

nome_1 == nome_2

nome_1 != nome_2

# É possível guardar valores lógicos em objetos:

verdadeiro <- nome_1 == nome_2

verdadeiro


falso <- nome_1 != nome_2

falso


# Outros valores importantes:

TRUE #logical
T #logical
FALSE #logical
F #logical
NA #logical
NULL #NULL
Inf #numeric
-Inf #numeric

# Podemos guardar bases de dados inteiras em objetos, porém, antes, devemos
# pensar sobre como guardar mais de uma informação em um objeto.

vetor <- 1 2 3 4 5 6 7 8 9 10

vetor <- 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

vetor <- (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# A resposta está na função concatenate: c()

vetor <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

vetor


# O exposto, de forma análoga, vale para valores textuais

nomes <- c("mariana", "pedro", "daniela")

nomes


# Funções -----------------------------------------------------------------

# Funções são tipos especiais de objetos no R, cujo nome vem seguido de 
# parêntesis. Equivalem a ordens diretas à máquina.

# Funções são algoritmos. Cada algoritmo possui suas próprias atribuições
# e carrega dentro de si seu processo decisório. Para a função c(), seu
# objetivo é o de concatenar valores.

# Vamos utilizar outro exemplo para esclarecer o assunto:

round(x = 3.141592)

# No comando anterior, não houve a criação de objeto algum. Houve a 
# declaração de uma função cujo objetivo é o arredondamento numérico, em 
# que "x" é um argumento da função.

# Argumentos são complementos às ordens dadas. Imagine o seguinte caso:

round()

# Por que houve um erro?

# Voltemos ao exemplo:

round(x = 3.141592)

# Por que o R apenas transforma o valor de 3.141592 no valor inteiro 3?

# Devemos complementar a ordem com um novo argumento:

round(x = 3.141592, digits = 3)

# Como saber quais os argumentos de uma dada função?

# Primeira maneira:
?round

#segunda maneira:
args(round)


# Coerção -----------------------------------------------------------------

# Voltando à criação de objetos, é possível ter surgido a dúvida do que 
# aconteceria se guardássemos valor numéricos e textuais num único objeto. 
# Vamos testar?

nomes_e_idades <- c("mariana", 22, "pedro", 30, "daniela", 45)

nomes_e_idades

# Todas as observações internas ao objeto criado viraram textos, certo?
# Isso se chama coerção. Podemos comprovar com a função class():

class(nomes_e_idades)
class(meu_primeiro_objeto)
class(verdadeiro)

# De novo:
class(nomes_e_idades)


# Há uma hierarquia básica de valores no R, e é a seguinte: valores 
# textuais > valores numéricos > valores lógicos. Vamos expandir o exemplo
# da seguinte forma:

teste <- c("laranja", 230, FALSE)

teste

class(teste)

# Como o esperado, houve a coerção dos valores salvos no objeto "teste"
# para valores textuais. Outro exemplo:

outro_teste <- c(12, 37, FALSE, TRUE, FALSE, TRUE, TRUE, TRUE, TRUE)

outro_teste

class(outro_teste)


# Os valores lógicos utilizados foram transformados em números, seguindo
# o padrão 0 para FALSE e 1 para TRUE. Diferentemente seria se utilizás-
# semos os valor lógico NA. O valor NA significa Not Available, e é como 
# o R explicita os missing values.

missings <- c(12, 37, FALSE, TRUE, FALSE, TRUE, TRUE, TRUE, TRUE, NA)

missings


# Variáveis categóricas ---------------------------------------------------

# O R identifica suas variáveis categóricas como pertencentes à classe
# factor. Vamos criar um objeto que contenha o seguinte exemplo de variá-
# vel categórica policotômica:

tipo_sanguineo <- c("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")

tipo_sanguineo

class(tipo_sanguineo)

# Para transformamos os valores internos ao objeto "tipo_sanguineo" em
# categorias, devemos utilizar a função factor():

tipo_sanguineo <- factor(tipo_sanguineo)

tipo_sanguineo

class(tipo_sanguineo)

# OBS:

tipo_sanguineo <- c("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-", "A+", "A+")

tipo_sanguineo <- factor(tipo_sanguineo)
# Ainda temos 8 níveis após a modificação!!

tipo_sanguineo

# Para a utilização dos valores declarados em técnicas direcionadas a 
# variáveis nominais, o procedimento acima basta e está completo.

# Para o caso de variáveis ordinais, o trabalho deve ser estendido. Vamos
# criar um objeto com novas categorias:

nivel_escolarizacao <- c("fundamental", "médio", "graduação")

nivel_escolarizacao

class(nivel_escolarizacao)

# Utilizando a função factor():

nivel_escolarizacao <- factor(nivel_escolarizacao)

class(nivel_escolarizacao)

nivel_escolarizacao

# Observem os levels. Não é essa a ordem comumente aceita. Como faremos
# para o R entender a ordem fundamental, médio, graduação?

# A resposta está na expansão da argumentação da função factor():

nivel_escolarizacao <- factor(nivel_escolarizacao,
                              levels = c("fundamental",
                                         "médio",
                                         "graduação"))

class(nivel_escolarizacao)

nivel_escolarizacao


# E se tivéssemos recebido uma base de dados cujos rótulos para as 
# categorias fossem números? Vamos assumir o exemplo de que em dada base
# o valor "0" equivale a "não"; o valor "1" equivale a sim; e o valor
# "99" equivale a "talvez".

respostas <- c(0, 1, 1, 1, 99, 0, 99, 0, 0, 0, 1, 99)

respostas

class(respostas)

# Transformando em categorias:

respostas <- factor(respostas)

respostas

class(respostas)

# Explicando para o R os novos rótulos, incluindo um sentido de ordem (não,
# talvez, sim):

respostas <- factor(respostas,
                    levels = c(0, 99, 1),
                    labels = c("não", "talvez", "sim"))

class(respostas)

respostas


# Juntando objetos para a criação de bases de dados -----------------------

empresas <- c("Empresa A", NA, "Empresa C", "Empresa D", "Empresa E")
funcionarios <- c(100, 5000, 230, 12000, 1700)
presenca_bolsa <- c(F,T,NA,T,T)
sede_brasil <- c(NA,0,1,0,0)
diretor_executivo <- c(NA,"daniel","carlos","carla","solange")

#Antes de juntarmos os vetores, devemos verificar se seus comprimentos são
#iguais:

length(empresas)
length(funcionarios)
length(presenca_bolsa)
length(sede_brasil)
length(diretor_executivo)

dados <- data.frame(empresas, funcionarios, presenca_bolsa, 
                    sede_brasil, diretor_executivo)


dados

View(dados)

#Os nomes dos vetores criados e posteriormente unidos pela função 
#data.frame() serão os nomes das variáveis da nova base de dados. Assim, 
#poderíamos propor outros nomes da seguinte maneira:

dados <- data.frame(companies = empresas, 
                    employees = funcionarios, 
                    stock_exchange = presenca_bolsa, 
                    brazil_hq = sede_brasil, 
                    ceo = diretor_executivo)

dados

View(dados)


# Salvando objetos carregados no R ----------------------------------------

# Para salvar objetos, independentemente de sua classe (e.g. gráficos, bases
# de dados, modelos de machine learning, arquivos pdf, arquivos do Microsoft
# Office, etc.), podemos utilizar a função save():

save(dados, file = "dados.RData")

# Caso quiséssemos carregar os objetos salvos num outro momento, deveríamos
# utilizar a função load(). Exemplo: load("dados.RData").

load("dados.RData")


# Carregando objetos de extensão *.RData ----------------------------------

load("spam.RData")


# Carregando arquivos de alguns softwares mais utilizados -----------------

# Para carregar um arquivo *.csv, podemos, por exemplo:

bicicletas <- read_delim(file = "bicicletas.csv",
                         delim = ";", 
                         escape_double = FALSE, 
                         trim_ws = TRUE)

# O R retornou um erro, certo? A mensagem foi: ‘could not find function 
# "read_delim"’. Em  suma, o R disse não conhecer a função read_delim(). 
# Noutras palavras, seria como se o R ainda não soubesse como carregar uma base 
# de dados de extensão *.csv.

# Uma forma de ampliar as capacidades do R é pela instalação de bibliotecas 
# (comumente chamadas de pacotes). Um pacote, em regra, contém um conjunto de 
# funções (algoritmos) destinadas para determinado fim.

# Para dar uma ordem de ação ao R, já aprendemos que devemos utilizar uma 
# função. Logo, para instalar uma biblioteca, utilizaremos uma função. Essa 
# função será a install.packages(). A função read_delim() que queremos utilizar 
# faz parte do pacote readr:

install.packages("readr")

# Após a instalação de um pacote, é necessário que ele seja carregado com a 
# função library(). Então:

library(readr)

# Agora sim, podemos revisitar o comando presente na linha 377:

bicicletas <- read_delim(file = "bicicletas.csv",
                         delim = ";", 
                         escape_double = FALSE, 
                         trim_ws = TRUE)

#Caso quiséssemos salvar o nosso data frame 'dados' em formato *.csv:
write.csv(dados, file = "dados.csv", row.names = FALSE)

#
#
#
#Para carregar um arquivo do tipo *.xlsx:
library(readxl)
stricto_2018 <- read_excel("stricto_2018.xlsx")

#Caso quiséssemos salvar o nosso data frame 'dados' em formato *.xlsx
library(writexl)

write_xlsx(dados, "dados.xlsx")

#
#
#
#Para carregar uma base de dados do SPSS:
library(haven)

bolsa_estudos <- read_sav("bolsa_estudos.sav")

#Caso quiséssemos salvar o nosso data frame 'dados' em formato *.sav
write_sav(dados, "dados.sav")

#
#
#
#Para carregar uma base de dados do Stata:
vestibular <- read_dta("vestibular.dta")

#Caso quiséssemos salvar o nosso data frame 'dados' em formato *.dta
write_dta(dados, "dados.dta")

write_sas(dados, "dados")

# Podemos, inclusive, carregar bases de dados disponibilizadas on-line:

# Importando os dados de 210 países sobre a COVID19
covid <- read.csv("https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/csv/data.csv", 
                  na.strings = "", 
                  fileEncoding = "UTF-8-BOM")



# Introdução à manipulação de dados ---------------------------------------

# Há algumas bases de dados interessantes já armazenadas no R compiladas em
# um pacote chamado 'datasets'

# Para ver a documentação ou buscar ajuda a respeito de algum pacote:

help(package = "datasets")

# Para carregarmos uma base de dados interna, utilizamos a função data():

data("mtcars")

# Para melhor entendermos o que há na base de dados chamada 'mtcars', pode-
# mos comandar o seguinte:

?mtcars

# Se você está aqui é porque se interessa por dados, e pode ser que as bases de
# dados que você utiliza sejam extensas! Assim, por enquanto, vamos dar
# preferência às funções head() e tail() no lugar da função View():

head(x = mtcars)
tail(x = mtcars)

head(mtcars, n = 1)
tail(mtcars, n = 10)

# Outra função interessante é a função str():

str(mtcars)

# Também podemos obter informações a respeito do número de linhas e de colu-
# nas da base de dados com as funções nrow(), ncol() e dim():

nrow(mtcars)
ncol(mtcars)
dim(mtcars)

# Podemos, ainda, ter acesso aos nomes das variáveis da base de dados com o
# auxílio da função names():

names(mtcars)

# Podemos deletar a base de dados do nosso ambiente de trabalho com a função
# rm():

rm(mtcars)

# Voltando a carregar a base de dados mtcars
data("mtcars")

#Podemos acessar uma variável da nossa base de dados com o operador $:
mtcars$mpg
mtcars$cyl
#Também podemos acessar uma variável com o uso do operador [ , ]:
mtcars[, 10]

#Há, ainda, a função attach() que facilita bastante!
attach(mtcars)
gear
detach(mtcars)

#Podemos acessar as observações com o uso semelhante do operador [ , ]:
mtcars[1, ]

#Assim, é possível acessar valores específicos ao combinarmos o aprendido:
mtcars[2, 1]
mtcars[4, 5]

#Podemos, ainda, combinar as posições com o nome das variáveis:
mtcars[1, "mpg"]

#Não podemos, porém, comandar o seguinte:
mtcars[, "mpg" : "disp"]

#E agora? A declaração abaixo funcionará?
mtcars[ ,c("mpg", "cyl", "disp")]

#Outra forma interessante de seleção de valores:
mtcars[, -c(3:11)]

#A função which() pode ser uma boa aliada na tarefa de seleção de valores. 
#Vamos supor que a intenção seja que o R filtre todos os carros cujo valor para 
#a variável mpg seja igual a 21:
mtcars[which(mtcars$mpg == 21.0), ]

#E se quiséssemos os carros cujo valor para a variável mpg seja diferente de 21:
mtcars[which(mtcars$mpg != 21.0), ]

#Nesse momento é oportuno apresentar dois novos operadores:
# & #significa "e"
# | #em regra, significa "ou".

#Carros cujo valor para a variável mpg seja igual a 21 E com a variável qsec 
#menor do que 17:
mtcars[which(mtcars$mpg == 21.0 & mtcars$qsec < 17), ]

#Carros cujo valor para a variável mpg seja igual a 21 OU com a variável qsec 
#menor do que 17:
mtcars[which(mtcars$mpg == 21.0 | mtcars$qsec < 17), ]

# Criando e excluindo variáveis em uma base de dados ----------------------

#O operador $ também é útil para criarmos variáveis:
mtcars$var_nova <- NA

head(mtcars)

#Ainda para criarmos variáveis, poderíamos declarar o seguinte:
mtcars["nova_var"] <- NA

head(mtcars)

#Para excluir uma coluna de nossa base de dados, utilizamos o valor lógico NULL:

mtcars$var_nova <- NULL

head(mtcars)

mtcars["nova_var"] <- NULL

head(mtcars)


# Editando valores das observações ----------------------------------------

#Há várias formas de editar os valores de uma base de dados. Poderíamos 
#utilizar o que aprendemos sobre o oprador [ , ] de forma direta:

mtcars[1, 1] <- 82

mtcars[1, ]

#Caso houvesse um padrão de repetição para uma determinada substituição, 
#poderíamos utilizar a função gsub():

mtcars$cyl <- gsub(x = mtcars$cyl,
                   pattern = 6,
                   replacement = 8)

head(mtcars)

#A função edit() - Suponhamos que se queira desfazer a última alteração, 
#isto é, mudar o valor 82.0 para 21.0 da célula [1,1] da base mtcars:

mtcars <- edit(mtcars) #Utilizar o mouse e o teclado

mtcars[1, ]

#A função unique() é uma alternativa interessante de filtrar observações únicas.
#Para facilitar, vamos utilizar o dataset mtcars:
data("mtcars")

#Vamos salvar as 3 primeiras observaçoes do dataset mtcars num objeto novo
exemplo <- mtcars[1:3, ]

#Agora vamos, propositalmente, repetir as observações da base de dados 'exemplo'
#por 6 vezes:

exemplo_final <- rbind(exemplo,
                       exemplo,
                       exemplo)

#Aplicando a função unique():
unique(exemplo_final)
