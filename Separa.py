class Separa:
    def __init__(self,name,spent,has_to_recieve,split):

        self.name = name
        self.spent = spent
        self.has_to_recieve = has_to_recieve
        self.split = split


    def mostrar(self):
        return(f"Nombre: {self.name}\nspent: {self.spent}\ntiene que recibit: {self.has_to_recieve}\naplit {self.split}")