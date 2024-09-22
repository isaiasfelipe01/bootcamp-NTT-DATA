## maneiras de criar um dicionário
pessoa = {"nome": "Isaias", "idade": 23}
print(pessoa)
pessoa = dict(nome="Isaias", idade=23)
print(pessoa)

## adicionando informações em um dicionário'
pessoa["cidade"] = "João Pessoa"
print(pessoa)

## maneiras de acessar um dicionário
print(pessoa["nome"])
print(pessoa["idade"])

## alterando informações de um dicionário
pessoa["nome"] = "Felipe"
pessoa["idade"] = 24
print(pessoa)


contatos = {
    "isaias.@gmail.com": {"nome": "Isaias", "telefone": "9999-9999"},
    "felipe.@gmail.com": {"nome": "Felipe", "telefone": "8888-8888", "extra": {"a": 1}}
}
## existencia de informção em um dicionário
resultado = "isaias.@gmail.com" in contatos
print(resultado)

## acessando informações de um dicionário dentro de outro
telefone = contatos["isaias.@gmail.com"]["telefone"]
print(telefone)

extra = contatos["felipe.@gmail.com"]["extra"]["a"]
print(extra)

for contato, chave in contatos.items():
    print(contato, chave)

#pegando valor de uma chave, se não existir retorna None
print(contatos.get("chave"))

contatos["felipe.@gmail.com"].get("chave", {"chave não encontrada"})
print(contatos)

#lista de tuplas
print(contatos.items())

#retorna somente as chaves do dicionário
print(contatos.keys())

#remove um item do dicionário
print(contatos.pop("isaias.@gmail.com", {"não encontrado"}))

#adiciona uma chave com valor padrão
contatos["felipe.@gmail.com"].setdefault("pais", "Brasil")
print(contatos)

#apaga um item do dicionário
del contatos["felipe.@gmail.com"]["extra"]
print(contatos)

# criando uma copia de um dicionário
copia_contatos = contatos.copy()
contatos.clear()
print(contatos)
print(copia_contatos)

#criando conjunto de chaves
print(dict.fromkeys(["nome", "idade", "cidade", "telefone"]))
#criando conjunto de chaves com valor padrão
print(dict.fromkeys(["nome", "idade", "cidade", "telefone"], "desconhecido"))

