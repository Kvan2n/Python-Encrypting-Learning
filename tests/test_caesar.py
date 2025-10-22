"""
Tests for the Caesar Cipher implementation.
"""

import unittest
from src.python_encrypting.caesar import CaesarCipher


class TestCaesarCipher(unittest.TestCase):
    """Test cases for CaesarCipher class."""

    def setUp(self):
        """Set up test fixtures."""
        self.cipher = CaesarCipher(shift=3)

    def test_encrypt_uppercase(self):
        """Test encryption of uppercase letters."""
        self.assertEqual(self.cipher.encrypt("HELLO"), "KHOOR")
        self.assertEqual(self.cipher.encrypt("ABC"), "DEF")
        self.assertEqual(self.cipher.encrypt("XYZ"), "ABC")

    def test_encrypt_lowercase(self):
        """Test encryption of lowercase letters."""
        self.assertEqual(self.cipher.encrypt("hello"), "khoor")
        self.assertEqual(self.cipher.encrypt("abc"), "def")
        self.assertEqual(self.cipher.encrypt("xyz"), "abc")

    def test_encrypt_mixed_case(self):
        """Test encryption of mixed case letters."""
        self.assertEqual(self.cipher.encrypt("Hello World"), "Khoor Zruog")

    def test_encrypt_with_special_characters(self):
        """Test that special characters are not encrypted."""
        self.assertEqual(self.cipher.encrypt("Hello, World!"), "Khoor, Zruog!")
        self.assertEqual(self.cipher.encrypt("123 ABC"), "123 DEF")

    def test_decrypt_uppercase(self):
        """Test decryption of uppercase letters."""
        self.assertEqual(self.cipher.decrypt("KHOOR"), "HELLO")
        self.assertEqual(self.cipher.decrypt("DEF"), "ABC")
        self.assertEqual(self.cipher.decrypt("ABC"), "XYZ")

    def test_decrypt_lowercase(self):
        """Test decryption of lowercase letters."""
        self.assertEqual(self.cipher.decrypt("khoor"), "hello")
        self.assertEqual(self.cipher.decrypt("def"), "abc")
        self.assertEqual(self.cipher.decrypt("abc"), "xyz")

    def test_decrypt_mixed_case(self):
        """Test decryption of mixed case letters."""
        self.assertEqual(self.cipher.decrypt("Khoor Zruog"), "Hello World")

    def test_decrypt_with_special_characters(self):
        """Test that special characters are not decrypted."""
        self.assertEqual(self.cipher.decrypt("Khoor, Zruog!"), "Hello, World!")

    def test_encrypt_decrypt_roundtrip(self):
        """Test that encryption followed by decryption returns original text."""
        original = "The Quick Brown Fox Jumps Over The Lazy Dog!"
        encrypted = self.cipher.encrypt(original)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, original)

    def test_custom_shift(self):
        """Test Caesar cipher with different shift values."""
        cipher_1 = CaesarCipher(shift=1)
        self.assertEqual(cipher_1.encrypt("ABC"), "BCD")

        cipher_13 = CaesarCipher(shift=13)
        self.assertEqual(cipher_13.encrypt("HELLO"), "URYYB")

    def test_shift_wraparound(self):
        """Test that shift values greater than 26 wrap around correctly."""
        cipher_29 = CaesarCipher(shift=29)  # Same as shift=3
        self.assertEqual(cipher_29.encrypt("HELLO"), "KHOOR")


if __name__ == "__main__":
    unittest.main()
