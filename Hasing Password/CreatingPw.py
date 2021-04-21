#pip install bcrypt

import bcrypt

password = b'tanya2001$'
hashed = bcrypt.hashpw(password,bcrypt.gensalt())
print(hashed)

input_password = input('Enter Password')
input_password = bytes(input_password,encoding = 'utf-8')        # or write simply 'utf-8'


if bcrypt.checkpw(input_password, hashed):
    print('Login successful')
else:
    print("Invalid Password")