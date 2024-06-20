from Trabalho.Encomenda import Encomenda


class EncomendaManager:
    def __init__(self):
        self.encomendas = []
        self.encomendas_backup = []

    # Método para adicionar encomendas
    def adicionar_encomenda(self, destino, peso, hora_entrega):
        encomenda = Encomenda(destino, peso, hora_entrega)
        self.encomendas.append(encomenda)
        self.encomendas_backup.append(encomenda)
        print(f"Encomenda para {encomenda.destino} adicionada com sucesso.\n")

    # Método para obter a lista de encomendas
    def obter_encomendas(self):
        return self.encomendas_backup

    def obter_encomendas_por_destino(self, destino):
        encomendas_por_destino = [encomenda for encomenda in self.encomendas if encomenda.destino == destino]
        return encomendas_por_destino

    # Método para atribuir uma encomenda a uma estafeta (exemplo)
    def atribuir_encomenda_a_estafeta(self, encomenda, estafeta):
        estafeta.adicionar_entrega_pendente(encomenda)
        print(f"Encomenda para {encomenda.destino} atribuída a {estafeta.nome}.")

    # Método para representar a lista de encomendas como uma string

    # Em EncomendaManager
    def imprimir_encomendas(self):
        result = ""
        for encomenda in self.encomendas_backup:
            result += str(encomenda) + "\n"
        return result
