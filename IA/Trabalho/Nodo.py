# Classe nodo para definiçao dos nodos
# cada nodo tem um nome e um id
class Node:
    def __init__(self, name, loc, lati, longi, id=-1):     #  construtor do nodo....."
        self.m_id = id
        self.m_name = str(name)
        self.m_location = loc
        self.m_latitude = lati
        self.m_longitude = longi


    def __str__(self):
        return "node " + self.m_name

    def setId(self, id):
        self.m_id = id

    def getId(self):
        return self.m_id

    def getName(self):
        return self.m_name

    def getLocation(self):
        return self.m_location

    def getLatitude(self):
        return self.m_latitude

    def getLongitude(self):
        return self.m_longitude

    def __eq__(self, other):
        return self.m_name == other.m_name

    def __hash__(self):
        return hash(self.m_name)