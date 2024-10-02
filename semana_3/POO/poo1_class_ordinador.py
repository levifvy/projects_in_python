class Ram:
    def __init__(self, frecuencia, latencia, capacidad):
        self._frecuencia = frecuencia # en MHz
        self._latencia = latencia # en CAS Latency
        self._capacidad = capacidad # en GB

    # Getters
    def get_frecuencia(self):
        return self._frecuencia

    def get_latencia(self):
        return self._latencia

    def get_capacidad(self):
        return self._capacidad

    # Setters
    def set_frecuencia(self, frecuencia):
        self._frecuencia = frecuencia

    def set_latencia(self, latencia):
        self._latencia = latencia

    def set_capacidad(self, capacidad):
        self._capacidad = capacidad

    # Método DDR
    def DDR(self):
        if 3200 <= self._frecuencia <= 7200:
            return "DDR5"
        elif 2133 <= self._frecuencia < 3200:
            return "DDR4"
        elif 800 <= self._frecuencia < 2133:
            return "DDR3"
        else:
            return "DDR Desconocido"

    # Método to_string
    def to_string(self):
        return (f"Frecuencia: {self._frecuencia} MHz, "
                f"Latencia: {self._latencia}, "
                f"Capacidad: {self._capacidad} GB")


class Ordenador:
    def __init__(self, procesador, placabase, memoria_ram, marca, modelo, año, precio_salida):
        self._procesador = procesador
        self._placabase = placabase
        self._memoria_ram = memoria_ram # Debe ser una instancia de Ram
        self._marca = marca
        self._modelo = modelo
        self._año = año
        self._precio_salida = precio_salida # en Euros

    # Getters
    def get_procesador(self):
        return self._procesador

    def get_placabase(self):
        return self._placabase

    def get_memoria_ram(self):
        return self._memoria_ram

    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_año(self):
        return self._año

    def get_precio_salida(self):
        return self._precio_salida

    # Setters
    def set_procesador(self, procesador):
        self._procesador = procesador

    def set_placabase(self, placabase):
        self._placabase = placabase

    def set_memoria_ram(self, memoria_ram):
        self._memoria_ram = memoria_ram

    def set_marca(self, marca):
        self._marca = marca

    def set_modelo(self, modelo):
        self._modelo = modelo

    def set_año(self, año):
        self._año = año

    def set_precio_salida(self, precio_salida):
        self._precio_salida = precio_salida

    # Método gama
    def gama(self):
        if self._precio_salida > 1400:
            return "gama alta"
        elif self._precio_salida > 800:
            return "gama media"
        else:
            return "gama baja"

    # Método to_string
    def to_string(self):
        return (f"El ordenador es de la marca {self._marca}, del modelo {self._modelo}, del año {self._año}, "
                f"que salió con el precio de salida es de la {self.gama()} y en su interior lleva un procesador {self._procesador}, "
                f"y tiene la placa base {self._placabase}, y el tipo de memoria RAM {self._memoria_ram.to_string()}, "
                f"y con un {self._memoria_ram.DDR()}.")
    

    # Ejemplo de uso:
if __name__ == "__main__":
    # Crear una instancia de Ram
    ram1 = Ram(frecuencia=3200, latencia=16, capacidad=16)

    # Crear una instancia de Ordenador
    ordenador1 = Ordenador(
        procesador="Intel Core i7-12700K",
        placabase="ASUS ROG Strix Z690-E",
        memoria_ram=ram1,
        marca="ASUS",
        modelo="ROG Strix",
        año=2023,
        precio_salida=1500
    )

    # Imprimir la descripción del ordenador
    print(ordenador1.to_string())
