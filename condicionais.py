saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Reazliando saque!")

if saldo < saque:
    print("Saldo insuficiente!")


maior_idade = 18
idade_especial = 17
idade = int(input("Informe sua idade: "))

if idade >= maior_idade:
    print("Você está apto a tirar sua CNH!")
elif idade == 17:
    print("Pode fazer as aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Você não está apto a tirar sua CNH.")




