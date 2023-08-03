import secrets
from random import *
import string
all_chars = list(string.ascii_letters + string.digits + string.punctuation)
shuffle(all_chars)
all_chars = ''.join(all_chars)
def generate_password(length):
	password = ''.join([secrets.choice(all_chars) for i in range(length)])
	return password

while True:
	try:
		num = int(input("Enter len of password: "))
		if num < 8:
			print("Password length must be greater than 8!!!")
			continue
		else:
			break
	except:
		print("Oops..., wrong input!")
password = generate_password(num)
print(password)
