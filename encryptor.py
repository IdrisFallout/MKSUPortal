import json
import binascii
from Crypto.Cipher import AES
from Crypto import Random
import base64
from dotenv import dotenv_values

config = dotenv_values(".env")


def my_encrypt(data, passphrase):
    """
         Encrypt using AES-256-CBC with random/shared iv
        'passphrase' must be in hex, generate with 'openssl rand -hex 32'
    """
    try:
        key = binascii.unhexlify(passphrase)
        pad = lambda s: s + chr(16 - len(s) % 16) * (16 - len(s) % 16)
        iv = Random.get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted_64 = base64.b64encode(cipher.encrypt(pad(data).encode())).decode('ascii')
        iv_64 = base64.b64encode(iv).decode('ascii')
        json_data = {}
        json_data['iv'] = iv_64
        json_data['data'] = encrypted_64
        clean = base64.b64encode(json.dumps(json_data).encode('ascii'))
    except Exception as e:
        print("Cannot encrypt datas...")
        print(e)
        exit(1)
    return clean


def my_decrypt(data, passphrase):
    """
         Decrypt using AES-256-CBC with iv
        'passphrase' must be in hex, generate with 'openssl rand -hex 32'
        # https://stackoverflow.com/a/54166852/11061370
    """
    try:
        unpad = lambda s: s[:-s[-1]]
        key = binascii.unhexlify(passphrase)
        encrypted = json.loads(base64.b64decode(data).decode('ascii'))
        encrypted_data = base64.b64decode(encrypted['data'])
        iv = base64.b64decode(encrypted['iv'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(encrypted_data)
        clean = unpad(decrypted).decode('ascii').rstrip()
    except Exception as e:
        print("Cannot decrypt datas...")
        print(e)
        exit(1)
    return clean