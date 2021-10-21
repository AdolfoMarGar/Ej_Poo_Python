import random


# en este ejercicio si he creado getters debido a que he puesto los atributos privados y al ser privados no se pueden
# llamar con objeto.atributo
class Persona:
    def __init__(self, nombre="", apellido="", edad=0, sexo='M', peso=0.00, altura=0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__dni = generarDNI()

    def set_nombre(self, nom):
        if nom != "" and nom.isalpha():
            self.__nombre = nom
        else:
            print("Error.")
            print("Introduce el nombre de la persona:")
            self.set_nombre(input())

    def set_apellido(self, ape):
        if ape != "" and ape.isalpha():
            self.__apellido = ape
        else:
            print("Error.")
            print("Introduce el apellido de la persona:")
            self.set_apellido(input())

    def set_edad(self, ano):
        if ano.isnumeric() and int(ano) > 0:
            self.__edad = int(ano)
        else:
            print("Error.")
            print("Introduce la edad:")
            self.set_edad(input())

    def introducirSexo(self, sex):
        sex = sex.upper()
        if sex == 'H' or sex == 'M':
            self.__sexo = sex
        else:
            self.__sexo = "M"

    def set_peso(self, pes):
        if pes.isalpha() is False:
            if pes != "":
                pes = float(pes)
                if 0 < pes < 250:
                    self.__peso = pes
                else:
                    print("Error.")
                    print("Introduce el peso entre 0 y 250: ")
                    self.set_peso(input())
            else:
                print("Error.")
                print("Introduce el peso: ")
                self.set_peso(input())
        else:
            print("Error.")
            print("Introduce el peso: ")
            self.set_peso(input())

    def set_altura(self, alt):
        if alt.isalpha() is False:
            if alt != "":
                alt = int(alt)
                if 0 < alt < 250:
                    self.__altura = alt
                else:
                    print("Error.")
                    print("Introduce la altura entre 0 y 250(cm): ")
                    self.set_altura(input())
            else:
                print("Error.")
                print("Introduce la altura(cm): ")
                self.set_altura(input())
        else:
            print("Error.")
            print("Introduce la altura(cm): ")
            self.set_altura(input())

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_edad(self):
        return self.__edad

    def get_sexo(self):
        return self.__sexo

    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura

    def get_dni(self):
        return self.__dni

    def __str__(self):
        return str(
            "Esta persona se llama " + self.__nombre + " " + self.__apellido + "." + "Su DNI es " + self.__dni
            + " y su genero es " + self.__sexo + " (H de hombre y M de mujer)." + "Tiene " + repr(self.__edad)
            + " años con una altura de " + repr(self.__altura) + " y un peso de " + repr(self.__peso) + ".")


def generarDNI():
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    aux = random.randint(11111111, 99999999)
    dni = str(aux) + random.choice(letras)
    return dni


def esMayorDeEdad(anos):
    if anos >= 18:

        return True
    else:
        return False


def calcularIMC(peso, altura):
    if altura != 0:
        # Esta multiplicado por 10000 pq le introduzco cm en vez de m y hay que pasar de cm2 a m2
        imc = (peso / (altura * altura)) * 10000
        if imc > 30:
            print("Peso: Obesidad.")
        else:
            if imc > 24.9:
                print("Peso: Sobrepeso.")
            else:
                if imc > 18.4:
                    print("Peso: Normal.")
                else:
                    print("Peso: Bajopeso.")
        return str(imc)
    else:
        imc = "Error. Altura=0 Indivisible"
        return imc


persona1 = Persona()
print("Introduce el nombre de la persona:")
persona1.set_nombre(input())
print("Introduce el primer apellido de la persona:")
persona1.set_apellido(input())
print("Introduce el edad de la persona:")
persona1.set_edad(input())
print("Introduce el sexo de la persona:")
persona1.introducirSexo(input())
print("Introduce la altura(cm) de la persona:")
persona1.set_altura(input())
print("Introduce el peso de la persona:")
persona1.set_peso(input())

persona2 = Persona()
persona2.set_nombre(persona1.get_nombre())
persona2.set_apellido(persona1.get_apellido())
persona2.set_edad(str(persona1.get_edad()))
persona2.introducirSexo(persona1.get_sexo())

persona3 = Persona()
persona3.set_nombre("Pepe")
persona3.set_apellido("Viñuela")
persona3.set_edad("53")
persona3.introducirSexo('H')
persona3.set_altura("173")
persona3.set_peso("90")

print(str(persona1))
print("Tiene un IMC de : " + calcularIMC(persona1.get_peso(), persona1.get_altura()))
if esMayorDeEdad(persona1.get_edad()) is True:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

print()
print()
print()

print(str(persona2))
print("Tiene un IMC de : " + calcularIMC(persona2.get_peso(), persona2.get_altura()))
if esMayorDeEdad(persona2.get_edad()) is True:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

print()
print()
print()

print(str(persona3))
print("Tiene un IMC de : " + calcularIMC(persona3.get_peso(), persona3.get_altura()))
if esMayorDeEdad(persona3.get_edad()) is True:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
