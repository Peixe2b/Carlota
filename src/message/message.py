from typing import Union

from pydantic import BaseModel

class Message(BaseModel):
    message: str
    sender: str # Nome do remetente (Carlota)
    receiver: str # Nome do destinatário
    number: Union[str, None]=None # Número de telefone do remetente (Union[PhoneNumber, None])
