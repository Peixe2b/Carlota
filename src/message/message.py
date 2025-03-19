from typing import Union

from pydantic import BaseModel

# Representa uma mensagem no whatsapp
# A mensagem deve ter um texto, um remetente e um destinatário
# O remetente é o nome de quem enviou a mensagem
# O destinatário é o nome de quem deve receber a mensagem
# A mensagem também pode ter um número de telefone
class Message(BaseModel):
    message: str
    sender: str # Nome do remetente (Carlota)
    receiver: str # Nome do destinatário
    number: Union[str, None] = None # Número de telefone do remetente

# Função que cria uma mensagem
# Ela deve retornar None caso não tenha um destinatário
# Ela deve retornar um erro caso não tenha um número de telefone
def create_message(sender: str,  receiver: str, message: str, number: str) -> Union[Message, None]:
    message = Message(
        message=message,
        sender=sender,
        receiver=receiver,
        number=number
    )

    if message.number is None:
        raise ValueError("The number parameter is required")
    
    if message.receiver is None or message.receiver == "":
        return None
    return message