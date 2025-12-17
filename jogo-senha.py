# Usar o import para importar o random
# Fazer uma lista
# Fazer uma estrutura de repetição que repita o randint até quando estiver 4 numeros na lista
# Fazer um if que se o numero não estiver na lista do computador adicionar com o append
# Criar uma lista para os palpites do usuario
# Fazer outra estrutura de repetição para que repita a pergunta do palpite até estiver 4 numeros na lista do usuario
# Verificar se tem algum numero repetido e se estiver pedir para ponhar outro no lugar
# fazer um if para que se todos os numeros estejam certos então acertou tudo
# criar um else e dentro dele ponhar um for e dentro do for ponhar um if que vai verificar se o numero esta no lugar certo
# criar um elif para ver se o numero esta no lugar errado
# e criar outro elif para ver se o numero não está na lista
# Não esquecer de ponhar um while pra ficar repetindo o jogo


import random 
ganhou = False
computador = []
tentativa = 0
while len(computador) < 4:
    numero = random.randint(0, 9)
    if numero not in computador:
        computador.append(numero)

while not ganhou and tentativa < 5:
    lista = []

    while len(lista) < 4:
        palpite = int(input(("Digite um número que não seja repetido: ")))
       
        if palpite not in lista:
                lista.append(palpite)
        else:
                print("Número repetido tente outro!")
    tentativa += 1
    if lista == computador:
        ganhou = True
        print("Acertou tudo")
    else:
        for c in range(0, 4):
            if lista[c] == computador [c]:
                print("o número {} esta no lugar correto".format(lista[c]))
                        
            elif lista[c] in computador:
                print("o numero {} está no lugar errado".format(lista[c]))
            elif lista[c] not in computador:
                print("o número {} não existe".format(lista[c]))
if not ganhou:
     print("Você perdeu")


                

