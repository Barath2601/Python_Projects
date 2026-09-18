# This is a Python script to encrypt and decrypt password.

password = input('Enter your password: ')
ls = list(password)
key = 259874
sec = []
encrypt = []
string = ''

#encryption
for i in range (0,len(ls)):
    sec.append(ord(ls[i]))
    encrypt.append(sec[i]^key)
    string += chr(encrypt[i])
print(sec)
print(encrypt)
print('The encrypted value of password is: ', string)

#decryption
decrypt = []
val = []
pwd = ''
ans = input('Do you want to decrypt [y/n]: ')
if ans == 'y':
    for i in range(0,len(string)):
        decrypt.append(string[i])
        val.append(ord(decrypt[i])^key)
        pwd += chr(val[i])
    print(decrypt)
    print(val)
    print('The decrypted password is: ', pwd)
else:
    print('The operation cannot be performed')


