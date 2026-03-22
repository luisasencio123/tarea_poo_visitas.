from modelos.visitante import Visitante

class VisitaServicio:
    def __init__(self):
        self.__visitantes = []

    def registrar_visitante(self, cedula, nombre, motivo):
        for v in self.__visitantes:
            if v.cedula == cedula:
                return False

        visitante = Visitante(cedula, nombre, motivo)
        self.__visitantes.append(visitante)
        return True

    def obtener_visitantes(self):
        return self.__visitantes

    def eliminar_visitante(self, cedula):
        for v in self.__visitantes:
            if v.cedula == cedula:
                self.__visitantes.remove(v)
                return True
        return False