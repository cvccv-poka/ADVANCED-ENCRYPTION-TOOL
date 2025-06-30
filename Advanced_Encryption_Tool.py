import os
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

class AdvancedEncryptionTool:
    def __init__(self):
        pass

    def generate_key(self):
        return os.urandom(32) # AES-256 requires a 32-byte key

    def encrypt_file(self, input_filepath, output_filepath, key):
        try:
            with open(input_filepath, 'rb') as f:
                plaintext = f.read()

            iv = os.urandom(16) # AES block size is 16 bytes, IV must be same size

            padder = padding.PKCS7(algorithms.AES.block_size).padder()
            padded_data = padder.update(plaintext) + padder.finalize()

            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_data) + encryptor.finalize()

            with open(output_filepath, 'wb') as f:
                f.write(iv + ciphertext)
            print(f"File encrypted successfully to {output_filepath}")
            return True
        except Exception as e:
            print(f"Error encrypting file: {e}")
            return False

    def decrypt_file(self, input_filepath, output_filepath, key):
        try:
            with open(input_filepath, 'rb') as f:
                encrypted_data = f.read()

            iv = encrypted_data[:16]
            ciphertext = encrypted_data[16:]

            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

            with open(output_filepath, 'wb') as f:
                f.write(plaintext)
            print(f"File decrypted successfully to {output_filepath}")
            return True
        except Exception as e:
            print(f"Error decrypting file: {e}")
            print("Possible causes: Incorrect key, corrupted file, or wrong algorithm/mode.")
            return False

if __name__ == "__main__":
    tool = AdvancedEncryptionTool()

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python encryption_tool.py generate_key")
        print("  python encryption_tool.py encrypt <input_file> <output_file> <hex_key>")
        print("  python encryption_tool.py decrypt <input_file> <output_file> <hex_key>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "generate_key":
        key = tool.generate_key()
        print(f"Generated AES-256 Key (Hex): {key.hex()}")
        print("WARNING: Store this key securely! Without it, you cannot decrypt your data.")
    elif command == "encrypt":
        if len(sys.argv) != 5:
            print("Usage: python encryption_tool.py encrypt <input_file> <output_file> <hex_key>")
            sys.exit(1)
        input_file = sys.argv[2]
        output_file = sys.argv[3]
        hex_key = sys.argv[4]
        try:
            key = bytes.fromhex(hex_key)
            if len(key) != 32:
                raise ValueError("Key must be 32 bytes for AES-256 (64 hex characters).")
            tool.encrypt_file(input_file, output_file, key)
        except ValueError as e:
            print(f"Key error: {e}")
            sys.exit(1)
    elif command == "decrypt":
        if len(sys.argv) != 5:
            print("Usage: python encryption_tool.py decrypt <input_file> <output_file> <hex_key>")
            sys.exit(1)
        input_file = sys.argv[2]
        output_file = sys.argv[3]
        hex_key = sys.argv[4]
        try:
            key = bytes.fromhex(hex_key)
            if len(key) != 32:
                raise ValueError("Key must be 32 bytes for AES-256 (64 hex characters).")
            tool.decrypt_file(input_file, output_file, key)
        except ValueError as e:
            print(f"Key error: {e}")
            sys.exit(1)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
