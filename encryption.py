from Crypto.Cipher import AES
from Crypto.Util import Counter
from os import path

def encrypt(key, input_path):
    output_path = input_path + ".enc"

    with open(input_path, 'rb') as fin, open(output_path, 'wb') as fout:
        nonce = os.urandom(8)  # Generate a random nonce (8 bytes)
        fout.write(nonce)  # Write the nonce at the beginning of the file

        counter = Counter.new(64, prefix=nonce)
        cipher = AES.new(key, AES.MODE_CTR, counter=counter)

        while chunk := fin.read(1024):
            encrypted_chunk = cipher.encrypt(chunk)
            fout.write(encrypted_chunk)

    print(f"✅ Encrypted successfully to: {output_path}")

def get_valid_key():
    key_input = input("Enter your AES key (16, 24, or 32 chars): ")
    key_bytes = key_input.encode()

    if len(key_bytes) not in [16, 24, 32]:
        print(f"❌ Invalid key length: {len(key_bytes)}. Must be 16, 24, or 32 bytes.")
        exit(1)
    return key_bytes

# === MAIN ===
import os

key = get_valid_key()
input_file = input("Enter path file :")

if not path.exists(input_file):
    print("❌ Path not found!")
else:
    encrypt(key, input_file)
