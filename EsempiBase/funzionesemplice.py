def somma(x,y):
    print("sto sommando ", x, "a", y)
    s=x+y
    return s

def saluto_generale():
    print("Ciao a tutti!")

saluto_generale()
y=somma(2,3)
z=somma(y,9)
print(y,z)
saluto_generale()