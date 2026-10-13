studente={"nome": "Pippo", "citta": "Ancona", "eta": 33}
print(studente["nome"])
print(studente["eta"])
studente["eta"] = 45
studente["email"] = "pippo@molto.it"
print(studente)
studente.pop("citta")
print(studente)
del studente["email"]
print(studente)