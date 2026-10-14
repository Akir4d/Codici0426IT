variabile_globale=20

def stampa():
    global variabile_globale
    variabile_globale = 10
    print(variabile_globale)

def stampa_due():
    print(variabile_globale)

stampa()
stampa_due()