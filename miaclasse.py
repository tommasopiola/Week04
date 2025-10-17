from dataclasses import dataclass

# Anziché definire il metodo __init_() ed
# altri metodi dunder per la classe, sfrutto
# il decoratore @dataclass

# Con questa configurazione, definisce due attributi,
# crea un costruttore per inizializzarli, e definisce
# metodi per confronto ed ordinamento sui parametri;
# non serve quindi che sia io a definire __eq__() e __lt__()

@dataclass(eq=True, order=True)
class MiaClasse:
    attributo1 : int
    attributo2 : str




