import Pyro5.api
@Pyro5.api.expose

class StringService:
	def concate (self,strA,strB):
		print (f"Return : {strA} and {strB}.")
		return strA+ " " + strB

# python -m Pyro5.nameserver
