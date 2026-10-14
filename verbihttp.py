import http.client

host = input("inserire host oppure ip: ")
link = input("inserire link es: /dav/ (default: /)")
port = input("inserire porta http (default: 80): ")

if not link: link = "/"

if port == "":
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('OPTIONS', link)
    response = connection.getresponse()
    verbs =response.getheader('Allow')
    if verbs:
        print(verbs)
    else:
        print("Non ho trovato verbi prova con un altro link")
except ConnectionRefusedError:
    print("Connessione rifiutata")
