from Usuario import Usuario

class Persona(Usuario):
    def __init__(self,banco,codigo,balance,nombre,correo,contrasena,tipo,fecha,sexo):
        self.fecha = fecha
        self.sexo = sexo
        super().__init__(banco,codigo,balance,nombre,correo,contrasena,tipo)

    def mostrar(self):
        return(f"Nombre: {self.nombre}\nTipo: {self.tipo}\ncodigo: {self.codigo}\nbalance {self.balance}\ncorreo {self.correo}\ncontrasena {self.contrasena}\nbanco {self.banco}\nfecha {self.fecha}\nsexo{self.sexo}")