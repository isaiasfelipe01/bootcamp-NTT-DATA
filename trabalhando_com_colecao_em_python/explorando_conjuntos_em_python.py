print(set([1, 2, 3, 1, 2, 4, 10, 8, 9, 10]))
print(set("banana"))
print(set(("palio", "gol", "celta", "palio")))

linguagens = {"python", "Java", "C", "python"}
print(linguagens)

linguagens.add("Ruby")
print(linguagens)

linguagens.update(["Go", "R", "Kotlin"])
print(linguagens)

linguagens = list(linguagens)
print(linguagens[0])

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
#união
print(conjunto_a.union(conjunto_b))
print(conjunto_a | conjunto_b)
#interseção
print(conjunto_a.intersection(conjunto_b))
#diferença
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
#diferença simétrica
print(conjunto_a.symmetric_difference(conjunto_b))

#conjunto_a é subconjunto de conjunto_b
print(conjunto_a.issubset(conjunto_b))
#não tem elementos em comum
print(conjunto_a.isdisjoint(conjunto_b))

## removendo elementos
print(conjunto_a.pop())
print(conjunto_a)
print(conjunto_a.remove(2))
print(conjunto_a)

#o discard não gera erro caso o elemento não exista
print(conjunto_b.discard(4))
print(conjunto_b)
print(conjunto_b.discard(9))
print(conjunto_b)

print(1 in conjunto_a)