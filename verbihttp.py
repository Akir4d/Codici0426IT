import http.client

host = input("inserire host oppure ip: ")
port = input("inserire porta http (default: 80): ")

if port == "":
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS','/')
    response = connection.getresponse()
    print(response.getheaders())
except ConnectionRefusedError:
    print("Connessione rifiutata")
