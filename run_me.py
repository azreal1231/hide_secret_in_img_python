try:
    from termcolor import colored
    from stegano import lsb
    import cryptocode
    import getpass
    import json
except Exception as e:
    print('Please install All required PIP Modules!')
    print(str(e))
    exit()


def check_if_file_exists(_file_name):
    import os
    ex = os.path.exists(_file_name)
    file = _file_name
    if ex:
        return _file_name
    while not ex:
        print(f"{colored('Warning', 'yellow')} Could Not Find File {colored(file, 'yellow')}")
        file = input('Please Re-Enter File Name: ')
        e = os.path.exists(file)
        if e:
            return file

    return file


def get_encrypt_key():
    return getpass.getpass('Enter Encryption Key... ')


def start():
    print(colored('Enter The One Following Options Continue', 'cyan'))
    print(f'Option {colored("1", "magenta")} hides a secret in an image.')
    print(f'Option {colored("2", "magenta")} gets a secret from and image.')

    option = input('... ')
    if option not in ['1', '2']:
        print(f' {colored(str(option), "red")} is not a valid option!')
        exit()

    if option == '1':
        hide()
    elif option == '2':
        show()
    else:
        raise Exception('Something Went Wrong...')


def hide():
    key = None

    def ask_for_encryption():
        awns = ['yes', 'no']
        awn = input(f'Would You Like To Encrypt Your Secret Text {colored("YES", "green")}/{colored("NO", "red")} ')
        awn = awn.lower()
        valid_awn = True if awn in awns else False
        while not valid_awn:
            print(colored(f'{awn} is not a Valid Answer!\n', 'red'))
            awn = input(f'Would You Like To Encrypt Your Secret Text '
                        f'{colored("YES", "green")}/{colored("NO", "red")} ')
            awn = awn.lower()
            valid_awn = True if awn in awns else False

        return awn

    def encrypt_text(_key, _text):
        str_encoded = cryptocode.encrypt(_text, _key)
        return str_encoded

    def encrypt_img(_file, _encrypt, _text):
        data = {
            'encrypted': True if _encrypt == 'yes' else False,
            'text': _text
        }
        json_data = json.dumps(data)
        try:
            secret = lsb.hide(_file, json_data)
            new_file = f"encrypted.png"
            print('Encrypted File Name:  ' + colored(new_file, 'cyan') + '\n')
            secret.save(new_file)
            print(f"{colored(f'Success', 'green')} Encrypted Img With Secret Message.\n")
        except Exception as e:
            print(f"{colored('Warning: ', 'yellow')} Failed To Encrypt Img With Secret Message!")
            print(f"{colored('Error: ', 'red')} {str(e)}")
            exit()

    file_to_embed_data_into = input('Please Enter Filename: ')
    file_to_embed_data_into = check_if_file_exists(file_to_embed_data_into)

    encrypt = ask_for_encryption()
    if encrypt == 'yes':
        key = get_encrypt_key()

    secret_text = input('Please Enter Secret Text... ')

    if encrypt == 'yes':
        secret_text = encrypt_text(key, secret_text)

    encrypt_img(file_to_embed_data_into, encrypt, secret_text)


def show():
    print(f"{colored('       SHOW IMAGE SECRET       ', 'green')}")

    raw_data = None
    file_name = input('Please Enter Filename: ')
    file_name = check_if_file_exists(file_name)
    try:
        raw_data = lsb.reveal(file_name)
    except Exception as e:
        print(f"Could Not Extract Secret From {colored(file_name, 'cyan')}")
        print(f"{colored('Error: ', 'red')} {str(e)}")
        exit()

    data = json.loads(raw_data)
    if data['encrypted']:
        print('Data Has Been Encrypted!')
        key = get_encrypt_key()
        str_decoded = cryptocode.decrypt(data['text'], key)
        if not str_decoded:
            print(f"{colored('Warning', 'yellow')} Incorrect Decryption KEY!")
        else:
            print(f"\n{colored('Secret Message: ', 'cyan')} {str_decoded}")
    else:
        print(f"\n{colored('Secret Message: ', 'cyan')} {data['text']}")


if __name__ == '__main__':
    print(colored('\n===================================\n'
                  '       Welcome To Secret Img     \n'
                  '===================================\n', 'green'))
    start()
