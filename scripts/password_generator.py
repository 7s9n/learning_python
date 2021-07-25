from enum import Enum
import secrets
from string import (
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation,

)
from typing import Type

class PasswordType(Enum):
    ALL = (ascii_letters + digits + punctuation) #Letters, numbers and symbols
    UPPER_CASE = ascii_uppercase #Only uppercase letters
    LOWER_CASE = ascii_lowercase #Only lowercase letters
    NUMERIC = digits #Only numbers
    ALPHANUMERIC = ascii_letters + digits #Letters and numbers
    ALPHA = ascii_letters #Only letters
    SYMBOLS = punctuation #Only symbols

class Password:
    """An object of this class represents a single password generation process."""
    def __init__(self ,
    type: Type[PasswordType] = PasswordType.ALL ,
    length: int = 8
    ) -> None:
        self.type = type
        self.length = length

    def generate(self) -> str:
        return ''.join(secrets.choice(self.type.value) for _ in range(self.length) )

    @classmethod
    def create(cls , type: Type[PasswordType] = PasswordType.ALL , length: int = 8):
        return cls(type=type , length=length)

if __name__ == '__main__':
    password = Password.create(length=5 , type=PasswordType.LOWER_CASE).generate()
    print(password)
