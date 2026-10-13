studente={"nome": "Pippo", "citta": "Ancona", "eta": 33}
studente["eta"] = 45
studente["email"] = "pippo@molto.it"

print(studente.keys())
print(studente.values())

for val in studente.keys():
    print(val + ":", studente[val])