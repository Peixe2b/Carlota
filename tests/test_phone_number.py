import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.message.phone import PhoneNumber, PhoneNumberValidator

class TestPhoneNumber:
    
    def test_basic_phone_number_without_country_and_ddd(self):
        phone = PhoneNumber("96820-2469")
        assert phone.get_number() == "96820-2469"

    def test_complete_phone_number(self):
        phone = PhoneNumber("96820-2469")
        phone_number = PhoneNumberValidator.format_number(phone)
        assert phone_number == "+55 11 96820-2469"

    def test_valid_phone_number(self):
        phone = PhoneNumber("96820-2469")
        phone_number_is_valid = PhoneNumberValidator.validator(phone)
        assert phone_number_is_valid == True

    def test_invalid_phone_number(self):
        phone = PhoneNumber("312-2469")
        phone_number_is_invalid = PhoneNumberValidator.validator(phone)
        assert phone_number_is_invalid == False

    def test_repr(self):
        phone = PhoneNumber("96820-2469")        
        assert str(phone) == 'PhoneNumber(96820-2469)'
