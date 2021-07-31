import secrets
import string
import uuid
from typing import Any, List, Optional

def randstr(unique: bool = False,
                length: Optional[int] = None) -> str:
        """Generate random string value.

        This method can be especially useful when you need to generate
        only unique values in your provider. Just pass parameter unique=True.

        Basically, this method is just a simple wrapper around uuid.uuid4().

        :param unique: Generate only unique values.
        :param length: Length of string. Default range is (min=16, max=128).
        :return: Random string.

        """
        if unique:
            return str(uuid.uuid4().hex)

        if length is None:
            length = self.randint(16, 128)

        _string = string.ascii_letters + string.digits
        _string = ''.join(
            secrets.choice(_string) for _ in range(length)
        )
        return _string

if __name__ == '__main__':
    print(randstr(unique=False , length=6))
