#!/usr/bin/env python3
"""
Example usage of the python-encrypting library.

This script demonstrates how to use the Caesar cipher for encryption and decryption.
"""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from python_encrypting import CaesarCipher


def main():
    """Demonstrate Caesar cipher encryption and decryption."""
    print("=" * 60)
    print("Python-Encrypting: Caesar Cipher Example")
    print("=" * 60)
    print()

    # Create a Caesar cipher with shift of 3
    cipher = CaesarCipher(shift=3)

    # Example 1: Simple encryption
    plaintext1 = "HELLO WORLD"
    encrypted1 = cipher.encrypt(plaintext1)
    decrypted1 = cipher.decrypt(encrypted1)

    print("Example 1: Basic Encryption")
    print(f"  Plaintext:  {plaintext1}")
    print(f"  Encrypted:  {encrypted1}")
    print(f"  Decrypted:  {decrypted1}")
    print()

    # Example 2: Mixed case with punctuation
    plaintext2 = "The Quick Brown Fox Jumps Over The Lazy Dog!"
    encrypted2 = cipher.encrypt(plaintext2)
    decrypted2 = cipher.decrypt(encrypted2)

    print("Example 2: Mixed Case with Punctuation")
    print(f"  Plaintext:  {plaintext2}")
    print(f"  Encrypted:  {encrypted2}")
    print(f"  Decrypted:  {decrypted2}")
    print()

    # Example 3: Different shift value
    cipher_rot13 = CaesarCipher(shift=13)
    plaintext3 = "ROT13 is a special case of Caesar cipher"
    encrypted3 = cipher_rot13.encrypt(plaintext3)
    decrypted3 = cipher_rot13.decrypt(encrypted3)

    print("Example 3: ROT13 (shift=13)")
    print(f"  Plaintext:  {plaintext3}")
    print(f"  Encrypted:  {encrypted3}")
    print(f"  Decrypted:  {decrypted3}")
    print()

    # Example 4: Interactive mode
    print("=" * 60)
    print("Interactive Mode")
    print("=" * 60)

    try:
        shift = int(input("Enter shift value (1-25): "))
        message = input("Enter message to encrypt: ")

        interactive_cipher = CaesarCipher(shift=shift)
        encrypted = interactive_cipher.encrypt(message)

        print(f"\nEncrypted message: {encrypted}")
        print(f"Decrypted message: {interactive_cipher.decrypt(encrypted)}")
    except (ValueError, KeyboardInterrupt):
        print("\nSkipping interactive mode.")

    print()
    print("=" * 60)


if __name__ == "__main__":
    main()
