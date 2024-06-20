class Encomenda:
    def __init__(self, destino, peso, hora_entrega):
        self.destino = destino
        self.peso = float(peso)
        self.hora_entrega = hora_entrega

    def __str__(self):
        return f"{self.destino} ({self.peso} kg, {self.hora_entrega})"

    def get_destino(self):
        return self.destino

    def get_peso(self):
        return self.peso

    def determinar_veiculo(self, distancia):
        if 1 <= distancia <= 4:
            return "bicicleta"
        elif 4 < distancia <= 6:
            return "mota"
        else:
            return "carro"
