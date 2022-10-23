from encryptor import *
from dotenv import dotenv_values

config = dotenv_values(".secret")

with open('.secret', 'r') as f:
    data = f.read()


def decrypt_env():
    pwd = config["SECRET_KEY"]
    return my_decrypt(my_encrypt(data, pwd), pwd)


def add_env_file():
    with open('.env', 'w') as f:
        f.write(decrypt_env())
