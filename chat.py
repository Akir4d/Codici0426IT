import socket

# queste variabili mi servono per la tupla dell'oggetto s
SRV_ADDR = "0.0.0.0"
SRV_PORT = 44444

# crea oggetto connessione ipv4 (AF_NET) in tcp (SOCK_STREAM) [SOCK_DGRAM = udp]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Quando ti avvierai devi chidere al sistema operattivo di occupare l'ip SRV_ADDR e la porta SRV_PORT 
s.bind((SRV_ADDR, SRV_PORT))
# Quando ti avvierai dei metterti in ascolto e accettare 1 connessione
s.listen(1)
# Prima di avviare avvertiamo l'utente
print("Sono in attesa di connessione")
# A questo punto mi metto in attesa
# acc = s.accept() # metodono senza destrutturazione
# connection = acc[0]
# address = acc[1]
connection, address = s.accept()
# avverto l'utente della connessione avvenuta
print("Connesso con:", address)
# avvio in ciclo infinto per gestire la connessione
while True:
    risposta = "\n Tu: "
    connection.sendall(risposta.encode())
    # accetta massimo 1024 byte (ottetti) per volta a meno che non prema invio
    data = connection.recv(1024)
    # se la connessione crolla esci
    if not data: break
    # stampa quello che ti ricevi convertendolo da byte a caratteri
    print(data.decode('utf-8').strip())
    risposta = input("Risposta: ")
    risposta += "\n Tu: "
    connection.sendall(risposta.encode())
# Attenzione questo non e' while
# chiudi la connessione uscito dal ciclo infinito
connection.close()

