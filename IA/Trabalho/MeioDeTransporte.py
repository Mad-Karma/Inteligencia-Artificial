class MeioDeTransporte:
    def __init__(self, nome, velocidade_media, peso_maximo):
        self.nome = nome
        self.velocidade_media = velocidade_media
        self.peso_maximo = 50

    def calcular_velocidade_com_peso(self, peso):
        """
        Método para calcular a velocidade média ajustada pelo peso.
        :param peso: Peso da carga
        :return: Velocidade média ajustada pelo peso
        """
        return max(0, self.velocidade_media - self.calcular_decremento_velocidade(peso))

    def calcular_decremento_velocidade(self, peso):
        """
        Método para calcular o decremento na velocidade média com base no peso da carga.
        :param peso: Peso da carga
        :return: Decremento na velocidade média
        """
        return 0  # Implemente a lógica específica para cada tipo de meio de transporte

    def obter_peso_maximo(self):
        return self.peso_maximo

class Bicicleta(MeioDeTransporte):
    def __init__(self):
        super().__init__('Bicicleta', velocidade_media=10, peso_maximo=5)

    def __str__(self):
        return "bicicleta"

    def calcular_decremento_velocidade(self, peso):
        return 0.6 * peso if peso <= 5 else 0.6 * 5  # Limita o decremento ao máximo de 5 Kg

    def transform_string(self):
        return "bicicleta"

class Moto(MeioDeTransporte):
    def __init__(self):
        super().__init__('Moto', velocidade_media=35, peso_maximo=20)

    def __str__(self):
        return "moto"

    def calcular_decremento_velocidade(self, peso):
        return 0.5 * peso if peso <= 20 else 0.5 * 20  # Limita o decremento ao máximo de 20 Kg

    def transform_string(self):
        return "moto"

class Carro(MeioDeTransporte):
    def __init__(self):
        super().__init__('Carro', velocidade_media=50, peso_maximo=100)

    def __str__(self):
        return "carro"

    def calcular_decremento_velocidade(self, peso):
        return 0.1 * peso if peso <= 100 else 0.1 * 100  # Limita o decremento ao máximo de 100 Kg

    def transform_string(self):
        return "carro"
