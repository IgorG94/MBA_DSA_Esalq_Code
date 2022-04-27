
# Funções if, else e ifelse -----------------------------------------------

#if() e else - exemplos:

vetor <- 2

if(vetor > 1){
  print("oi!")
}

#Porém:
if(vetor > 5){
  print("oi!")
}

#O R não respondeu nada. Por quê?

#Corrigindo:
if(vetor > 5){
  print("oi!")
} else {
  print("voltei!")
}

#Entendendo como o R 'pensa':

vetor <- 7

if(vetor > 8){
  print("O objeto é maior do que 8")
}else if(vetor > 7){
  print("O objeto é maior do que 7")
}else if(vetor > 6){
  print("O objeto é maior do que 6")
}else if(vetor > 5){
  print("O objeto é maior do que 5")
} else {
  print("O objeto é maior do que 4")
}

if(vetor > 4){
  print("O objeto é maior do que 4")
}else if(vetor > 5){
  print("O objeto é maior do que 5")
}else if(vetor > 6){
  print("O objeto é maior do que 6")
}else if(vetor > 7){
  print("O objeto é maior do que 7")
} else {
  print("O objeto é menor do que 4")
}

#ifelse() - exemplo:

ifelse(vetor == 7, 
       yes = "o objeto é igual a 7", 
       no = "o objeto é diferente de 7")


# Funções iterativas ------------------------------------------------------

#A função for():

y <- 10

for(i in 1:5){
  print(y + i)
}

#De onde veio o i? Você consegue entender o que ocorreu?

#Não há a necessidade de se trabalhar apenas com números! Exemplo:

vetor_regioes <- c("norte", "nordeste", "sudeste", "sul", "centro-oeste")

for(regiao in vetor_regioes){
  print(regiao)
}

#A função while():

z <- 0

while(z < 10){
  print(z)
  z <- z + 1
}

#A função repeat

w <- 3

repeat{
  print(w)
  w <- w + 2
  if(w > 18) break()
}
