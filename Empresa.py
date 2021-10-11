from Usuario import Usuario

class Empresa(Usuario):
    def __init__(self,banco,codigo,balance,nombre,correo,contrasena,tipo):
        
        super().__init__(banco,codigo,balance,nombre,correo,contrasena,tipo)

    def mostrar(self):
        return(f"Nombre: {self.nombre}\nTipo: {self.tipo}\ncodigo: {self.codigo}\nbalance {self.balance}\ncorreo {self.correo}\ncontrasena {self.contrasena}\nbanco {self.banco}")