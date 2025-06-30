# ADVANCED-ENCRYPTION-TOOL

*COMPANY*: CODTECH IT SOLUTIONS 

*NAME* : VIVEK KUMBHAKAR

*INTERN ID* :CT04DF361

*DOMAIN* : CYBERSECURITY AND ETHICAL HACKING

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

##Project Description
In an era where data privacy and security are paramount, robust encryption is not just a feature but a necessity. This project, the Advanced Encryption Tool, provides a practical implementation of symmetrical file encryption and decryption using the highly secure AES-256 (Advanced Encryption Standard with a 256-bit key) algorithm. It addresses the critical need to protect sensitive information at rest, ensuring that even if unauthorized individuals gain access to files, their contents remain unintelligible without the correct cryptographic key.

The primary problem this tool solves is the unauthorized disclosure of data. Whether it's confidential documents, personal files, or critical system backups, storing data without proper encryption exposes it to significant risks. Traditional password protection can be weak, and simple encoding offers no real security. AES-256 is a globally recognized and widely adopted encryption standard used by governments, financial institutions, and security experts worldwide. Implementing this tool helps to understand how modern cryptographic algorithms are applied to secure data.

The importance of an encryption tool like this lies in its ability to:

Ensure Data Confidentiality: Protect sensitive information from prying eyes.

Meet Compliance Requirements: Many regulations (e.g., GDPR, HIPAA) mandate data encryption to safeguard personal and sensitive information.

Secure Data at Rest: Protect files stored on hard drives, USB drives, or cloud storage.

Enhance Privacy: Empower individuals and organizations to control access to their digital assets.

Educate on Cryptography: Provide a hands-on understanding of symmetric encryption, key management, Initialization Vectors (IVs), and padding.

This project is a critical exercise in defensive cybersecurity, translating complex cryptographic concepts into a functional and user-friendly application.

Features & Functionality
This Python-based Advanced Encryption Tool offers three core functionalities, all centered around the AES-256 algorithm:

Key Generation:

Generates a cryptographically strong, random 256-bit (32-byte) key.

Outputs the key in hexadecimal format for easy display and copying.

Emphasizes the critical importance of securely storing and managing this key, as its loss means irreversible loss of encrypted data, and its compromise means data exposure.

File Encryption (AES-256 CBC Mode):

Takes an input file, an output file path, and a 256-bit hexadecimal key as arguments.

Reads the entire content of the input file into memory.

Generates a unique, random Initialization Vector (IV) for each encryption operation. The IV is crucial for security in CBC mode, ensuring that identical plaintexts produce different ciphertexts.

Applies PKCS7 padding to the plaintext. AES is a block cipher, meaning it encrypts data in fixed-size blocks (16 bytes for AES). Padding ensures that the plaintext always fits perfectly into these blocks.

Encrypts the padded data using the AES-256 algorithm in Cipher Block Chaining (CBC) mode. CBC mode links each ciphertext block to the previous one, enhancing security.

Combines the unique IV with the generated ciphertext and writes this combined binary data to the specified output file. The IV is prepended to the ciphertext so it can be used during decryption.

File Decryption (AES-256 CBC Mode):

Takes an encrypted input file, an output file path, and the exact 256-bit hexadecimal key used for encryption.

Reads the encrypted file, extracting the IV from the first 16 bytes and the actual ciphertext from the remaining data.

Decrypts the ciphertext using the provided key, the extracted IV, and AES-256 in CBC mode.

Removes the PKCS7 padding to restore the original plaintext content.

Writes the recovered plaintext to the specified output file.

Includes basic error handling for incorrect keys or corrupted files, making the tool more robust.

Technologies Used
Python 3.x: The primary development language.

cryptography Library: This is the cornerstone of the project, providing secure cryptographic primitives. Specifically:

cryptography.hazmat.primitives.ciphers: For implementing AES algorithm and CBC mode.

cryptography.hazmat.primitives.padding: For PKCS7 padding, a standard padding scheme for block ciphers.

cryptography.hazmat.backends.default_backend: Provides the cryptographic backend implementation.

os Module: Used for generating cryptographically secure random bytes for keys (os.urandom()) and Initialization Vectors.

sys Module: For processing command-line arguments to control the tool's operations (generate key, encrypt, decrypt).

File I/O: Standard Python file operations (open with rb and wb modes) for reading and writing binary file content.

How to Run / Usage
Clone the Repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name/Task4_AdvancedEncryptionTool
Install Dependencies:

Bash

pip install cryptography
Generate a Key:
You must first generate a key. This key is vital for both encryption and decryption. Keep it extremely safe!

Bash

python encryption_tool.py generate_key
(Example output: Generated AES-256 Key (Hex): <64-character-hex-string>)

Encrypt a File:
Replace <YOUR_HEX_KEY> with the 64-character hex key generated in the previous step.

Bash

python encryption_tool.py encrypt <input_file_path> <output_file_path> <YOUR_HEX_KEY>
# Example: python encryption_tool.py encrypt secret_doc.txt secret_doc.enc 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
Decrypt a File:
Use the exact same key to decrypt.

Bash

python encryption_tool.py decrypt <encrypted_file_path> <decrypted_output_file_path> <YOUR_HEX_KEY>
# Example: python encryption_tool.py decrypt secret_doc.enc decrypted_doc.txt 0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
Learning Outcomes & Concepts Demonstrated
This project provides a comprehensive understanding and practical application of:

Symmetric-Key Cryptography: The principles of using the same key for both encryption and decryption.

AES-256 Algorithm: Hands-on implementation of a strong, modern block cipher.

Cipher Modes (CBC): Understanding how block ciphers are operated to encrypt larger amounts of data securely.
Initialization Vectors (IVs): The importance of unique IVs for semantic security and preventing pattern exposure.

Padding Schemes (PKCS7): How data is prepared for block cipher encryption.

Key Management: The critical aspects of generating, storing, and using cryptographic keys securely.

Binary File Handling: Reading and writing data in binary format.

Exception Handling: Building robust tools that can manage errors during cryptographic operations.

Cybersecurity Defense: Practical application of encryption as a fundamental data protection mechanism.

os Module: Used for generating cryptographically secure random bytes for keys (os.urandom()) and Initialization Vectors.

sys Module: For processing command-line arguments to control the tool's operations (generate key, encrypt, decrypt).

File I/O: Standard Python file operations (open with rb and wb modes) for reading and writing binary file content
