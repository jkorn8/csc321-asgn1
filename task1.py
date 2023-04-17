from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def ecb(filename, cipher):
    cipher_text = b''
    with open(filename, 'rb') as file:
        header = file.read(54)
        while True:
            data = file.read(128)
            if not data:
                break
            padded_data = add_padding(data)
            cipher_text += cipher.encrypt(padded_data)
    with open(filename[:-4] + "_encrypted" + filename[-4:], 'wb') as file_writer:
        file_writer.write(header)
        file_writer.write(cipher_text)


def cbc(filename, cipher, iv):
    cipher_text = b''
    chain_iv = bytearray(iv)
    with open(filename, 'rb') as file:
        header = file.read(54)
        while True:
            data = file.read(128)
            padded_data = bytearray(add_padding(data))
            if not data:
                break
            result = bytearray()
            for i in range(len(padded_data)):
                result.append(padded_data[i] ^ chain_iv[i])
            chain_iv = result
            cipher_text += cipher.encrypt(result)
    with open(filename[:-4] + "_encrypted_cbc" + filename[-4:], 'wb') as file_writer:
        file_writer.write(header)
        file_writer.write(cipher_text)


def add_padding(data):
    missing_len = 128 - len(data)
    data = data + bytes(missing_len * chr(missing_len), 'utf-8')
    return data


if __name__ == "__main__":
    key = get_random_bytes(16)
    my_cipher = AES.new(key, AES.MODE_ECB)
    my_iv = get_random_bytes(128)
    ecb("mustang.bmp", my_cipher)
    cbc("mustang.bmp", my_cipher, my_iv)
