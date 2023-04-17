from time import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes


def main():
    # NEVER MIND I WASTED A BUNCH OF TIME, USE OPENSSL
    aes_start = time()
    aes("hello world")
    aes_end = time()
    rsa_start = time()
    rsa("hello world")
    rsa_end = time()
    print(f'AES total time: {aes_end - aes_start}\nRSA total time: {rsa_end - rsa_start}')


def rsa(plain_text):
    key = RSA.generate(2048)
    public_key = key.publickey().export_key().decode()
    private_key = key.export_key().decode()
    print("Public key:\n", public_key)
    print("Private key:\n", private_key)
    # PKCS1_OAEP is a padding method that adds randomness to strings. Ask the hart man what he wants
    cipher_rsa = PKCS1_OAEP.new(key)
    ct = cipher_rsa.encrypt(plain_text.encode('utf-8'))
    print(ct.hex())
    print(cipher_rsa.decrypt(ct).decode('utf-8'))
    # this is working, just have to add a parameter for the key size
    return ct


def aes(plain_text):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    # cipher_text = cipher.encrypt(plain_text)


if __name__ == "__main__":
    main()
