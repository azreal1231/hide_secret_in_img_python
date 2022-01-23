import cryptocode

KEY = 'HALO is cool'
text = 'master chief is DEAD!'

str_encoded = cryptocode.encrypt(text, KEY)
str_decoded = cryptocode.decrypt(str_encoded, KEY)
print(str_encoded)
print(str_decoded)