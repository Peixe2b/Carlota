import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.message.phone import PhoneNumber

class TestPhoneNumber:
    def test_basic_phone_number_without_country_and_ddd(self):
        phone = PhoneNumber("96820-2469")
        
        assert str(phone) == 'PhoneNumber(96820-2469)'
        assert phone.get_number() == "96820-2469"

    def test_complete_phone_number(self):
        assert True

    def test_valid_phone_number(self):
        phone = PhoneNumber("96820-2469")
        assert True

    def test_invalid_phone_number(self):
        assert True

    def test_repr(self):
        assert True
