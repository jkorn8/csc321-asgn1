from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from task1 import add_padding


def main():
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    iv = get_random_bytes(16)
    user_plaintext = "hello:admin<true"
    ciphertext = submit(user_plaintext, cipher, iv)
    if verify(key, iv, attack(ciphertext)):
        print("Admin access granted.")
    else:
        print("Welcome user 456.")


def submit(plaintext, cipher, iv):
    formatted_plaintext = plaintext.replace(";", "%3B").replace("=", "%3D")
    submit_string = bytes("userid=456;userdata=" + formatted_plaintext + ";session-id=31337", 'utf-8')
    print(f'Input string: {submit_string}')
    cipher_text = b''
    chain_iv = bytearray(iv)

    i = 0
    while i < len(submit_string):
        data = submit_string[i: min(i+16, len(submit_string))]
        padded_data = bytearray(add_padding(data))
        result = bytearray()
        for j in range(len(padded_data)):
            result.append(padded_data[j] ^ chain_iv[j])
        chain_iv = cipher.encrypt(result)
        cipher_text += cipher.encrypt(result)
        i += 16
    return cipher_text


def remove_padding(padded_string):
    last_bit = padded_string[-1]
    referenced_bit = padded_string[-last_bit] if last_bit < len(padded_string) else None
    if last_bit == referenced_bit:
        return padded_string[:-last_bit]
    return padded_string


def verify(key, iv, ciphertext):
    decrypt_cipher = AES.new(key, mode=AES.MODE_CBC, iv=iv)
    plaintext = remove_padding(decrypt_cipher.decrypt(ciphertext))
    print(f'Attacked string: {plaintext}')
    return b';admin=true' in plaintext


def attack(ciphertext):
    ba_ciphertext = bytearray(ciphertext)
    ba_ciphertext[9] = ba_ciphertext[9] ^ ord(":") ^ ord(";")
    ba_ciphertext[15] = ba_ciphertext[15] ^ ord("<") ^ ord("=")
    return bytes(ba_ciphertext)


if __name__ == "__main__":
    main()