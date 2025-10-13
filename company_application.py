from employee import Employee
from manager import Manager

e1 = Employee("M. Rossi", 20000)

m = Manager("B. Boss", 50000,
             "Marketing")

print(m)

e2 = Employee("A. Arancioni", 3000)

employees = [e1, e2, m]

for emp in employees:
    emp.increment_wage() # PRIMA INCREMENTO LA PAGA
                         # PYTHON GUARDA DI CHE TIPO
                         # E' L'OGGETTO E CHIAMA LA VERSIONE
                         # DEL METODO PIU' SPECIFICO DISPONIBILE
                         # (POLIMORFISMO)
    #print(emp.__class__.__name__)
    print(emp) # POI STAMPO, POSSO USARE isinstance() PER VERIFICARE IL TIPO

eA = Employee("G. Verdi", 20000)
eB = Employee("G. Verdi", 35000)

# COSI' COME QUANDO STAMPO, VIENE VERIFICATA LA PRESENZA DEL
# METODO __str()__, QUANDO CONFRONTO VIENE VERIFICATA LA PRESENZA
# DEL METODO __eq()__ NEGLI OGGETTI (ALTRIMENTI USATA LA VERSIONE
# DI BASE DEFINITA IN Object (CHE CONFRONTA I RIFERIMENTI)

if eA == eB:
    print("Sono uguali")
else:
    print("Sono diversi")
