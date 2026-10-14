def saluta(nome="", cognome=""):
    nominativo = nome + " " + cognome
    nom = nominativo.strip()
    if not nom:
        nom = input("Come ti chiami? ")
    print("Ciao, " + nom + ". Come va?")

#saluta()
#saluta("Paolo")
#saluta(cognome="Fucci", nome="Simona")
#saluta(cognome="Fucci")

