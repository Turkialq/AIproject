#Nodes and their connection with COST
tree      = {'S':[['B',1.9]],
             'B':[['A',1.8], ['V',1.8],['C',2.7],['S',1.9]],
             'A':[['F',2.7], ['B',1.8]],
             'C':[['H',0.8],['Y',0.8],['B',2.7]],
             'Y':[['I',4.8],['D',4],['C',0.8]],
             'D':[['L',3.6],['E',2.5],['Y',4]],
             'E':[['R',3.4],['D',2.5]],
             'R':[['Q',1.7],['E',3.4]],
             'F':[['Z',0.8],['V',3.8],['A',2.7]],
             'V':[['H',0.8],['F',3.8],['B',1.8]],
             'H':[['I',1.8],['J',1.3],['V',0.8],['C',0.8]],
             'I':[['K',2.8],['H',1.8],['Y',4.8]],
             'Z':[['J',4.6],['M',1.8],['F',0.8]],
             'J':[['K',2.3],['X',1.8],['Z',4.6],['H',1.3]],
             'K':[['L',4.3],['Z2',3.8],['I',2.8],['J',2.3]],
             'Z2':[['P',6.2],['X',4.7],['K',3.8]],
             'L':[['Q',3.6],['D',3.6],['K',4.3]],
             'M':[['X',4.5],['N',3.6],['Z',1.8]],
             'N':[['O',5.5],['M',3.6]],
             'O':[['P',1.7],['Z1',3.6],['X',2.2],['N',5.5]],
             'Z1':[['U',14.8],['O',3.6]],
             'U':[['T',5.7],['Z1',14.8]],
             'T':[['G',1.9],['U',5.7],['Q',1.8]],
             'X':[['O',2.2],['Z2',4.7],['J',1.8],['M',4.5]],
             'P':[['Q',4.8],['Z2',6.2],['O',1.7]],
             'Q':[['T',1.8],['P',4.8],['L',3.6],['R',1.7]]}

heuristic = {'S':16.97,'A':17.79,'B':16.23,'C':14.71,'Y':13.26,'D':10.24,'E':9.7,'F':16.78,'V':15.07,'H':13.37,'I':11.86,'Z':15.94,
'J':12.33,'K':10.38,'L':6.52,'M':15.44,'X':11.35,'Z2':9.15,'N':15.3,'O':10.84,'P':7.81,'Q':2.4,'R':4.13,'Z1':11.6,'U':2.95,
'T':0.87,'G':0

}
cost ={'S':0} 

def AStarSearch():
    global tree, heuristic
    closed = []             # closed nodes
    opened = [['S', 16.97]]     # opened nodes

    '''find the visited nodes'''
    while True:
        fn = [i[1] for i in opened]     # fn = f(n) = g(n) + h(n)
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]  # current node
        closed.append(opened[chosen_index])
        del opened[chosen_index]
        if closed[-1][0] == 'G':        # break the loop if node G has been found
            break
        for item in tree[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            cost.update({item[0]: cost[node] + item[1]})            # add nodes to cost dictionary
            fn_node = cost[node] + heuristic[item[0]] + item[1]     # calculate f(n) of current node
            temp = [item[0], fn_node]
            opened.append(temp)                                     # store f(n) of current node in array opened

    '''find optimal sequence'''
    trace_node = 'G'                        # correct optimal tracing node, initialize as node G
    optimal_sequence = ['G']                # optimal node sequence
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0]           # current node
        if trace_node in [children[0] for children in tree[check_node]]:
            children_costs = [temp[1] for temp in tree[check_node]]
            children_nodes = [temp[0] for temp in tree[check_node]]

            '''check whether h(s) + g(s) = f(s). If so, append current node to optimal sequence
            change the correct optimal tracing node to current node'''
            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                optimal_sequence.append(check_node)
                trace_node = check_node
    optimal_sequence.reverse()              # reverse the optimal sequence

    return closed, optimal_sequence
visited_nodes, optimal_nodes = AStarSearch()
print('visited nodes: ' + str(visited_nodes))
print('optimal nodes sequence: ' + str(optimal_nodes))
