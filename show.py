from termcolor import colored
from stegano import lsb
import cryptocode
import json
raw_data = lsb.reveal('encrypted.png')
data = json.loads(raw_data)
# print(data)
if data['encrypted']:
    print('Data Has Been Encrypted!')
    key = input('Please Enter Decryption Key... ')
    str_decoded = cryptocode.decrypt(data['text'], key)
    if not str_decoded:
        print(colored('Incorrect Decryption KEY!', 'red'))
    else:
        print(f"\nSecret Message: {str_decoded}")
else:
    print(f"\nSecret Message: {data['text']}")

