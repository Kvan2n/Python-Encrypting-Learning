from cryptography.fernet import Fernet

key = Fernet.generate_key()
message = "this is my secret message".encode()
f = Fernet(key)

print(f.encrypt(message).decode())