import math
import os
from IPython.display import clear_output

from Encomenda import Encomenda
from Grafo import Graph


def main():
    g = Graph()

    # Adicionando nós e arestas
    locais = [
        ("Cabanelas", (0, 0), 41.577444226019146, -8.495171807935977),
        ("Cervães", (-1, 1), 41.59861670103133, -8.522671159279675),
        ("Parada de Gatim", (-1, 2), 41.623884001638636, -8.524537567065721),
        ("Escariz", (-1, 3), 41.63668147808751, -8.528824999390569),
        ("Freiriz", (-1, 4), 41.64082883511219, -8.508846465002959),
        ("Moure", (0, 4), 41.63746553715982, -8.477127583512969),
        ("Atiães", (0, 3), 41.62966312583673, -8.491860486538194),
        ("Lage", (1, 2), 41.62253116751869, -8.467777906749479),
        ("Oleiros", (0, 1), 41.611591906588274, -8.48856486385381),
        ("Prado", (1, 1), 41.60795705347527, -8.457706644486882),
    ]

    arestas = [
        ("Cabanelas", "Cervães", 4),
        ("Cabanelas", "Oleiros", 6),
        ("Cabanelas", "Prado", 5.2),
        ("Cervães", "Parada de Gatim", 3.8),
        ("Cervães", "Oleiros", 4.5),
        ("Parada de Gatim", "Escariz", 2),
        ("Parada de Gatim", "Atiães", 4.6),
        ("Parada de Gatim", "Oleiros", 4),
        ("Parada de Gatim", "Freiriz", 2.9),
        ("Escariz", "Freiriz", 1.9),
        ("Freiriz", "Atiães", 4.9),
        ("Freiriz", "Moure", 2.1),
        ("Moure", "Atiães", 4.2),
        ("Moure", "Lage", 5.4),
        ("Atiães", "Oleiros", 3.1),
        ("Atiães", "Lage", 3.7),
        ("Lage", "Prado", 2.6),
        ("Lage", "Oleiros", 2.6),
        ("Oleiros", "Prado", 3.3)
    ]

    for local, loc, latitude, longitude in locais:
        g.add_node(local, loc, latitude, longitude)

    for aresta in arestas:
        g.add_edge(aresta[0], aresta[1], aresta[2])

    nodo_referencia = "Lage"
    g.calcular_heuristicas(nodo_referencia)

    ######################################################
    # Estafetas e Ecomendas para usar ao testar o programa

    g.estafeta_manager.adicionar_estafeta("Joao", "bicicleta")
    g.estafeta_manager.adicionar_estafeta("Diogo", "moto")
    g.estafeta_manager.adicionar_estafeta("Sandra", "carro")
    g.estafeta_manager.adicionar_estafeta("Paulo", "bicicleta")

    g.encomenda_manager.adicionar_encomenda("Prado", "1", "1") # bicicleta
    g.encomenda_manager.adicionar_encomenda("Prado", "2", "2") # bicicleta
    g.encomenda_manager.adicionar_encomenda("Oleiros", "3", "3") # bicicleta
    g.encomenda_manager.adicionar_encomenda("Atiães", "4", "4") # bicicleta
    g.encomenda_manager.adicionar_encomenda("Freiriz", "5", "5") # moto
    g.encomenda_manager.adicionar_encomenda("Cervães", "6", "6") # carro
    ######################################################

    ######################################################
    # Heuristica do grafo

    # Cabanelas: 5.87 - Moto
    # Cervães: 6.66 - Carro
    # Parada de Gatim: 6.31 - Carro
    # Escariz: 6.97 - Carro
    # Freiriz: 5.0 - Moto
    # Moure: 1.96 - Bicicleta
    # Atiães: 2.79 - Bicicleta
    # Oleiros: 2.61 - Bicicleta
    # Prado: 1.97 - Bicicleta
    ######################################################

    ######################################################
    # Algoritmos a implementar

    # BFS
    # DFS
    # A*
    # Greedy
    # Custo uniforme
    # DFS iterativo
    ######################################################

    saida = -2

    while saida != -1:
        print("Selecione o que pretende:")
        print("\n1. Gestão de Encomendas e Estafetas")
        print("2. Algoritmos de Procura")
        print("3. Operações sobre o Grafo")

        saida = int(input("Insira o número da sua escolha (ou -1 para sair): "))

        if saida == 1:
            while saida == 1:
                print("\n\n\n1. Adicionar Estafeta")
                print("2. Adicionar Encomenda")
                print("3. Listar Estafetas")
                print("4. Listar Encomendas")
                print("5. Distribuir Encomendas para Estafeta")
                print("6. Lista Entregas Pendentes de Estafeta")
                print("Insira 0 para voltar ao menu inicial")

                saida = int(input("Insira o número da sua escolha: "))

                if saida == 1:
                    estafeta_nome = input("Nome da estafeta-> ")
                    meio_transporte = input("Meio de transporte (bicicleta/moto/carro)-> ")
                    g.estafeta_manager.adicionar_estafeta(estafeta_nome, meio_transporte)

                elif saida == 2:
                    destino = input("Freguesia destino da encomenda-> ")
                    peso = float(input("Peso da encomenda-> "))
                    hora_entrega = input("Prazo máximo para entrega-> ")
                    g.encomenda_manager.adicionar_encomenda(destino, peso, hora_entrega)

                elif saida == 3:
                    print("\nEstafetas:")
                    print(g.estafeta_manager.imprime_estafetas())

                elif saida == 4:
                    print("\nEncomendas:")
                    encomendas_str = g.encomenda_manager.imprimir_encomendas()
                    print(encomendas_str)

                elif saida == 5:
                    print("A distribuir as encomendas existentes...")
                    lista_encomendas = g.encomenda_manager.obter_encomendas()
                    g.filtrar_encomendas_estafeta(lista_encomendas)
                    print("\nEncomendas distribuídas pelos estafetas existentes.")

                elif saida == 6:
                    estafeta_nome = input("Indique o nome do Estafeta: ")
                    lista_encomendas = g.estafeta_manager.listar_entregas_pendentes_estafeta(estafeta_nome)
                    print("\n")
                    print(lista_encomendas)

        elif saida == 2:
            while saida == 2:
                print("\n\n\n1. DFS")
                print("2. BFS")
                print("3. A*")
                print("4. Greedy")
                print("5. Custo Uniforme")
                print("Insira 0 para voltar ao menu inicial")

                saida = int(input("Insira o número da sua escolha: "))

                if saida == 1:
                    inicio = input("Nodo inicial->")
                    fim = input("Nodo final->")
                    print("Escolha o algoritmo:")
                    print("1 - DFS Recursivo")
                    print("2 - DFS Iterativo")
                    escolha_algoritmo = int(input("Escolha o número do algoritmo->"))

                    if escolha_algoritmo == 1:
                        print(g.procura_DFS(inicio, fim, path=[], visited=set()))
                    elif escolha_algoritmo == 2:
                        print(g.procura_DFS_iterativo(inicio, fim))
                    else:
                        print("Escolha de algoritmo inválida.")

                elif saida == 2:
                    inicio = input("Nodo inicial->")
                    fim = input("Nodo final->")
                    print(g.procura_bfs(inicio, fim))

                elif saida == 3:
                    inicio = input("Nodo inicial->")
                    fim = input("Nodo final->")
                    print(g.procura_A_estrela(inicio, fim))

                elif saida == 4:
                    inicio = input("Nodo inicial->")
                    fim = input("Nodo final->")
                    print(g.procura_greedy(inicio, fim))

                elif saida == 5:
                    inicio = input("Nodo inicial->")
                    fim = input("Nodo final->")
                    print("Implemente o Custo Uniforme aqui.")  # Substitua esta linha pelo seu código

        elif saida == 3:
            while saida == 3:
                print("\n\n\n1-Imprimir Grafo")
                print("2-Desenhar Grafo")
                print("3-Imprimir  nodos de Grafo")
                print("4-Imprimir arestas de Grafo")
                print("5-Imprimir heuristicas de Grafo")
                print("Insira 0 para voltar ao menu inicial")

                saida = int(input("Insira o número da sua escolha: "))

                if saida == 1:
                    print(g.m_graph)
                    l = input("Prima enter para continuar")

                elif saida == 2:
                    g.desenha()

                elif saida == 3:
                    print(g.m_graph.keys())
                    l = input("Prima enter para continuar")

                elif saida == 4:
                    print(g.imprime_aresta())
                    l = input("Prima enter para continuar")

                elif saida == 5:
                    g.imprime_heuristicas()
                    l = input("Prima enter para continuar")

                elif saida == 0:
                    print("Saindo.......")


if __name__ == "__main__":
    main()
