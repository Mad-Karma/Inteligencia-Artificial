from Trabalho.MeioDeTransporte import Bicicleta, Moto, Carro
class Estafeta:
    def __init__(self, nome):
        self.nome = nome
        self.entregas_pendentes = []
        self.ranking_satisfacao = 5.0
        self.meio_transporte = None
        self.ponto_partida = "Lage"

    def adicionar_meio_transporte(self, meio_transporte):
        self.meio_transporte = meio_transporte

    def obter_meio_transporte(self):
        return self.meio_transporte

    def adicionar_entrega_pendente(self, encomenda):
        self.entregas_pendentes.append(encomenda)

    def adicionar_ponto_partida(self, ponto_partida):
        self.ponto_partida = ponto_partida

    def obter_entregas_pendentes(self):
        return self.entregas_pendentes

    def adicionar_entregas_pendentes(self, lista_encomendas):
        self.entregas_pendentes.extend(lista_encomendas)

    def calcular_peso_total(self):
        peso_total = 0
        for entrega in self.entregas_pendentes:
            peso_total += entrega.peso
        return peso_total
