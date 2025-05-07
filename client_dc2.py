import Pyro5.api

def main():
	uri = Pyro5.api.locate_ns().lookup("example.stringconcate")
	stringservice = Pyro5.api.Proxy(uri)
	strA = input("Enter string 1: ")
	strB = input("Enter string 2: ")
	result = stringservice.concate(strA, strB)
	print("Concate: ", result)
	
if __name__ == "__main__":
	main()