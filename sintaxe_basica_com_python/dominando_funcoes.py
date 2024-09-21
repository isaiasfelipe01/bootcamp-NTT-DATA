def end():
    print("-"*30)
end()
# PARTE 1
print("PARTE 1")

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2("Isaias")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    return numero-1, numero+1

def func_3():
    print("Olá mundo!")

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))
print(func_3())

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

print(salvar_carro("Fiat", "Uno", 2010, "ABC-1234"))
print(salvar_carro(marca="Fiat", modelo="Uno", ano=2010, placa="ABC-1234"))
print(salvar_carro(**{"marca": "Fiat", "modelo": "Uno", "ano": 2010, "placa": "ABC-1234"}))
# *args valores como uma tupla
# **kwargs valores como um dicionário

def exibir_poema(data_extenso, *tupla, **dicionario):
    texto = "\n".join(tupla)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    return mensagem

print(exibir_poema("Sexta-feira, 26 de agosto de 2024","Zen of Python", "Beautful is better than ugly", "Explicit is better than implicit", "Simple is better than complex", "Complex is better than complicated", "Flat is better than nested", "Sparse is better than dense", "Readability counts", "Special cases aren't special enough to break the rules", "Although practicality beats purity", "Errors should never pass silently", "Unless explicitly silenced", "In the face of ambiguity, refuse the temptation to guess", "There should be one-- and preferably only one --obvious way to do it", "Although that way may not be obvious at first unless you're Dutch", "Now is better than never", "Although never is often better than *right* now", "If the implementation is hard to explain, it's a bad idea", "If the implementation is easy to explain, it may be a good idea", autor="Tim Peters", ano=1999))

end()

# PARTE 2
print("PARTE 2")

## so aceita 
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
criar_carro("Uno", 2010, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Flex")
#criar_carro(modelo="Uno", ano=2010, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Flex")

## Só aceita com a chave
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
#criar_carro("Uno", 2010, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Flex")
criar_carro(modelo="Uno", ano=2010, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Flex")

def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
criar_carro("Uno", 2010, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Flex")
criar_carro("Uno", 2010, "ABC-1234", "Fiat", motor="1.0", combustivel="Flex")

##objetos de primeira classe
def somar(x, y):
    return x + y
def subtrair(x, y):
    return x - y

def exibir_resultado(x, y, funcao):
    resultado = funcao(x, y)
    print(f"O resultado é = {resultado}")

print(exibir_resultado(10, 20, somar))
print(exibir_resultado(20, 10, subtrair))

op = somar
print(op(1, 23))

end()

salario = 2000
def salario_bonus(bonus):
    global salario

    lista_auxiliar = lista.copy()
    lista_auxiliar.append(2)
    print(f'Lista auxiliar: {lista_auxiliar}')

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = (salario_bonus(500))
print(salario_com_bonus)
print('lista:', lista)