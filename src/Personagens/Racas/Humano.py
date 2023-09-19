from AbstractRaca import Abstract_Raca

   
class Humano(Abstract_Raca):
    
    def __init__(self):
        self.nome = "Humano"

humano = Humano()
humano.nome