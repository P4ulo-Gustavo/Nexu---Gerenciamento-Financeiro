
#função responsável por remover caracteres não numericos do cpf, garantindo que o cpf seja composto apenas por numeros
#idel para validar e armazenar de forma padronizada, usada para comunicacao com o DB
def sanitize_cpf(cpf:str)->str:
    #declaração de variaveis
    new_cpf = str()

    for n in cpf:
        if n.isdigit():
            new_cpf += n

    return new_cpf
