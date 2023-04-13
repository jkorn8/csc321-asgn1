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
            cipher_text += cipher.encrypt(data)
    with open(filename[:-4] + "_encrypted" + filename[-4:], 'wb') as file_writer:
        file_writer.write(header)
        file_writer.write(cipher_text)


if __name__ == "__main__":
    main("mustang.bmp")
