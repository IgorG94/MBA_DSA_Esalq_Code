
# Instalação e carregamento de pacotes ------------------------------------

install.packages("proton")
library(proton)

# ATENÇÃO: o presente script apresenta um jogo virtual que demandará do aluno 
# os conhecimentos apresentados nos Scripts 1 e 2 dessa aula. Poderão ser 
# demandados, ainda, conhecimentos a respeito das obras sugeridas nessa aula.

# O jogo colocará o estudante na posição de um hacker que tentará desvendar 
# alguns segredos para cumprir seus objetivos. Seja como for, aos alunos 
# desavisados, esse script não ensina, nem tem a intenção de ensinar alguma 
# técnica de hacking. A ideia é lúdica, com fins pedagógicos, apenas.


# Instruções do Desafio ---------------------------------------------------

# Seu objetivo é encontrar as credenciais de acesso de Slawomir Pietraszko ao
# servidor. Essa é a única maneira de encontrar os planos secretos de seu 
# laboratório.

# Para começar o desafio, comande proton()

# Lembre-se que a qualquer momento você poderá argumentar hint=TRUE aos comandos
# executados para receber dicas adicionais. Porém, é desejável que o aluno não
# tente recorrer a esse recurso.

# O Projeto Proton é de autoria de Przemyslaw Biecek. Ver ?proton para outros
# créditos e informações.


# Iniciando o jogo ---------------------------------------------------------
proton()

# Pietraszko utiliza uma senha difícil de adivinhar. Primeiramente, tentaremos 
# hackear a conta de um usuário que não é tão cuidadoso quanto o Pietraszko.

# Porém, quem é esse usuário mais descuidado? Investigações preliminares sugerem
# que John Insecure não se importa com a segurança de sua conta no servidor 
# Proton. Ele deve utilizar uma senha fácil de se quebrar. Começaremos atacando 
# a conta dele primeiro!


################################################################################  
#                 DESAFIO 1: Encontrar o login do John Insecure                #
################################################################################

# Nosso amigo chamado Bit conseguiu uma base de dados chamada de 'employees' que
# contém os nomes e os logins da página da internet da Universidade Tecnológica 
# de Warsaw. Sua tarefa, portanto, será a de encontrar o login de John Insecure.

# Quando, finalmente, você encontrar o login do John Insecure, utilize o comando
#`proton(action = "login", login="XYZ")`, substituindo o valor XYZ pelo login do
# John Insecure.

# Como já dito, ao precisar de mais dicas, basta utilizar o argumento hint=T:
proton(hint = TRUE)

# DICA: Na base de dados `employees`, tente encontrar uma linha que contenha o 
# valor `Insecure` na coluna `surname`.

# Para carregar a base de dados `employees`
data("employees")

# Para observar o nome das variáveis da base de dados `employees`
names(employees)

# Selecionando, na base de dados `employees`, os funcionários cujo primeiro
# nome seja John e cujo sobrenome seja Insecure
employees[which(employees$name == "John" & employees$surname == "Insecure"), ]

# Ou de maneira absolutamente precisa:
employees[which(employees$name == "John" & employees$surname == "Insecure"), ]$login

# Então, para cumprir o Desafio 1, basta comandar:
proton(action = "login", login = "johnins")

#Parabéns! Você descobriu qual é o login do John Insecure!

# É muito provável que ele utilize uma senha comum.

# Nosso amigo Bit encontrou e baixou na internet uma base de dados com as 1000 
# senhas mais utilizadas no mundo. Você poderá encontrar essas informações no 
# vetor `top1000passwords`.


################################################################################  
#                 DESAFIO 2: Descobrir a senha do John Insecure                #
################################################################################

# Depois de descobrir a senha do John Insecure, utilize o comando 
# `proton(action = "login", login="XYZ", password="ABC")` para logar no servidor
# Proton com as credenciais capturadas. Se a senha estiver correta, você 
# receberá a seguinte mensagem: `Success! User is logged in!` (Sucesso! O 
# usuário está logado!). Se a senha estiver errada, você receberá a seguinte 
# mensagem: `Password or login is incorrect!` (Senha ou login incorretos).

