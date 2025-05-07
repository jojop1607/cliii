from xmlrpc.server import SimpleXMLRPCServer

def factorial(n):
 result = 1
 if n == 0:
  return 1
 for i in range(2, n+1):
  result*= i
 return result
    
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server 8000 running ...")
server.register_function(factorial,"factorial")
server.serve_forever()