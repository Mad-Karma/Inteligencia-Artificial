# Classe grafo para representaçao de grafos,
import heapq
import math
from queue import Queue, PriorityQueue

import matplotlib.pyplot as plt  # idem
import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo

from EncomendaManager import EncomendaManager
from EstafetaManager import EstafetaManager
from Nodo import Node
from Trabalho.MeioDeTransporte import MeioDeTransporte


# Constructor
# Methods for adding edges
# Methods for removing edges
# Methods for searching a graph
# BFS, DFS
# Other interesting methods

class Graph:

    def __init__(self, directed=False):
        self.m_nodes = dict()
        self.m_directed = directed
        self.m_graph = {}  # dicionario para armazenar os nodos e arestas
        self.m_h = {}  # dicionario para posterirmente armazenar as heuristicas para cada nodo -> pesquisa informada
        self.estafeta_manager = EstafetaManager()
        self.encomenda_manager = EncomendaManager()

    ####################################
    #   add node
    ####################################

    def add_node(self, node_name, node_loc, node_latitude, node_longitude):
        new_node = Node(node_name, node_loc, node_latitude, node_longitude)
        if new_node not in self.m_nodes:
            new_node.setId(len(self.m_nodes))
            self.m_nodes[node_name] = new_node
            self.m_graph[node_name] = []

    ######################################
    #    escrever o grafo como string
    #####################################
    def __str__(self):
        out = ""
        for key in self.m_graph.keys():
            out = out + "node" + str(key) + ": " + str(self.m_graph[key]) + "\n"
        return out

    #################################### Estafetas
    def adicionar_estafeta(self, estafeta_nome, meio_transporte):
        self.estafeta_manager.adicionar_estafeta(estafeta_nome, meio_transporte)

    def obter_estafeta(self, estafeta_nome):
        return self.estafeta_manager.obter_estafeta(estafeta_nome)

    def listar_entregas_pendentes_estafeta(self, estafeta_nome):
        return self.estafeta_manager.listar_entregas_pendentes_estafeta(estafeta_nome)

    def imprime_estafetas(self):
        return self.estafeta_manager.imprime_estafetas()

    #################################### Encomendas
    def adicionar_encomenda(self, destino, peso, hora_entrega):
        self.encomenda_manager.adicionar_encomenda(destino, peso, hora_entrega)

    # obter encomenda por destino
    def obter_encomendas_por_destino(self, destino):
        return self.encomenda_manager.obter_encomendas_por_destino(destino)

    # imprimir encomendas
    def imprimir_encomendas(self):
        return self.encomenda_manager.imprimir_encomendas()

    ###############################
    #   encontrar nodo pelo nome
    ################################

    def get_node_by_name(self, name):
        return self.m_nodes[name]

    def neighbors(self, node_name):
        return [adjacente for adjacente, peso in self.m_graph[node_name]]

    ############################
    #   imprimir arestas
    ############################

    def imprime_aresta(self):
        listaA = ""
        lista = self.m_graph.keys()
        for nodo in lista:
            for (nodo2, custo) in self.m_graph[nodo]:
                listaA = listaA + nodo + " ->" + nodo2 + " custo:" + str(custo) + "\n"
        return listaA

    ################
    #   adicionar   aresta no grafo
    ######################

    def add_edge(self, node1, node2, weight):
        self.m_graph[node1].append((node2, weight))  # poderia ser n1 para trabalhar com nodos no grafo

        if not self.m_directed:
            self.m_graph[node2].append((node1, weight))

    #############################
    # devolver nodos
    ##########################

    def getNodes(self):
        return self.m_nodes

    #######################
    #    devolver o custo de uma aresta
    ##############3

    def get_arc_cost(self, node1, node2):
        custoT = math.inf
        a = self.m_graph[node1]  # lista de arestas para aquele nodo
        for (nodo, custo) in a:
            if nodo == node2:
                custoT = custo

        return custoT

    def __getitem__(self, key):
        return self.m_nodes[key]

    ##############################
    #  dado um caminho calcula o seu custo
    ###############################

    def calcula_custo(self, caminho):
        # caminho é uma lista de nodos
        teste = caminho
        custo = 0
        i = 0
        while i + 1 < len(teste):
            custo = custo + self.get_arc_cost(teste[i], teste[i + 1])
            i = i + 1
        return custo

    ##############################
    #  calcula a distância em linha reta entre duas freguesias
    ###############################

    def calcular_distancia_em_linha_reta(self, nodo1, nodo2):
        lat1, lon1 = math.radians(nodo1.m_latitude), math.radians(nodo1.m_longitude)
        lat2, lon2 = math.radians(nodo2.m_latitude), math.radians(nodo2.m_longitude)

        # Fórmula da distância euclidiana em um espaço tridimensional
        distancia = math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

        # Raio da Terra em quilômetros (aproximado)
        raio_terra_km = 6371.0

        # Multiplica pela circunferência da Terra para obter a distância em quilômetros
        distancia_em_km = raio_terra_km * distancia
        distancia_arredondada = round(distancia_em_km, 2)

        return distancia_arredondada

    ##############################
    #  Preenche o dicionário das heuristicas
    ###############################

    def calcular_heuristicas(self, nodo_referencia):
        nodo_referencia_obj = self.m_nodes[nodo_referencia]

        for nodo_nome, nodo_obj in self.m_nodes.items():
            if nodo_nome != nodo_referencia:
                distancia = self.calcular_distancia_em_linha_reta(nodo_referencia_obj, nodo_obj)
                self.m_h[nodo_nome] = distancia

    def imprime_heuristicas(self):
        print("Heurísticas:")
        for nodo, heuristica in self.m_h.items():
            print(f"{nodo}: {heuristica}")

    def get_heuristica(self, node_nome):
        return self.m_h.get(node_nome, None)

    ###########################
    # desenha grafo  modo grafico
    #########################

    def desenha(self):
        ## criar lista de vertices
        lista_v = self.m_nodes.values()
        lista_a = []
        g = nx.Graph()
        for nodo in lista_v:
            n = nodo.getName()
            g.add_node(n)
            for (adjacente, peso) in self.m_graph[n]:
                lista = (n, adjacente)
                # lista_a.append(lista)
                g.add_edge(n, adjacente, weight=peso)

        # Ajustar o tamanho da figura
        plt.figure(figsize=(12, 10))  # Ajuste os valores de largura e altura conforme necessário

        pos = nx.spring_layout(g)
        nx.draw_networkx(g, pos, with_labels=True, font_weight='bold')
        labels = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)

        plt.draw()
        plt.show()

    ################
    # Distribui as encomendas pelos Estafetas
    ###############

    def filtrar_encomendas_estafeta(self, encomendas):
        for estafeta_nome in self.estafeta_manager.estafetas:
            estafeta = self.estafeta_manager.estafetas[estafeta_nome]
            entregas_pendentes = estafeta.obter_entregas_pendentes()
            meio_transporte = estafeta.obter_meio_transporte()
            encomendas_copia = encomendas.copy()
            encomendas_a_remover = []
            print("For 1")

            if not entregas_pendentes:
                print("If 1")
                for encomenda in encomendas_copia:
                    destino = encomenda.get_destino()
                    distancia = self.get_heuristica(destino)
                    print("For 2")
                    if encomenda.determinar_veiculo(distancia) == meio_transporte.transform_string():
                        estafeta.adicionar_entrega_pendente(encomenda)
                        encomendas_a_remover.append(encomenda)
                        print("Yes")
                        break

            if estafeta.calcular_peso_total() < meio_transporte.obter_peso_maximo():
                if entregas_pendentes:
                    print("If 2")
                    for encomenda in encomendas_copia:
                        freguesia = entregas_pendentes[-1].get_destino()
                        vizinhos = self.neighbors(freguesia)
                        destino = encomenda.get_destino()
                        distancia = self.get_heuristica(destino)
                        print("For 3")
                        if encomenda.get_destino() in vizinhos:
                            if encomenda.determinar_veiculo(distancia) == meio_transporte.transform_string:
                                if estafeta.calcular_peso_total() < meio_transporte.obter_peso_maximo():
                                    estafeta.adicionar_entrega_pendente(encomenda)
                                    encomendas_a_remover.append(encomenda)
                                    print("OLAAAAAAAAAA")
            print(f"Antes do primeiro loop: {len(encomendas_a_remover)}")
            for encomenda in encomendas_a_remover:
                if encomenda in encomendas:
                    encomendas.remove(encomenda)
                    print("For 4")

        if encomendas:
            encomendas_copia = encomendas.copy()
            encomendas_a_remover = []
            for encomenda in encomendas_copia:
                destino = encomenda.get_destino()
                distancia = self.get_heuristica(destino)
                print("For 5")
                for estafeta_nome in self.estafeta_manager.estafetas:
                    estafeta = self.estafeta_manager.estafetas[estafeta_nome]
                    meio_transporte = estafeta.obter_meio_transporte()
                    print("For 6")
                    if encomenda.determinar_veiculo(distancia) == meio_transporte.transform_string():
                        if isinstance(meio_transporte, MeioDeTransporte) and estafeta.calcular_peso_total() < meio_transporte.obter_peso_maximo():
                            estafeta.adicionar_entrega_pendente(encomenda)
                            encomendas_a_remover.append(encomenda)
                            print("Yes1")

            for encomenda in encomendas_a_remover:
                if encomenda in encomendas:
                    encomendas.remove(encomenda)
                    print("For 7")

        if encomendas:
            encomendas_copia = encomendas.copy()
            encomendas_a_remover = []
            for encomenda in encomendas_copia:
                print("For 8")
                for estafeta_nome in self.estafeta_manager.estafetas:
                    print("For 9")
                    estafeta = self.estafeta_manager.estafetas[estafeta_nome]
                    meio_transporte = estafeta.obter_meio_transporte()
                    if isinstance(meio_transporte, MeioDeTransporte) and estafeta.calcular_peso_total() < meio_transporte.obter_peso_maximo():
                        estafeta.adicionar_entrega_pendente(encomenda)
                        encomendas_a_remover.append(encomenda)
                        print("Yes2")

            for encomenda in encomendas_a_remover:
                if encomenda in encomendas:
                    encomendas.remove(encomenda)
                    print("For 10")

    ################################################################################
    ################################################################################

    ################################################################################
    #     procura DFS
    ####################################################################################

    def procura_DFS(self, start, end, path=None, visited=None):
        if path is None:
            path = []

        if visited is None:
            visited = set()

        path.append(start)
        visited.add(start)

        if start == end:
            # calcular o custo do caminho funçao calcula custo.
            custoT = self.calcula_custo(path)
            return (path, custoT)
        for (adjacente, peso) in self.m_graph[start]:
            if adjacente not in visited:
                resultado = self.procura_DFS(adjacente, end, path, visited)
                if resultado is not None:
                    return resultado
        path.pop()  # se nao encontra remover o que está no caminho......
        return None

    #####################################################
    # Procura BFS
    ######################################################

    def procura_bfs(self, start, end):
        # definir nodos visitados para evitar ciclos
        visited = set()
        fila = Queue()
        custo = 0
        # adicionar o nodo inicial à fila e aos visitados
        fila.put(start)
        visited.add(start)

        # garantir que o start node nao tem pais...
        parent = dict()
        parent[start] = None

        path_found = False
        while not fila.empty() and path_found == False:
            nodo_atual = fila.get()
            if nodo_atual == end:
                path_found = True
            else:
                for (adjacente, peso) in self.m_graph[nodo_atual]:
                    if adjacente not in visited:
                        fila.put(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)

        # reconstruir o caminho

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # funçao calcula custo caminho
            custo = self.calcula_custo(path)
        return (path, custo)

    #####################################################
    # Procura A*
    ######################################################

    def reconstruir_caminho(self, parent, end):
        caminho = [end]
        custo_total = 0

        while end in parent:
            custo_total += parent[end][1]
            end = parent[end][0]
            caminho.append(end)

        caminho.reverse()
        return caminho, custo_total

    def procura_A_estrela(self, start, end):
        fila_prioridade = PriorityQueue()
        fila_prioridade.put((0, start))  # Tupla: (custo_acumulado + heuristica, nodo)
        visited = set()
        parent = dict()
        custo_so_far = dict()
        custo_so_far[start] = 0

        while not fila_prioridade.empty():
            custo, atual = fila_prioridade.get()

            if atual == end:
                return self.reconstruir_caminho(parent, end)

            visited.add(atual)

            for vizinho, peso in self.m_graph[atual]:
                novo_custo = custo_so_far[atual] + peso
                if vizinho not in visited or novo_custo < custo_so_far.get(vizinho, float('inf')):
                    custo_so_far[vizinho] = novo_custo
                    prioridade = novo_custo + self.get_heuristica(vizinho)
                    fila_prioridade.put((prioridade, vizinho))
                    parent[vizinho] = (atual, peso)

        # Se não encontrou um caminho
        return None, 0

    #####################################################
    # Procura Greedy
    #####################################################

    def procura_greedy(self, start, end):
        fila_prioridade = PriorityQueue()
        fila_prioridade.put((0, start))  # Tupla: (heuristica, nodo)
        visited = set()
        parent = dict()

        while not fila_prioridade.empty():
            heuristica, atual = fila_prioridade.get()

            if atual == end:
                return self.reconstruir_caminho(parent, end)

            visited.add(atual)

            for vizinho, peso in self.m_graph[atual]:
                if vizinho not in visited:
                    prioridade = self.get_heuristica(vizinho)
                    fila_prioridade.put((prioridade, vizinho))
                    parent[vizinho] = (atual, peso)

        # Se não encontrou um caminho
        return None, 0

    #####################################################
    # Procura Custo Uniforme
    #####################################################

    def procura_custo_uniforme(self, start, end):
        fila_prioridade = PriorityQueue()
        fila_prioridade.put((0, start))  # Tupla: (custo_acumulado, nodo)
        visited = set()
        parent = dict()
        custo_so_far = dict()
        custo_so_far[start] = 0

        while not fila_prioridade.empty():
            custo, atual = fila_prioridade.get()

            if atual == end:
                return self.reconstruir_caminho(parent, end)

            visited.add(atual)

            for vizinho, peso in self.m_graph[atual]:
                novo_custo = custo_so_far[atual] + peso
                if vizinho not in visited or novo_custo < custo_so_far.get(vizinho, float('inf')):
                    custo_so_far[vizinho] = novo_custo
                    fila_prioridade.put((novo_custo, vizinho))
                    parent[vizinho] = (atual, peso)

        # Se não encontrou um caminho
        return None, 0

    ################################################################################
    #     procura DFS Iterativa
    ####################################################################################
    def procura_DFS_iterativo(self, start, end):
        visited = set()
        stack = []
        custo = 0
        stack.append(start)
        visited.add(start)

        parent = {start: None}
        path_found = False

        while stack and not path_found:
            nodo_atual = stack.pop()
            if nodo_atual == end:
                path_found = True
            else:
                # Ordenar os vizinhos para garantir uma ordem determinística
                neighbors = sorted(self.m_graph[nodo_atual], key=lambda x: x[0])
                for (adjacente, peso) in neighbors:
                    if adjacente not in visited:
                        stack.append(adjacente)
                        parent[adjacente] = nodo_atual
                        visited.add(adjacente)

        path = []
        if path_found:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            custo = self.calcula_custo(path)
        return path, custo







    # def calcula_heuristica(self, destino):
    #     dest = [n for n in destino if n.getName() == destino][0]
    #
    #     for n in self.m_nodes:
    #         self.m_h[n.getName()] = dist(n.getLocation(), dest.getLocation()) * 5


    # def dist(a, b):
    #     xa, ya = a
    #     xb, yb = b
    #     return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
