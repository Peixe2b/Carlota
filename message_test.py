import sys
import os

from src import *

if __name__ == "__main__":
    first_message = Message(
        message="Hello, World!",
        sender="Carlota",
        receiver="Me",
        number=PhoneNumberValidator.format_number(PhoneNumber("123456789"))
    )
    print(first_message.message)  # Hello, World!

    # Obter caminho do src.message.phone
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src", "message")))
    print(sys.path[-1])