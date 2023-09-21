from source import Menu
import hashlib, os


class SystemSet:
	
	def __init__(self, menu) -> None:
		self.menu = menu
											
	def clear(self):
	  if os.name == "posix":
	  	os.system("clear")
	  else:
	  	os.system("cls")
	

class GetHash:
	
	def sha256(self):
		message = input("Input Pesan : ").encode()
		return f"\nSHA-256 : {hashlib.sha256(message).hexdigest()}"
		
	def sha384(self):
		message = input("Input Pesan : ").encode()
		return f"\nSHA-384 : {hashlib.sha384(message).hexdigest()}"		
		
	def sha512(self):
		message = input("Input Pesan : ").encode()
		return f"\nSHA-512 : {hashlib.sha512(message).hexdigest()}"		
		
	def sha3_256(self):
		message = input("Input Pesan : ").encode()
		return f"\nSHA3-256 : {hashlib.sha3_256(message).hexdigest()}"
				
	def sha3_384(self):
		message = input("Input Pesan : ").encode()
		return f"\nSHA3-384 : {hashlib.sha3_384(message).hexdigest()}"
				
	def sha3_512(self):
		message = input("Input Pesan : ").encode()
		return f"\nSHA3-512 : {hashlib.sha3_512(message).hexdigest()}"		
		
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
	system = SystemSet(Menu())
	secret = GetHash()
	algorithms = {
        1 : secret.sha256,
        2 : secret.sha384,
        3 : secret.sha512,
        4 : secret.sha3_256,
        5 : secret.sha3_384,
        6 : secret.sha3_512,
        7 : secret.blake2s,
        8 : secret.blake2b,
        9 : secret.md5
    }
    
	try:
		choice = int(input("[+] Pilih Menu : "))
		if choice in algorithms:
			system.clear()
			print(algorithms[choice]())
		elif choice == 0:
			exit(0)
		else:
			print("\nInput Angka 0-9")
	except ValueError as err:
		print("\n" + str(err))		

		
if __name__ == "__main__" :
	main()