# Carregando os dados presentes em 'top1000passwords'
data("top1000passwords")

# Como já dito, ao precisar de mais dicas, basta utilizar o argumento hint=T:
proton(action = "login", login = "johnins", hint = TRUE)

# DICA: Utilize o método da força bruta. Ao utilizar funções de loop, tente 
# logar com as senhas existentes no vetor 'top1000passwords'

# Sabendo-se que o comando para a digitação da senha é o 
# proton(action = "login", login="XYZ", password="ABC"), então:
for(i in 1:length(top1000passwords)){
  proton(action = "login", login = "johnins", password = top1000passwords[i])
}

# Se o aluno quiser saber, de fato, qual a senha do John Insecure, a rotina
# abaixo pode ser uma solução:
for(i in 1:length(top1000passwords)){
  resultado <- proton(action = "login", 
                  login = "johnins", 
                  password = top1000passwords[i])
  
  if(resultado == "Success! User is logged in!"){
    print(top1000passwords[i])
    break()
  }
}


# Muito bem! Você descobriu qual é a senha do John Insecure!
  
# O nosso amigo Bit utilizou as credenciais do John Insecure para acessar o 
# servidor Proton. Acontece que o John Insecure parece ter acesso aos logs do 
# servidor.

# Agora, o Bit quer verificar de qual máquina o Pietraszko loga no servidor 
# Proton mais frequentemente. A ideia do Bit é encontrar algum dado útil.

# Os logs de acesso estão na base de dados `logs`. As colunas desse dataset 
# contêm informações sobre quem, quando e qual computador foi logado ao servidor
# Proton.


################################################################################  
#   DESAFIO 3: Verificar de qual computador o Pietraszko costuma logar mais    # 
#   frequentemente ao servidor Proton                                          #
################################################################################

# Utilize o comando `proton(action = "server", host="XYZ")` para aprender mais 
# sobre o que pode ser encontrado no servidor XYZ.

# A maior probabilidade de encontrar algo interessante está em descobrir qual 
# máquina o Pietraszko utiliza para logar mais frequentemente.

# Carregando a base de dados 'logs'
data("logs")

# Observando as colunas da base de dados 'logs'
names(logs)

# Dentre várias soluções possíveis, podemos voltar a utilizar os conhecimentos
# aplicados no desafio anterior

# Vamos observar ao comando sugerido pelo desafio, argumentando os resultados
# presentes na primeira linha do dataset logs:
logs[1, ]

proton(action = "server", host = "193.0.96.13.15")

# A resposta foi:

# Bit has spent some time on infiltration of this workstation, but there is 
# nothing interesting. 
# Find the workstation that Pietraszko is using most often and try again.

# A tradução aqui, não é tão importante. Em suma, é um aviso que o nosso amigo
# Bit gastou algum tempo explorando o IP dessa máquina e não encontrou nada de
# interessante. Por outro lado, capturar essa resposta do R parece ser
# importantíssimo!

# Vamos observar a resposta do R ao argumentar os resultados presentes na 
# segunda linha do dataset logs:
logs[2, ]

proton(action = "server", host = "193.0.96.13.9")

# A resposta foi a mesma, certo? Então, nosso objetivo será descobrir quando, 
# isto é, para qual valor do argumento host, o R retorna uma resposta diferente!

# Salvando a resposta comum do R:
resposta <- proton(action = "server", host = "193.0.96.13.9")
resposta

# Espera! O R não consegue capturar a resposta desse comando. O que fazer?

# Lembram que ainda temos acesso ao dataset ‘employees’? Vamos buscar pelo 
# login do Pietraszko. Isso faz sentido porque o dataset ‘logs’ é identificado 
# por logins. Assim, ao capturarmos o login do Pietraszko, poderemos cruzar 
# informações relevantes:
employees[which(employees$surname == "Pietraszko"), ]

