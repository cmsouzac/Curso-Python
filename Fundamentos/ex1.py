# Desafio 
# - Pede seu nome e idade
# - Da um olá pra você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui 5 anos

nome = input("Qual é o seu nome? ")
idade = input("Qual é a sua idade? ")

print(f"Olá {nome}, você tem {idade} anos.")
print(f"Seu nome tem {len(nome)} letras.")
print(f"Daqui 5 anos você terá {int(idade) + 5} anos.")

