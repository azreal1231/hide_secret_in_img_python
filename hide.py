from stegano import lsb
from termcolor import colored
import cryptocode

key = None


def test_if_file_exists(_file_name):
    import os
    ex = os.path.exists(_file_name)
    file = ''
    if ex:
        return _file_name
    while not ex:
        print(colored('\nCould Not Find File', 'red'))
        file = input('Please Re-Enter File Name: ')
        e = os.path.exists(file)
        if e:
            return file

    return file


def ask_for_encryption():
    awns = ['yes', 'no']
    awn = input('Would You Like To Encrypt Your Secret Text {YES/NO}: ')
    awn = awn.lower()
    valid_awn = True if awn in awns else False
    while not valid_awn:
        print(colored(f'{awn} is not a Valid Answer!\n', 'red'))
        awn = input('Would You Like To Encrypt Your Secret Text {YES/NO}: ')
        awn = awn.lower()
        valid_awn = True if awn in awns else False

    return awn


def get_encrypt_key():
    return input('Enter Encryption Key!: ')


def encrypt_text(_key, _text):
    str_encoded = cryptocode.encrypt(_text, _key)
    return str_encoded


def encrypt_img(_file, _encrypt, _text):
    try:
        secret = lsb.hide(_file, _text)
        new_file = f"encrypted.png"
        print('Encrypted File Name:  ' + new_file + '\n')
        secret.save(new_file)
        return colored(f'Successfully Encrypted Img With Secret Message.\n', 'green')
    except Exception as e:
        print(e)
        return colored(f'Failed To Encrypt Img With Secret Message!.\n', 'red')


file_to_embed_data_into = input('Please Enter File Name: ')
file_to_embed_data_into = test_if_file_exists(file_to_embed_data_into)
# print(file_to_embed_data_into)
# print(file_to_embed_data_into)
#
# print(os.path.exists(file_to_embed_data_into))

encrypt = ask_for_encryption()
if encrypt == 'yes':
    key = get_encrypt_key()

secret_text = input('Please Enter Secret Text.: ')

if encrypt == 'yes':
    secret_text = encrypt_text(key, secret_text)


result = encrypt_img(file_to_embed_data_into, encrypt, secret_text)
print(result)
