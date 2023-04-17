from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from task1 import add_padding

import binascii


def main():
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    iv = get_random_bytes(16)
    ciphertext = submit(cipher, iv)
    print(binascii.hexlify(ciphertext).decode('utf-8'))
    res = verify(key, iv, ciphertext)


def submit(cipher, iv):
    userdata = input("Enter data: ")
    formatted_userdata = userdata.replace(";", "%3B").replace("=", "%3D")
    submit_string = bytes("userid=456;userdata=" + formatted_userdata + ";session-id=31337", 'utf-8')
    print(binascii.hexlify(submit_string).decode('utf-8'))
    cipher_text = b''
    chain_iv = bytearray(iv)

    i = 0
    while i < len(submit_string):
        data = submit_string[i: min(i + 16, len(submit_string))]
        padded_data = bytearray(add_padding(data))
        result = bytearray()
        for j in range(len(padded_data)):
            result.append(padded_data[j] ^ chain_iv[j])
        chain_iv = cipher.encrypt(result)
        cipher_text += cipher.encrypt(result)
        i += 16
    return cipher_text


def verify(key, iv, ciphertext):
    decrypt_cipher = AES.new(key, mode=AES.MODE_CBC, iv=iv)
    plaintext = decrypt_cipher.decrypt(ciphertext)
    return b';admin=true' in plaintext


if __name__ == "__main__":
    main()
