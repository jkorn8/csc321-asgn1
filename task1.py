from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def main(filename):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
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


def add_padding(data):
    missing_len = 128 - len(data)
    data = data + bytes(missing_len * chr(missing_len), 'utf-8')
    return data


if __name__ == "__main__":
    main("mustang.bmp")
