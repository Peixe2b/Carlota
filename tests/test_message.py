import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import Message

class TestMessage:
    def test_basic_message(self):
        first_message = Message(
            message="Hello, World!"
        )
        assert first_message.message == "Hello, World!"
