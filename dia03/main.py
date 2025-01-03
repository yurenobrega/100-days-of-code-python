print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Bem-vindo a Ilha do Tesouro")
print("Sua missão é encontrar o tesouro.")

escolha1 = input("Você está em uma encruzilhada. Para onde você quer ir? Digite 'esquerda' ou 'direita': ")
if escolha1 == "direita":
    escolha2 = input("Você chegou a um lago. Há uma ilha no meio do lago. Digite 'esperar' para esperar por um barco. Digite 'nadar' para atravessar nadando: ")
    if escolha2 == "esperar":
        escolha3 = input("Você chega à ilha sem ferimentos. Há uma casa com 3 portas. Uma vermelha, uma amarela e uma azul. Qual cor você escolhe? ")
        if escolha3 == "vermelha":
            print("É um quarto cheio de fogo. Fim de jogo.")
        elif escolha3 == "azul":
            print("Você entra em um quarto cheio de feras. Fim de jogo.")
        elif escolha3 == "amarela":
            print("Você encontrou o tesouro! Você venceu!")
        else:
            print("Você escolheu uma porta que não existe. Fim de jogo.")
    else:
        print("Você foi atacado por uma piranha raivosa. Fim de jogo.")
else:
    print("Você caiu em um buraco. Fim de jogo.")
    
