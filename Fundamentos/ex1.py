# Desafio 
# - Pede seu nome e idade
# - Da um olá pra você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui 5 anos

# Pega os inputs
nome = input("Qual é o seu nome?\nDigite aqui: ")
idade = input("Qual é a sua idade? ")

# Exibe os resultados
print('--' * 10)
print(f"Olá {nome}, você tem {idade} anos.")
# print(f'olá, {nome}!') sintaxe dinamica
print(f"Seu nome tem {len(nome)} letras.")
print(f"Daqui 5 anos você terá {int(idade) + 5} anos.")
print('--' * 15)