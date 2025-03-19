from src.message.phone import PhoneNumber, PhoneNumberValidator

# Teste com a classe PhoneNumber e PhoneNumberValidator
if __name__ == "__main__":
    phone = PhoneNumber("96820-2469")
    print(phone.get_number())
    print(phone)
    
    print(PhoneNumberValidator.format_number(phone))
