# # =================================================
# Controle de Fluxo: if, else, elif     
# Autor: Cristian Souza
# Descrição: Sintaxe e exemplos de estruturas condicionais em Python
# =================================================


# ==== Exemplo 1 ====
def verificar_idade(idade: int) -> str:
    if idade >= 18:
        return "Você é maior de idade\nVocê pode entrar na boate"
    else:
        return "Você é menor de idade\nNão pode entrar na boate"

# ==== Exemplo 2 ====
def comparar_numeros(a: int, b: int) -> str:
    if b > a:
        return "b é maior que a"
    elif a == b:
        return "a e b são iguais"
    else:
        return "a é maior que b"


# ==== Exemplo 3 ====
def verificar_maior(a: int, b: int) -> str:
    if b > a:
        return "b é maior que a"
    else:
        return "b não é maior que a"
    
    
    
    
# ==== Testes ====
print(verificar_idade(20))
print(verificar_idade(16))

