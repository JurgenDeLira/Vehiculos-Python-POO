from VehiculoClass import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color ):
        super().__init__(marca,modelo)
        self.color = color
    def obtener_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"
 """       
coche = Coche("VW", "Vento", "Rojo")
print(coche.obtener_informacion())"""

