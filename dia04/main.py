import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imagens = [pedra, papel, tesoura]
escolha = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura: "))
computador = random.randint(0, 2)

print(imagens[escolha])
print("O computador escolheu:")
print(imagens[computador])

if (escolha == 0 and computador == 2) or (escolha == 1 and computador == 0) or (escolha == 2 and computador == 1):
    print("Você venceu!")
elif escolha == computador:
    print("Empatou!")
else:
    print("Você perdeu!")