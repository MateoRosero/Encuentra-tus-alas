from models import Vuelo

class VueloFactory:
    @staticmethod
    def crear_vuelo(origen, destino, fecha, hora_salida, hora_llegada, precio):
        return Vuelo(
            origen=origen,
            destino=destino,
            fecha=fecha,
            hora_salida=hora_salida,
            hora_llegada=hora_llegada,
            precio=precio
        )
