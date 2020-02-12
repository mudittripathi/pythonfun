import random
characters = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
length = input('Enter Password lenght:')
length = int(length)
password = ''
for i in range (length):
    password += random.choice(characters)
print("Your Password is :" , password)
