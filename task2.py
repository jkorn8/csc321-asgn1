from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from task1 import add_padding


def main():
    key = get_random_bytes(16)
    iv = get_random_bytes(128)
    ciphertext = submit(key, iv)
    print(ciphertext)


def submit(key, iv):
    userdata = input("Enter data: ")
    submitstring = bytes("userid=456;userdata=" + userdata + ";sessionid=31337", 'utf-8')

    cipher = AES.new(key, AES.MODE_ECB)
    cipher_text = b''
    chain_iv = bytearray(iv)

    i = 0
    while i < len(submitstring):
        j = min(i + 128, len(submitstring))
        data = submitstring[i: j]
        padded_data = add_padding(data)
        result = bytearray()
        for i in range(len(padded_data)):
            result.append(padded_data[i] ^ chain_iv[i])
        chain_iv = result
        cipher_text += cipher.encrypt(result)
        return cipher_text


def verify(key, iv):
    return False


if __name__ == "__main__":
    main()
