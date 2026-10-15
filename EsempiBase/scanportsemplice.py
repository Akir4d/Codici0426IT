import socket

# qui chiedo l'ip
target = input("Dammi indirizzo da scansire: ")
portra = input("Dammi le porte da scansire (es 5-200): ")

# mi ricavo le porte dalla risposta utente
lowport, highport = portra.split('-')
#print ("Sto scansendo " +  target + " dalla porta " + lowport + " alla porta " + highport)
print(f"Sto scansendo {target} dalla porta {lowport} alla porta {highport}")
fallite = []
for port in range(int(lowport), int(highport)+1):
    # configuriamo connessione ipv4 tcp
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # usiamo connessione di esempio
    status = s.connect_ex((target, port))
    if status == 0:
        print(f"Connessione alla porta {port} ha avuto successo")
    else:
        fallite.append(port)
    s.close()
if input("vuoi vedere le fallite? (s/n): ").lower().strip().startswith("s"):
    print("fallite: ", fallite)