from re import compile

class PhoneNumber(object):
    """
    Essa classe representa um número de telefone
    Ela deve ser capaz de lidar apenas com o número de telefone simples, sem formatação
    O número de telefone deve ser composto por 8 ou 9 dígitos, exemplo: 96820-2469
    """

    def __init__(self, number: str):
        self.__number: str = number # 96820-2469
    
    # Essa função é chamada quando você tenta imprimir um objeto PhoneNumber
    # Ela deve retornar uma representação do objeto em forma de string (número do telefone)
    def __repr__(self):
        return "PhoneNumber({})".format(self.__number)

    def get_number(self) -> str:
        return self.__number


class PhoneNumberValidator(object):
    """
    Essa classe é responsável por validar um número de telefone
    """

    # Essa função avalia o número de telefone (sem formatação)
    # Ela deve retornar verdadeiro se o número for válido e falso caso contrário
    # O número de telefone deve ser composto por 8 ou 9 dígitos, exemplo: 96820-2469
    # Ela é uma função estátitica, então ela pode ser usada em qualquer lugar do código, sem instância da classe 
    @staticmethod
    def validator(phone: PhoneNumber) -> bool:
        basic_syntaxe = compile(r"[0-9]{4,5}-[0-9]{4}")

        # Retorna falso se o número de telefone for nulo ou vazio
        if phone.get_number() == None or phone.get_number() == "":
            return False
        
        if basic_syntaxe.match(phone.get_number()):
            return True
        return False

    # Essa função retorna o número de telefone (com formatado)
    @staticmethod
    def format_number(phone: PhoneNumber) -> str:    
        COUNTRY_CODE = "+55"
        MAIN_DDD = "11"
        return f"{COUNTRY_CODE} {MAIN_DDD} {phone.get_number()}" # +55 11 96820-2469
