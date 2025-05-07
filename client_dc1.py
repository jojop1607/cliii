import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
num = int(input("Enter the number:"))
result = proxy.factorial(num)
print("Factorial: ", result)
