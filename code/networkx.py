import networkx as nx
import matplotlib.pyplot as plt

#all nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z', 'Z1', 'Z2']

g = nx.Graph()
g.add_nodes_from(nodes)


g.add_edge('S', 'B', weight=0.78)
g.add_edge('B', 'A', weight=1.99)
g.add_edge('B', 'V', weight=2.00)
g.add_edge('B', 'C', weight=2.10)
g.add_edge('A', 'F', weight=1.99)
g.add_edge('C', 'H', weight=2.10)
g.add_edge('C', 'Y', weight=2.00)
g.add_edge('Y', 'I', weight=2.0)
g.add_edge('Y', 'D', weight=6.42)
g.add_edge('D', 'L', weight=3.68)
g.add_edge('D', 'E', weight=5.31)
g.add_edge('E', 'R', weight=5.45)
g.add_edge('R', 'Q', weight=3.26)
g.add_edge('F', 'Z', weight=2.04)
g.add_edge('F', 'V', weight=1.98)
g.add_edge('V', 'H', weight=2.1)
g.add_edge('H', 'I', weight=2.00)
g.add_edge('H', 'J', weight=2.00)
g.add_edge('I', 'K', weight=2.03)
g.add_edge('Z', 'J', weight=4.00)
g.add_edge('Z', 'M', weight=2.03)
g.add_edge('J', 'K', weight=2.22)
g.add_edge('J', 'X', weight=2.42)
g.add_edge('K', 'L', weight=6.78)
g.add_edge('K', 'Z2', weight=1.95)
g.add_edge('Z2', 'P', weight=3.06)
g.add_edge('L', 'Q', weight=4.23)
g.add_edge('M', 'X', weight=4.20)
g.add_edge('M', 'N', weight=3.95)
g.add_edge('N', 'O', weight=4.54)
g.add_edge('O', 'P', weight=3.1)
g.add_edge('O', 'Z1', weight=4.2)
g.add_edge('Z1', 'U', weight=10.64)
g.add_edge('U', 'T', weight=3.14)
g.add_edge('T', 'G', weight=0.94)
g.add_edge('X', 'O', weight=3.13)
g.add_edge('X', 'Z2', weight=2.58)
g.add_edge('P', 'Q', weight=6.72)
g.add_edge('Q', 'T', weight=2.02)


pos = nx.spring_layout(g)

nx.draw(g, pos, with_labels=True, node_size=300)

nx.draw_networkx_edge_labels(g, pos, font_size=10, edge_labels=nx.get_edge_attributes(g, 'weight'))
plt.show()

print(nx.shortest_path(g, source='S', target='G', weight='weight'))
