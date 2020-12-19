# Atividade programação, validador de CPF - Matheus Henrique.
cpf = input("Digite o número do seu CPF(sem pontos): ")
# tamanho_cpf = len(cpf)
# print(tamanho_cpf)
if not (cpf.isdecimal() and len(cpf) == 11): # Analisa a quantidade de números digitados
    print("ERRO: Digite os 11 digitos completos")
    quit()

if cpf=='00000000000' or cpf=='11111111111' or cpf=='22222222222' or cpf=='33333333333' or cpf=='44444444444' or cpf=='55555555555' or cpf=='66666666666' or cpf=='77777777777' or cpf=='88888888888' or cpf=='99999999999':
    print("ERRO: Números repetidos são considerados validos, porem não são aceitos!") # Difere os CPF's validos porem não aceitos
    quit()

def cpf_valido(cpf): # Distribuição
    mult1 = (10,9,8,7,6,5,4,3,2)

    digito1 = 0     # Inicio da verificação do primeiro digito                    
    for n in range(9):
        digito1 += mult1[n]*int(cpf[n])
    if digito1 % 11 < 2:
        digito1 = '0'
    else:
        digito1 = str(11 - (digito1 % 11))

    cpf1 = cpf[:-2] + digito1

    mult2 = (11,10,9,8,7,6,5,4,3,2)

    digito2 = 0    # Inicio da verificação do primeiro digito
    for n in range(10):
        digito2 += mult2[n]*int(cpf1[n])
    if digito2 % 11 < 2:
        digito2 = '0'
    else:
        digito2 = str(11 - (digito2 % 11))

    if cpf == cpf1 + digito2: # Condição para validação do CPF
        return True
    else:
        return False
if cpf_valido(cpf): 
    print("O CPF:",cpf, "é valido!") # Positiva
else:
    print("O CPF:",cpf, "é invalido!") # Negativa
