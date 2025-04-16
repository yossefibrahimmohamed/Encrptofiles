from Crypto.Cipher import AES
from Crypto.Util import Counter
from os import path

def decrypt(key, input_path):
    output_path = input_path.replace(".enc", "")  # remove .enc

    with open(input_path, 'rb') as fin, open(output_path, 'wb') as fout:
        nonce = fin.read(8)
        counter = Counter.new(64, prefix=nonce)
        cipher = AES.new(key, AES.MODE_CTR, counter=counter)

        while chunk := fin.read(1024):
            decrypted_chunk = cipher.decrypt(chunk)
            fout.write(decrypted_chunk)

    print(f"✅ Decrypted successfully to: {output_path}")

def get_valid_key():
    key_input = input("Enter your AES key (must match the encryption key): ")
    key_bytes = key_input.encode()

    if len(key_bytes) not in [16, 24, 32]:
        print(f"❌ Invalid key length: {len(key_bytes)}. Must be 16, 24, or 32 bytes.")
        exit(1)
    return key_bytes

# === MAIN ===
key = get_valid_key()
input_file = input("Enter your path : ")

if not path.exists(input_file):
    print("❌ File not found!")
else:
    decrypt(key, input_file)
