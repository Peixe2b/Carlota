import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import Message, PhoneNumber, PhoneNumberValidator, create_message

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
        message_text = "Hello, World!\n"*10
        message = create_message(
            sender=self.GIRLFRIEND,
            receiver="Me",
            message=message_text,
            number=self.MY_PHONE_NUMBER
        )
        assert message.message == message_text

    def test_message_receiver_is_null(self):
        message = create_message(
            sender=self.GIRLFRIEND,
            receiver="",
            message="Hello, World!",
            number=self.MY_PHONE_NUMBER
        )
        assert message == None

    def test_basic_message_with_number(self):
        message = create_message(
            sender=self.GIRLFRIEND,
            receiver="Me",
            message="Hello, World!",
            number=self.MY_PHONE_NUMBER
        )
        assert message.number == "+55 11 123456789"
