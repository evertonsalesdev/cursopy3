# Operadores lógicos

# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras.
# se qualquer valor for considerado falso, a expressão inteira
# será avalaida naquele valor
# São considerados falsy (que você já viu)

# 0 0.0 '' False

# Também existe o tipo None que é usado para representar um não valor



entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'



if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou no sistema')

elif entrada == 'S':
    quit()

else:
    print('Digite algo válido! ')




# Avaliação de curto circuito



if 0 and 1:
    print(True and 1 )