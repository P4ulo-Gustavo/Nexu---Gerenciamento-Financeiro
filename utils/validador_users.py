import email_validator as ev #biblioteca que vai validar o email, já liberada no ambiente virtual do projeto, não é necessário instalar
from utils.formatadores import sanitize_cpf #função que remove caracteres não numericos do cpf, garantindo que o cpf seja composto apenas por numeros, ideal para validar e armazenar de forma padronizada, usada para comunicacao com o DB


def valida_email(email:str)->bool:
    if not email:
        return False
    try:
        ev.validate_email(email)
        return True
    except ev.EmailNotValidError as e:
        return False
    

def valida_password(password)-> bool:
    if not password:
        return False
    #declaração de cariáveis
    if len(password) > 7:
        char_espec = ['@', '*', '&', '-', '_', '#']
        
        return (
            any(c.isdigit() for c in password) and
            any(c.isalpha() for c in password) and
            any(c in char_espec for c in password)
        )
    return False

#A FUNÇÃO A BAIXO FOI FEITA POR IA-> CLAUDE. PARA ECONOMIZAR TIME(preguiça) -> mas foi testada e aprovada por mim, GUsta
def valida_cpf(cpf: str) -> bool:
    """
    Valida um CPF brasileiro verificando os dígitos verificadores.
    
    Returns:
        bool: True se o CPF é válido, False caso contrário
    """
    #sanitiza o cpf
    cpf = sanitize_cpf(cpf)

    # Verifica se o CPF é vazio ou None
    if not cpf:
        return False

    # Verifica se tem exatamente 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos são dígitos
    if not cpf.isdigit():
        return False
    
    # Verifica se não são todos números iguais (ex: 111.111.111-11)
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    
    # Verifica o primeiro dígito
    if int(cpf[9]) != digito1:
        return False
    
    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    
    # Verifica o segundo dígito
    if int(cpf[10]) != digito2:
        return False
    
    return True