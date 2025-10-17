from company.employee import Employee

class Manager(Employee):
    def __init__(self, name, wage, managedUnit ):
        # LA PRIMA COSA CHE DEVO FARE PER
        # COSTRUIRE/INIZIALIZZARE UN Manager
        # E' COSTRUIRE/INIZIALIZZARE
        # LA "SUA PARTE" Employee
        # USANDO LA FUNZIONE super()
        super().__init__(name, wage)

        # POI POSSO ANDARE A DEFINIRE/INIZIALIZZARE
        # EVENTUALI ATTRIBUTI SPECIFICI DEL Manager
        self._managedUnit = managedUnit

    # ANCHE SE NON DEFINISCO DI NUOVO __str__() E __repr()___
    # QUESTE SONO EREDITATE DA Employee

    # SE SERVE POSSO ANCHE ANDARE A RIDEFINIRE DELLE FUNZIONI
    # IN MODO CHE SI COMPORTINO IN MODO DIVERSO, PIU' SPECIFICO
    # PER IL Manager

    def __str__(self):
        #return f"{self._name}, {self._wage}, {self._managedUnit}"
        # POTREI ANCHE DELEGARE ALL'Employee IL COMPITO DI STAMPARE
        # CIO' CHE LO RIGUARDA, ED IO AGGIUNGERE SOLO managedUNit
        return f"{super().__str__()}, {self._managedUnit}"

    # QUESTA E' UNA VERSIONE DEL METODO increment_wage() DEFINITO
    # NEL PADRE Employee (STESSO NOME) MA SPECIFICA PER IL Manager

    def increment_wage(self):
        self._wage += 20000 # INCREMENTO PER IL MANAGER
