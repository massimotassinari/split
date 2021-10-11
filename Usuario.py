class Usuario:
    def __init__(self,banco,codigo,balance,nombre,correo,contrasena,tipo):

        self.banco = banco
        self.codigo = codigo
        self.balance = balance
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.tipo = tipo

    def mostrar(self):
        return(f"Nombre: {self.nombre}\nTipo: {self.tipo}\ncodigo: {self.codigo}\nbalance {self.balance}\ncorreo {self.correo}\ncontrasena {self.contrasena}\nbanco {self.banco}")