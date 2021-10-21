PRECIO_BASE = 100
CONSUMO_ENERGETICO = "F"
PESO = 5
COLOR = "BLANCO"


# No son necesarios los getters en las clases ya que al poner el nombre del objeto y el atributo deseado ya se llama ej:
# tele1.precio llamaria al valor que tenga el precio de tele1 siendo este un objeto de clase television


def comprobarConsumo(letra):
    if letra.upper() in ("A", "B", "C", "D", "E", "F"):
        return letra
    else:
        return CONSUMO_ENERGETICO


def comprobarColor(color):
    if color.lower() in ("blanco", "negro", "gris", "rojo", "azul"):
        return color
    else:
        return COLOR


class Electrodomestico:
    def __init__(self, precio=PRECIO_BASE, color=COLOR, consumo=CONSUMO_ENERGETICO, peso=PESO):
        self.precio = precio
        self.color = comprobarColor(color)
        self.consumo = comprobarConsumo(consumo)
        self.peso = peso

    def precioFinal(self):
        if self.consumo == 'A':
            self.precio = self.precio + 100
        elif self.consumo == 'B':
            self.precio = self.precio + 80
        elif self.consumo == 'C':
            self.precio = self.precio + 60
        elif self.consumo == 'D':
            self.precio = self.precio + 50
        elif self.consumo == 'E':
            self.precio = self.precio + 30
        else:
            self.precio = self.precio + 10

        if self.peso > 80:
            self.precio = self.precio + 100
        elif self.peso > 49:
            self.precio = self.precio + 80
        elif self.peso > 19:
            self.precio = self.precio + 50
        else:
            self.precio = self.precio + 10


# Clase Lavadora

CARGA = 5


class Lavadora(Electrodomestico):
    def __init__(self, carga=CARGA):
        super().__init__()
        self.carga = carga


# Clase Television

RESOLUCION = 20
FOURK = False


class Television(Electrodomestico):
    def __init__(self, peso, precio, resolucion=RESOLUCION, fourk=FOURK):
        super().__init__()
        self.peso = peso
        self.precio = precio
        self.resolucion = resolucion
        self.fourk = fourk

    def precioFinal(self):
        super().precioFinal()
        if self.resolucion > 40:
            self.precio = self.precio + (self.precio * 0.3)
        if self.fourk is True:
            self.precio = self.precio + 50


ele1 = Electrodomestico()
ele2 = Electrodomestico(50, "burdeos", "Z", 300)
ele3 = Electrodomestico(23, "azul", "C", 10)
ele4 = Electrodomestico(100, "GrIs", "F", 33)

lava1 = Lavadora(250)
lava2 = Lavadora()
lava3 = Lavadora(25)

tele1 = Television(20, 100)
tele2 = Television(50, 2000, 100, True)
tele3 = Television(100, 60, 45, False)

lista = [ele1, ele2, ele3, ele4, lava1, lava2, lava3, tele1, tele2, tele3]

p_ele = 0
p_tele = 0
p_lava = 0

for i in lista:
    i.precioFinal()
    if isinstance(i, Television):
        p_tele += i.precio
    elif isinstance(i, Lavadora):
        p_lava += i.precio
    else:
        p_ele += i.precio

print("Precios totales:")
print("Electrodomesticos: " + str(p_ele))
print("Lavadoras: " + str(p_lava))
print("Televisiones: " + str(p_tele))
