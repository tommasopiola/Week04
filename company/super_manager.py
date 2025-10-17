from company.manager import Manager

class SuperManager(Manager):
    def __init__(self, name, wage, managedUnit):
        # SISTEMARE IL COSTRUTTORE
        super().__init__(name, wage, managedUnit)