# LISTA: CRIAÇÃO E ACESSO AOS DADOS
print("LISTA: CRIAÇÃO E ACESSO AOS DADOS")

frutas = ['banana', 'maçã', 'uva', 'morango', 'abacaxi']
#frutas = []
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

## acesso direto
print(frutas[0])
print(frutas[-1])

matriz =[
    [1, "a", 3],
    ["b", 5, 6],
    [7, 8, "c"]
]
print(matriz)
print(matriz[0])

print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

carros = ["gol", "celta", "palio"]
for indice, carro in enumerate(carros):
    print((f"{indice}: {carro}"))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

pares = [numero for numero in quadrado if numero % 2 == 0]
print(pares)

# METODOS DA CLASSE LIST

lista = []
lista.append("a")
lista.append("python")
lista.append([40, 30, 20])
print(lista)

lista_copiada = lista.copy()
print(lista_copiada)
lista_copiada.append("a")
print(lista_copiada)

print(lista_copiada.count("a"))

linguagens = ["python", "java", "c"]
print(linguagens)
linguagens.extend(["c++", "ruby"])
print(linguagens)

print(linguagens.index("ruby"))

linguagens.insert(1, "javascript")
print(linguagens)

#removendo elementos
linguagens.pop()
print(linguagens)

linguagens.remove("c")
print(linguagens)

linguagens.reverse()
print(linguagens)

#ordem alfabetica
linguagens.sort()
print(linguagens)
#função biltin sorted
print(sorted(linguagens))

#ordem alfabetica reversa
linguagens.sort(reverse=True)
print(linguagens)
#do menor para o maior
linguagens.sort(key=lambda x: len(x))
print(linguagens)
#do maior para o maior
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

print(sorted(linguagens))

print([n**2 if n > 6 else n for n in range(10) if n % 2 == 0] )