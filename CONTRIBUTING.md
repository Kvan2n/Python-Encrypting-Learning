# Contributing to Python-Encrypting

Thank you for your interest in contributing to Python-Encrypting! This document provides guidelines for contributing to this project.

## Code of Conduct

Please be respectful and constructive in your interactions with other contributors.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear title and description
- Steps to reproduce the bug
- Expected vs actual behavior
- Python version and OS
- Any relevant code samples

### Suggesting Enhancements

Enhancement suggestions are welcome! Please create an issue with:
- A clear title and description
- Rationale for the enhancement
- Example use cases
- Any implementation ideas (optional)

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding guidelines below
3. **Add tests** for any new functionality
4. **Update documentation** if needed
5. **Ensure tests pass** by running `pytest`
6. **Format your code** with `black`
7. **Submit a pull request** with a clear description

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Python-Encrypting.git
cd Python-Encrypting

# Install development dependencies
pip install -r requirements-dev.txt

# Install package in editable mode
pip install -e .
```

## Coding Guidelines

### Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use `black` for code formatting (line length: 88)
- Use `flake8` for linting
- Write docstrings for all public functions, classes, and modules
- Use type hints where appropriate

### Testing

- Write tests for all new functionality
- Maintain or improve code coverage
- Use descriptive test names
- Follow the existing test structure

### Documentation

- Update README.md if adding new features
- Write clear docstrings with examples
- Add comments for complex logic
- Update examples if needed

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/python_encrypting

# Run specific test
pytest tests/test_caesar.py
```

## Code Quality Checks

```bash
# Format code
black src/ tests/ examples/

# Check style
flake8 src/ tests/ examples/

# Type checking
mypy src/
```

## Commit Messages

Write clear, concise commit messages:
- Use present tense ("Add feature" not "Added feature")
- Start with a capital letter
- Keep the first line under 50 characters
- Add detailed description if needed

Example:
```
Add Vigenère cipher implementation

- Implement encrypt and decrypt methods
- Add comprehensive tests
- Update documentation with examples
```

## Adding New Encryption Algorithms

When adding a new encryption algorithm:

1. **Create a new module** in `src/python_encrypting/` (e.g., `vigenere.py`)
2. **Implement the algorithm** as a class with `encrypt()` and `decrypt()` methods
3. **Add comprehensive tests** in `tests/test_<algorithm>.py`
4. **Create an example** in `examples/<algorithm>_example.py`
5. **Update `__init__.py`** to export the new class
6. **Update README.md** with the new algorithm documentation

## Questions?

If you have questions, feel free to:
- Open an issue for discussion
- Comment on existing issues or pull requests

Thank you for contributing to Python-Encrypting! 🎉
