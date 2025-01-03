print("Bem-vindo à calculadora de gorjetas!")
conta_total = float(input("Qual foi o valor total da conta? R$"))
gorjeta = int(input("Quanto de gorjeta você gostaria de dar? 10, 12 ou 15? "))
pessoas_dividir = int(input("Quantas pessoas vão dividir a conta? "))

valor_por_pessoa = (gorjeta / 100 * conta_total + conta_total) / pessoas_dividir

print(f"Cada pessoa deve pagar: R${valor_por_pessoa:.2f}")
