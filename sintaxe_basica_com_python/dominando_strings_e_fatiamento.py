def end():
    print("-"*30)

end()
# CONHECENDO METODOS UTEIS DA CLASSE STRING
print("CONHECENDO METODOS UTEIS DA CLASSE STRING")

## maiusculo minusculo e titulo
curso = "pYtHoN"
print(curso.upper())
print(curso.lower())
print(curso.title())

## tirando espaço em branco
curso = "      Pythoon     "
print(curso.strip() + ".")
print(curso.rstrip() + ".")
print(curso.lstrip() + ".")

## junção e centralização
curso = "Python"
print(curso.center(14, "#"))
print(curso.center(14))
print(".".join(curso))

lista = ["Python", "Java", "C", "C++"]
print(", ".join(lista))
end()

# INTERPOLAÇÃO DE VARIAVEIS
print("INTERPOLAÇÃO DE VARIAVEIS")

nome = "Isaias"
idade = 23
profissao = "Estudante"
curso = "Ciências Atuariais"
pessoa = dict(nome=nome, idade=idade, profissao=profissao, curso=curso)

print("1 - Olá, me chamo %s, tenho %d anos, sou %s e curso %s." % (nome, idade, profissao, curso))
print("2 - Olá, me chamo {}, tenho {} anos, sou {} e curso {}.".format(nome, idade, profissao, curso))
print("2 - Olá, me chamo {nome}, tenho {idade} anos, sou {profissao} e curso {curso}.".format(nome=nome, idade=idade, profissao=profissao, curso=curso))
print("4 - Olá, me chamo {nome}, tenho {idade} anos, sou {profissao} e curso {curso}.".format(**pessoa))
print("5 - Olá, me chamo {3}, tenho {2} anos, sou {1} e curso {0}.".format(curso, profissao, idade, nome))
print(f"6 - Olá, me chamo {nome}, tenho {idade} anos, sou {profissao} e curso {curso}.")

pi = 3.14159
print(f"O valor de pi é {pi:.2f}")
print(f"O valor de pi é {pi:10.2f}")
end()

# FATIAMENTO DE STRINGS
print("FATIAMENTO DE STRINGS")

nome = "Isaias Felipe Silva de Sousa"
print(nome[0])
print(nome[:13])
print(nome[7:])
print(nome[7:13])
print(nome[7:13:2])
print(nome[:])
print(nome[::-1])
end()

# STRING MÚLTIPLAS LINHAS
nome = "Isaias"

mensagem = f'''
Olá, meu nome é {nome},
estou aprendendo python.
    Essa mensagem tem diferentes recursos.
'''
print(mensagem)
end()
print("""
      ========== MENU ==========

        1 - Depositar
        2 - Sacar
        3 - Sair
      ==========================

            Obrigado por usar nosso sistema!!!
""")
end()