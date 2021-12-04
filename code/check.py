import networkx as nx
import matplotlib.pyplot as plt

heuristic = {'S':  16.97,
             'B':  16.21,
             'A':  17.83,
             'C':  14.68,
             'Y':  13.30,
             'D':  10.26,
             'E':  9.520,
             'R':  4.000,
             'F':  16.79,
             'V':  15.07,
             'H':  13.40,
             'I':  11.87,
             'Z':  15.94,
             'J':  12.34,
             'K':  10.40,
             'Z2': 9.170,
             'L':  6.570,
             'M':  15.95,
             'N':  15.33,
             'O':  10.83,
             'Z1': 11.65,
             'U':  3.020,
             'T':  0.900,
             'X':  11.38,
             'P':  7.830,
             'Q':  2.400,
             'G':  00.00
             }

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


is_admissible = True
for i in nodes:
    temp = nx.shortest_path_length(g, source=f'{i}', target='G', weight='weight')
    temp_h = heuristic[f'{i}']
    if temp < temp_h:
        is_admissible = False

if is_admissible:
    print('The heuristic is admissible')
else:
    print('The heuristic is NOT admissible')
