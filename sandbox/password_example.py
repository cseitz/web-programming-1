import hashlib
import codecs 
import os
import random

passwords = {
}

def bytes_to_str(b):
    s = str(codecs.encode(b,"hex"),"utf-8")
    assert type(s) is str
    return s

def str_to_bytes(s):
    b = codecs.decode(bytes(s,"utf-8"),"hex")
    assert type(b) is bytes
    return b

def generate_credentials(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac("sha256", password.encode('utf-8'),salt,100000)
    return {
        'key': key,
        'salt': key
    }

def save_password(username, password):
    global passwords
    print(f"saving {username}/{password}")
    passwords[username] = password[::-1]
    credentials = generate_credentials(password)
    print(credentials)

def verify_password(username, password):
    global passwords
    print(f"verifying {username}/{password}")
    if username not in passwords:
        return False
    return passwords[username] == password[::-1]

if __name__ == '__main__':
    # signup 
    save_password("santa", "elephant")
    save_password("greg", "dorothy")
    # accidental disclosure
    print(passwords)
    # login
    if verify_password("santa","elephant"):
        print("login allowed")
    else:
        print("login denied")
    if verify_password("rudolph","elephant"):
        print("login allowed")
    else:
        print("login denied")
    if verify_password("santa","crocodile"):
        print("login allowed")
    else:
        print("login denied")
    if verify_password("greg","dorothy"):
        print("login allowed")
    else:
        print("login denied")
