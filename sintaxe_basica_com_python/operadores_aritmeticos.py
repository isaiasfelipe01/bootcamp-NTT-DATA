def end():
    return print('-'*30)
end()

# OPERADORES ARITMÉTICOS
print("OPERADORES ARITMÉTICOS")
produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 * produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 % produto_2)
print(produto_1 ** produto_2)

x = (10 + 5) * 4
y = (10 / 2) + (25 * 2) - (2 ** 2)

print(x)
print(y)
end()

# OPERADORES DE COMPARAÇÃO
print("OPERADORES DE COMPARAÇÃO")
saldo = 200
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)
end()

# OPERADORES DE ATRIBUIÇÃO
print("OPERADORES DE ATRIBUIÇÃO")

## Atribuição simples
saldo = 500
print(saldo)

## Atribuição com adição
saldo += 200
print(saldo)

## Atribuição com subtração
saldo -= 100
print(saldo)

## Atribuição com multiplicação
saldo *= 2
print(saldo)

## Atribuição com divisão
saldo //= 2
print(saldo)

## etc...
end()

# OPERADORES LÓGICOS
print("OPERADORES LÓGICOS")

saldo = 1000
saque = 200
limite = 100

## Operador E
print(saldo >= saque and saque <= limite)
## Operador OU
print(saldo >= saque or saque <= limite)
## Operador de NEGAÇÃO
print(not saldo >= saque)
print(not saque <= limite)


saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = (saldo >= saque and saque <= limite or conta_especial and saldo >= saque)
print(exp)

exp_2 = ((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))
print(exp_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)
end()

# OPERADORES DE IDENTIDADE
print("OPERADORES DE IDENTIDADE")

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 500, 200

print(curso is nome_curso)
print(curso is not nome_curso)

print(saldo is limite)
print(saldo is not limite)

end()

# OPERADORES DE ASSOCIAÇÃO
print("OPERADORES DE ASSOCIAÇÃO")

curso = "Curso de Python"
frutas = ["maçã", "banana", "laranja"]
saques = [1500, 100]

print("Python" in curso)
print("maçã" not in frutas)
print(200 in saques)
