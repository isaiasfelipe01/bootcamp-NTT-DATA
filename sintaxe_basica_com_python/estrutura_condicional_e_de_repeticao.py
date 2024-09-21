import sys
def end():
    print("-"*30)
end()
# INTERAÇÃO E BLOCOS
print("INTERAÇÃO E BLOCOS")
def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire o seu dinherio na boca do caixa.")
    
    print("Obrigado por ser nosso cliente. Tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor

    print("Depósito realizado com sucesso!")
    print("Seu novo saldo é de R$ ", saldo)

sacar(100)
depositar(200)
end()

# ESTRUTURAS CONDICIONAIS
print("ESTRUTURAS CONDICIONAIS")

saldo = 2000.0
saque = float(input("Imforme o valor do saque: "))
if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extreato: "))
if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
elif opcao == 2:
    print("Exibindo extrato...")
else:
    sys.exit("Opção inválida!")

print("IF aninhado")
conta_normal = True
conta_universitaria = False
saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente!")

print("IF Ternario")

saldo = 2000
saque = 2500
status = "Sucesso" if saldo >= saque else "Falha"
print(f'{status} ao realizar o saque!')

end()

# ESTRUTURAS DE REPETIÇÃO
print("ESTRUTURAS DE REPETIÇÃO")
texto = str(input("Informe um texto: "))
vogais = "AEIOU"
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")
else:
    print("")
    print("Fim do texto!")

for nuemro in range(0,51, 5):
    print(nuemro, end=" ")

for numero in range(100):
    if numero == 12:
        break
    print(numero, end=" ")

for numero in range(100):
    if numero == 12:
        continue
    print(numero, end=" ")

## while
opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair: "))
    if opcao == 1:
        print("Realizando saque...")
    elif opcao == 2:
        print("Exibindo extrato...")
    elif opcao == 0:
        print("Obrigado por usar nosso sistema bancário, até logo!")
        break
    else:
        print("Opção inválida!")