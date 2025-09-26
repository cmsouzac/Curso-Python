print("(print) é uma palavra reservada de python!")

a = 1
b = 2
print("O valor de a é", a)
print("O valor de b é", b)

print("A soma de a + b é", a + b)
print("Ola", "mundo!", "Tudo", "bem?")

# Separador
print("Ola", "mundo!", sep="-")
print("Ola", "mundo!", sep="***")
print("Ola", "mundo!", sep="...")
print("Ola", "mundo!", sep="___")
print("Ola", "mundo!", "cruel", sep="/")

# Caractere especiais
print("Ola\nmundo!")
print("Ola\tmundo!")
print("Ola\rmundo!")
print("Ola\b mundo!")
print("Ola\\mundo!")
print('Ola\"mundo!')
print("Ola\'mundo!")

# Formatação texto a ser impresso a sintaxe do %
print("O valor de a é %d\nO valor de b é %i\nO valor de a + b  é %d" % (a, b, a + b))

# Input
nome = input("Qual é o seu nome? ")
print(nome)

num = input("Digite um numero: ")
print(num)
print(type(num)) # por padrão o input é uma string