# Agora vamos observar a base de dados logs filtrada em função do login do
# Pietraszko que foi encontrado:
logs[which(logs$login == "slap"), ]

# O R retornou muita coisa, certo? Porém, estamos interessados em descorbir a
# máquina mais utilizada por Pietraszko para logar no servidor Proton.

# Primeiramente, vamos salvar as respostas do R para o comando anterior em um
# objeto:

resposta_R <- logs[which(logs$login == "slap"), ]
resposta_R

names(resposta_R)

# A seguir, vamos salvar a coluna host, do objeto 'resposta_R' em um novo
# objeto, após a aplicação da função unique():
hosts <- as.character(unique(resposta_R$host))
hosts

# Sobraram 5 computadores:

# "194.29.178.16"  "194.29.178.108" "193.0.96.13.20" "193.0.96.13.38"
# "194.29.178.155"

# O número de linhas corresponderá ao número de acessos de Pietraszko ao 
# servidor Proton. Buscamos o computador com o maior número de acessos. Logo:
nrow(resposta_R[which(resposta_R$host == "194.29.178.16"), ])  #122 acessos
nrow(resposta_R[which(resposta_R$host == "194.29.178.108"), ])  #74 acessos
nrow(resposta_R[which(resposta_R$host == "193.0.96.13.20"), ])  #33 acessos
nrow(resposta_R[which(resposta_R$host == "193.0.96.13.38"), ])   #1 acesso
nrow(resposta_R[which(resposta_R$host == "194.29.178.155"), ])   #6 acessos

# OU: *************************
tail(names(sort(table(resposta_R$host))),1)
# JÁ DEVOLVE O HOST CERTO!!!

# Então:
proton(action = "server", host = "194.29.178.16")


# De fato, Pietraszko, costumeiramente, utiliza o computador público 
# 194.29.178.16. Que descuido!
  
# O Bit conseguiu se infiltrar no computador 194.29.178.16 facilmente. Ele 
# baixou um arquivo que contém todo o histórico de comandos dados ao console do
# computador. O arquivo é o ‘bash_history’.

# A expectativa é a de que, há a um tempo atrás, Pietraszko tenha digitado, por 
# engano, a senha no console do computador enquanto tentava logar no servidor 
# Proton.


################################################################################  
#                     DESAFIO 4: Descobrir a senha do Pietraszko               #
################################################################################

# Na base de dados ‘bash_history’ você encontrará todos os comandos e parâmetros
# que foram comandados por Pietraszko.

# Tente extrair desse dataset apenas os comandos e verique se eles se parecem 
# com senhas. Lembre-se que senhas não costumam conter espaços!

# Carregando os dados de ‘bash_history’
data("bash_history")

# Vamos verificar se faz sentido filtrar os comandos dados por Pietraszko.
length(unique(bash_history))
length(bash_history)

# Parece que faz sentido filtrar os comandos dados Pietraszko.
comandos_unicos <- unique(bash_history)

# Agora vamos filtrar os comandos que não possuem espaços, atribuindo o valor
# lógico NA para aqueles comandos que possuam espaços
comandos_sem_espaços <- gsub(pattern = " ",
                             replacement =  NA,
                             x = comandos_unicos)

# Finalmente, vamos solicitar que o R retorne os resultados presentes no objeto
# 'comandos_sem_espaços' que NÃO contenham os valores lógicos NA
comandos_sem_espaços[which(comandos_sem_espaços != NA)]
comandos_sem_espaços[which(is.na(comandos_sem_espaços) != T)]

# Sobraram 5 resultados, certo? Poderíamos tentar utilizar um a um, mas o
# resultado "DHbb7QXppuHnaXGN" é o que mais parece com uma senha. Logo:

proton(action = "login", login = "slap", password = "DHbb7QXppuHnaXGN")

# Parabéns!

# Você quebrou a senha do Pietraszko!

# Fim ---------------------------------------------------------------------