import source
import hashlib, os, sys


class Sys_tm:
	
	def __init__(self, menu):
		self.menu = menu
		
									
	def clear(self):
	  if os.name.__eq__("posix"):
	    os.system("clear")
	  else:
	  	os.system("cls")
	

class Data:
	
	def sha256(self):
		message = input("Input Pesan : ").encode()
		return f"\nSHA-256 : {hashlib.sha256(message).hexdigest()}"

		
	def sha384(self):
		message = input("Input Pesan : ").encode()
		return f"\nSHA-384 : {hashlib.sha384(message).hexdigest()}"
		
		
	def sha512(self):
		message = input("Input Pesan : ").encode()
		return f"\nSHA-512 : {hashlib.sha512(message).hexdigest()}"
		
		
	def sha3_256(self) -> str:
		message = input("Input Pesan : ").encode()
		print(f"\nSHA3-256 : {hashlib.sha3_256(message).hexdigest()}")
		
		
	def sha3_384(self):
		message = input("Input Pesan : ").encode()
		return f"\nSHA3-384 : {hashlib.sha3_384(message).hexdigest()}"
		
		
	def sha3_512(self) -> str:
		message = input("Input Pesan : ").encode()
		print(f"\nSHA3-512 : {hashlib.sha3_512(message).hexdigest()}")
		
		
	def blake2s(self):
		message = input("Input Pesan : ").encode()
		return f"\nBlake2s : {hashlib.blake2s(message).hexdigest()}"
		
	
	def blake2b(self):
		message = input("Input Pesan : ").encode()
		return f"\nBlake2b : {hashlib.blake2b(message).hexdigest()}"
	
	
	def md5(self):
		message = input("Input Pesan : ").encode()
		return f"\nMD5 : {hashlib.md5(message).hexdigest()}"
	
		
def main():
	s = Sys_tm(source.Menu())
	secret = Data()
	try:
		c = int(input("Pilih Menu : "))
		if c == 1:
			s.clear()
			print(secret.sha256())
		elif c == 2:
			s.clear()
			print(secret.sha384())
		elif c == 3:
			s.clear()
			print(secret.sha512())
		elif c == 4:
			s.clear()
			secret.sha3_256()
		elif c == 5:
			s.clear()
			print(secret.sha384())
		elif c == 6:
			s.clear()
			secret.sha3_512()
		elif c == 7:
			s.clear()
			print(secret.blake2s())
		elif c == 8:
			s.clear()
			print(secret.blake2b())
		elif c == 9:
			s.clear()
			print(secret.md5())
		elif c == 0:
			sys.exit(0)
		else:
			print("\nInput Angka 1-9")
	except ValueError as err:
		print("\n" + str(err))
		
	
if __name__ == "__main__" :
	main()	