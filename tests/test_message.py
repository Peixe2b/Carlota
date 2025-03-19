import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import Message, PhoneNumber, PhoneNumberValidator

class TestMessage:
    GIRLFRIEND = "Carlota"
    MY_PHONE_NUMBER = PhoneNumberValidator.format_number(PhoneNumber("123456789"))

    def test_basic_message_no_validation(self):
        first_message = Message(
            message="Hello, World!",
            sender=self.GIRLFRIEND,
            receiver="Me",
            number=self.MY_PHONE_NUMBER
        )
        assert first_message.message == "Hello, World!"
    
    def test_basic_message_with_ten_lines(self):
        assert True

    def test_basic_message_with_lot_of_spaces(self):
        assert True

    def test_basic_message_with_no_receiver(self):
        assert True
    
    def test_basic_message_with_no_sender(self):
        assert True
