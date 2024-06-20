from Estafeta import Estafeta
from Trabalho.MeioDeTransporte import Bicicleta, Moto, Carro


class EstafetaManager:
    def __init__(self):
        self.estafetas = {}

    def adicionar_estafeta(self, estafeta_nome, meio_transporte_tipo):
        # Verifica se o estafeta já existe
        if estafeta_nome not in self.estafetas:
            # Cria uma instância do Estafeta com o nome
            estafeta = Estafeta(estafeta_nome)

            # Adicionar o meio de transporte à instância
            if meio_transporte_tipo == "bicicleta":
                meio_transporte = Bicicleta()
            elif meio_transporte_tipo == "moto":
                meio_transporte = Moto()
            elif meio_transporte_tipo == "carro":
                meio_transporte = Carro()
            else:
                print(f"Tipo de meio de transporte inválido: {meio_transporte_tipo}")
                return

            estafeta.adicionar_meio_transporte(meio_transporte)

            # Adicione o estafeta aos dicionários
            self.estafetas[estafeta_nome] = estafeta
            print(f"Estafeta {estafeta_nome} adicionada com sucesso.\n")
        else:
            print(f"Estafeta {estafeta_nome} já existe no sistema.\n")

    def imprime_estafetas(self):
        # Retorna a lista de estafetas com os respetivos meios de transporte
        info_estafetas = {}
        for estafeta_nome, estafeta in self.estafetas.items():
            info_estafetas[estafeta_nome] = estafeta.obter_meio_transporte()
        return info_estafetas

    def obter_estafeta(self, estafeta_nome):
        if estafeta_nome in self.estafetas:
            estafeta = self.estafetas[estafeta_nome]
            return estafeta
        else:
            print(f"O estafeta que indicou, '{estafeta_nome}', não existe.")

    def listar_entregas_pendentes_estafeta(self, estafeta_nome):
        if estafeta_nome in self.estafetas:
            estafeta = self.estafetas[estafeta_nome]
            lista_entregas_pendentes = estafeta.obter_entregas_pendentes()

            if lista_entregas_pendentes:
                print(f"Encomendas pendentes para {estafeta_nome}:")
                for entrega in lista_entregas_pendentes:
                    print(entrega)
            else:
                print(f"O estafeta {estafeta_nome} não tem encomendas pendentes.")
        else:
            print(f"O estafeta que indicou, '{estafeta_nome}', não existe.")