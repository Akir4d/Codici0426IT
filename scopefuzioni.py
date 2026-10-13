variabile_globale=20

def stampa():
    #global variabile_globale
    variabile_locale = variabile_globale + 10
    print(variabile_locale)

def stampa_due():
    print(variabile_globale)

stampa()
stampa_due()
# no puoi accedere qui a varibile_locale
# print(variabile_locale) # se decommenti otterrai errore