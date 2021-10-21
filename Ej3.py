NUMERO_TEMP = 3
NUMERO_HORAS = 10


def entregado(obj):
    obj.entregado = True


# los getters no son necesarios al llamar la info de un atibuto con "objeto.atributo"
class Serie:
    def __init__(self, titulo="", num_temp=NUMERO_TEMP, genero="", creador=""):
        self.titulo = titulo
        self.num_temp = num_temp
        self.genero = genero
        self.creador = creador
        self.entregado = False

    def set_titulo(self, nom):
        self.titulo = nom

    def set_num_temp(self, num):
        self.num_temp = num

    def set_genero(self, gen):
        self.genero = gen

    def set_creador(self, crea):
        self.creador = crea

    # toString
    def __str__(self):
        return str("Titulo: " + self.titulo + ". Nº Temporadas: " + repr(self.num_temp) + "."
                   + " Genero: " + repr(self.genero) + ". Creador: " + repr(self.creador) + "."
                   + "Entregado: " + repr(self.entregado))


class Videojuego:
    def __init__(self, titulo="", horas_est=NUMERO_HORAS, genero="", compania=""):
        self.titulo = titulo
        self.horas_est = horas_est
        self.genero = genero
        self.compania = compania
        self.entregado = False

    def set_titulo(self, tit):
        self.titulo = tit

    def set_horas_est(self, hor):
        self.horas_est = hor

    def set_genero(self, gen):
        self.genero = gen

    def __str__(self):
        return str("Titulo: " + self.titulo + ". H. Estimadas: " + repr(self.horas_est) + "."
                   + " Genero: " + repr(self.genero) + ". Compañia: " + repr(self.compania) + "."
                   + "Entregado: " + repr(self.entregado))


ser1 = Serie("Pokemon", 5, "Aventura", "Konami")
ser2 = Serie()
ser3 = Serie()
ser4 = Serie("Walking dead", 7, "Drama", "HBO")
ser5 = Serie()
lista_series = [ser1, ser2, ser3, ser4, ser5]

jue1 = Videojuego()
jue2 = Videojuego()
jue3 = Videojuego("Pokemon", 33, "MmoRpg", "Nintendo")
jue4 = Videojuego()
jue5 = Videojuego("League of Legends", 150, "Moba", "Riot Games")
lista_vj = [jue1, jue2, jue3, jue4, jue5]

entregado(ser1)
entregado(ser3)
entregado(jue2)
entregado(jue5)
entregado(ser2)

cont_entregas = 0
aux_ser = ser1
for i in lista_series:
    if i.entregado is True:
        cont_entregas += 1
    if aux_ser.num_temp < i.num_temp:
        aux_ser = i

aux_vj = jue1
for i in lista_vj:
    if i.entregado is True:
        cont_entregas += 1
    if aux_vj.horas_est < i.horas_est:
        aux_vj = i

print("Entregas : " + str(cont_entregas))
print("Mayor Nº de temporadas y Mayor Nº de h. estimadas.")
print(str(aux_ser))
print(str(aux_vj))
