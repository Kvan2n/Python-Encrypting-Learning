# Python-Encrypting

A Python library for learning encryption algorithms. This project provides simple, educational implementations of various encryption techniques.

## Features

- 🔐 Caesar Cipher implementation
- 📚 Well-documented code with examples
- ✅ Comprehensive test coverage
- 🎓 Educational focus with clear explanations

## Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/Kvan2n/Python-Encrypting.git
cd Python-Encrypting

# Install the package
pip install -e .

# Or install with development dependencies
pip install -e ".[dev]"
```

### Using pip (when published)

```bash
pip install python-encrypting
```

## Quick Start

```python
from python_encrypting import CaesarCipher

# Create a cipher with shift of 3
cipher = CaesarCipher(shift=3)

# Encrypt a message
encrypted = cipher.encrypt("HELLO WORLD")
print(encrypted)  # Output: KHOOR ZRUOG

# Decrypt the message
decrypted = cipher.decrypt(encrypted)
print(decrypted)  # Output: HELLO WORLD
```

## Usage Examples

### Basic Caesar Cipher

```python
from python_encrypting import CaesarCipher

# Create a cipher
cipher = CaesarCipher(shift=3)

# Encrypt
message = "Secret Message"
encrypted = cipher.encrypt(message)
print(f"Encrypted: {encrypted}")

# Decrypt
decrypted = cipher.decrypt(encrypted)
print(f"Decrypted: {decrypted}")
```

### ROT13 Cipher

ROT13 is a special case of Caesar cipher with shift of 13:

```python
from python_encrypting import CaesarCipher

# ROT13 cipher
rot13 = CaesarCipher(shift=13)

message = "Hello World"
encrypted = rot13.encrypt(message)
print(f"Encrypted: {encrypted}")  # Output: Uryyb Jbeyq
```

### Running Examples

Check out the examples directory for more usage examples:

```bash
python examples/caesar_cipher_example.py
```

## Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/Kvan2n/Python-Encrypting.git
cd Python-Encrypting

# Install development dependencies
pip install -r requirements-dev.txt

# Install package in editable mode
pip install -e .
```

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=src/python_encrypting --cov-report=html

# Run specific test file
python -m pytest tests/test_caesar.py
```

### Code Quality

```bash
# Format code with black
black src/ tests/ examples/

# Check code style with flake8
flake8 src/ tests/ examples/

# Type checking with mypy
mypy src/
```

## Project Structure

```
Python-Encrypting/
├── src/
│   └── python_encrypting/
│       ├── __init__.py
│       └── caesar.py
├── tests/
│   ├── __init__.py
│   └── test_caesar.py
├── examples/
│   └── caesar_cipher_example.py
├── docs/
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml
├── setup.py
├── requirements.txt
└── requirements-dev.txt
```

## Encryption Algorithms

### Caesar Cipher

The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

**How it works:**
- Choose a shift value (e.g., 3)
- Each letter is replaced by the letter that is 'shift' positions ahead in the alphabet
- For example, with shift=3: A→D, B→E, C→F, etc.
- The alphabet wraps around: X→A, Y→B, Z→C

**Security Note:** Caesar cipher is not secure for real-world applications and should only be used for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Roadmap

Future algorithms to implement:
- [ ] Vigenère Cipher
- [ ] Substitution Cipher
- [ ] Transposition Cipher
- [ ] RSA (educational implementation)
- [ ] AES (using existing libraries)

## Resources

- [Cryptography on Wikipedia](https://en.wikipedia.org/wiki/Cryptography)
- [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Python Cryptography Documentation](https://cryptography.io/)

## Disclaimer

This library is for educational purposes only. The implementations are meant to demonstrate cryptographic concepts and should **not** be used for securing real data. For production use, please use established cryptographic libraries like `cryptography` or `PyCryptodome`.
