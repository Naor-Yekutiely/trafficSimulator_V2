class Graph:
    def __init__(self) -> None:
        pass


import networkx as nx

G = nx.DiGraph()
G.add_edge('a', 'b', weight=1)
G.add_edge('b', 'c', weight=1)
G.add_edge('c', 'f', weight=-1)
G.add_edge('a', 'f', weight=2.9)
print(nx.bellman_ford_path(G, 'a', 'f'))


