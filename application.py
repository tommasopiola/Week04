from company.employee import Employee
from company.super_manager import SuperManager

import flet

from miaclasse import MiaClasse

print(55)
print("abc")
print(True)
l = [10, 46, 78]
print(l)
e = Employee("John", 120000)
print(e)

# TUTTI QUESTE VARIABILI POSSONO ESSERE STAMPATE
# IN QUANTO PER OGNUNA E' RESA DISPONIBILE, DAGLI
# SVILUPPATORI DI PYTHON O DAL PROGRAMMATORE, UNA
# VERSIONE DEL METODO __str()__

# E SE QUESTO METODO NON E' STATO (ANCORA) SPECIFICATO
# PER UN DETERMINATO OGGETTO (UNA DETERMINATA) CLASSE,
# ALLORA VERRA INVOCATO IL METODO DI BASE, DEFINITO IN
# Object, CHE STAMPA IL RIFERIMENTO (INDIRIZZO DI MEM.)

s = SuperManager("Super Manager", 12000000, "All")
print(s)

# POSSO INSERIRE IN UN CONTENITORE, ES. UNA LISTA,
# OGGETTI DI TIPO DIVERSO (GIA' VISTO)

lista = [55, "abc", True, l, e, s]

# E SE TUTTI IMPLEMENTANO UN DETERMINATO "PROTOCOLLO",
# ES. SANNO DESCRIVERSI COME STRINGHE OFFRENDO / IMPLEMENTANDO
# IL METODO PER FARLO, OVVERO __str()__, ALLORA NON SOLO
# POTRO' SCRIVERE QUANTO SOTTO, MA QUANTO SOTTO STAMPERA'
# TUTTI GLI OGGETTI

for oggetto in lista:
    print(oggetto)


# USO DELLA CLASSE MiaClasse CREATA CON IL DECORATORE @dataclass

mia1 = MiaClasse(100, "Ciao") # DUE PARAMETRI
mia2 = MiaClasse(50, "Hello")
lista = []
lista.append(mia1)
lista.append(mia2)

print("\nLista di oggetti MiaClasse prima dell'ordinamento")
for o in lista:
    print(o) # STAMPABILE, GRAZIE AL METODO __repr__() DEFINITO DAL DECORATORE

sorted(lista) # ORDINABILE USANDO I METODI DI CONFRONTO DEFINITI DA @dataclass

print("\nLista di oggetti MiaClasse prima dell'ordinamento")
for o in lista:
    print(o)




