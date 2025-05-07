import Pyro5.api
from service_dc2 import StringService

def main():
	daemon = Pyro5.api.Daemon()
	ns = Pyro5.api.locate_ns()
	uri = daemon.register(StringService)
	ns.register("example.stringconcate", uri)
	print("Server is running...")
	daemon.requestLoop()

if __name__ == "__main__":
	main()