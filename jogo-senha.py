
import random 
ganhou = False
computador = []
tentativa = 0


while len(computador) < 4:
    numero = random.randint(0, 9)
    if numero not in computador:
        computador.append(numero)

while not ganhou and tentativa < 8:
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
        x = 0
        z = 0
        for c in range(0,4):
            if lista[c] == computador[c]:
                x += 1
                        
            elif lista[c] in computador:
                z += 1

        if x > 0 and z == 0:
             print(f"Tem {x} número(s) no lugar certo")
        elif x > 0 and z > 0:
             print(f"Tem {x} número(s) no lugar certo e {z} números no lugar errado")
        elif x == 0 and z > 0:
            print(f"Há {z} números certos no lugar errado")
        elif x == 0 and z == 0:
            print("Tudo errado")
if not ganhou:
     print("Você perdeu")


                

