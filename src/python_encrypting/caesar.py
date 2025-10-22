"""
Caesar Cipher implementation.

The Caesar cipher is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced
by a letter some fixed number of positions down the alphabet.
"""


class CaesarCipher:
    """
    A simple Caesar Cipher implementation.

    Attributes:
        shift (int): The number of positions to shift each letter.
    """

    def __init__(self, shift: int = 3):
        """
        Initialize the Caesar Cipher with a shift value.

        Args:
            shift (int): The number of positions to shift. Defaults to 3.
        """
        self.shift = shift % 26

    def encrypt(self, text: str) -> str:
        """
        Encrypt the given text using Caesar cipher.

        Args:
            text (str): The plaintext to encrypt.

        Returns:
            str: The encrypted text.

        Example:
            >>> cipher = CaesarCipher(shift=3)
            >>> cipher.encrypt("HELLO")
            'KHOOR'
        """
        result = []

        for char in text:
            if char.isupper():
                result.append(chr((ord(char) - 65 + self.shift) % 26 + 65))
            elif char.islower():
                result.append(chr((ord(char) - 97 + self.shift) % 26 + 97))
            else:
                result.append(char)

        return "".join(result)

    def decrypt(self, text: str) -> str:
        """
        Decrypt the given text using Caesar cipher.

        Args:
            text (str): The ciphertext to decrypt.

        Returns:
            str: The decrypted text.

        Example:
            >>> cipher = CaesarCipher(shift=3)
            >>> cipher.decrypt("KHOOR")
            'HELLO'
        """
        result = []

        for char in text:
            if char.isupper():
                result.append(chr((ord(char) - 65 - self.shift) % 26 + 65))
            elif char.islower():
                result.append(chr((ord(char) - 97 - self.shift) % 26 + 97))
            else:
                result.append(char)

        return "".join(result)
