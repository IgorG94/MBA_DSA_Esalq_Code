# -*- coding: utf-8 -*-
"""
# Funções if, else e elif

**O elif é a função que substitui o ifelse do R!**

Exemplos:
"""

vetor = 2

if vetor > 1:
  print("oi!")

"""Porém:"""

if vetor > 5:
  print("oi!")

"""O Python não responde nada, porque não cumpre com a condição delimitada!

Para corrigir, utilizamos o else:
"""

if vetor > 5:
  print("oi!")
else:
  print("voltei!")

"""Entendendo como elif funciona:"""

vetor = 7

if vetor > 8:
  print("O objeto é maior do que 8")
elif vetor > 7:
  print("O objeto é maior do que 7")
elif vetor > 6:
  print("O objeto é maior do que 6")
elif vetor > 5:
  print("O objeto é maior do que 5")
else:
  print("O objeto é maior do que 4")

"""Não há função equivalente ao ifelse do R no Python!

# Funções iterativas - a função for()
"""

y = 10

for i in range(1, 6):
  print(y + i)

"""De onde veio o i? Você consegue entender o que ocorreu?

Não há a necessidade de se trabalhar apenas com números! Exemplo:
"""

vetor_regioes = ["norte", "nordeste", "sudeste", "sul", "centro-oeste"]

for regiao in vetor_regioes:
  print(regiao)

"""# A função while()"""

z = 0

while z < 10:
  print(z)
  z += 1

w = 3

while True:
  print(w)
  w = w + 2
  if w > 18:
    break
