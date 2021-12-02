tree = {'S' : [['B', 0.78]],
        'B' : [['A', 1.99],  ['C', 2.10],  ['V', 2.00], ['S', 0.78]],
        'A' : [['F', 1.99],  ['B', 1.99]],
        'C' : [['H', 2.10],  ['Y', 2.00],  ['B', 2.10]],
        'Y' : [['I', 2.00],  ['D', 6.42],  ['C', 2.00]],
        'D' : [['L', 3.68],  ['E', 5.31],  ['Y', 6.42]],
        'E' : [['R', 5.45],  ['D', 5.31]],
        'R' : [['Q', 3.26],  ['E', 5.45]],
        'F' : [['Z', 2.04],  ['V', 1.98],  ['A', 1.99]],
        'V' : [['H', 2.10],  ['B', 2.00],  ['F', 1.98]],
        'H' : [['I', 2.00],  ['J', 2.00],  ['C', 2.10], ['V', 2.10]],
        'I' : [['K', 2.03],  ['Y', 2.00],  ['H', 2.00]],
        'Z' : [['J', 4.00],  ['M', 2.03],  ['F', 2.04]],
        'J' : [['K', 2.22],  ['X', 2.42],  ['H', 2.00], ['Z', 4.00]],
        'K' : [['L', 6.78],  ['Z2', 1.95], ['I', 2.03], ['J', 2.22]],
        'Z2': [['P', 3.06],  ['X', 2.58],  ['K', 1.95]],
        'L' : [['Q', 4.23],  ['D', 3.68],  ['K', 6.78]],
        'M' : [['X', 4.2],   ['N', 3.95],  ['Z', 2.03]],
        'N' : [['O', 4.54],  ['M', 3.95]],
        'O' : [['P', 3.10],  ['Z1', 4.2],  ['N', 4.54], ['X', 3.13]],
        'Z1': [['U', 10.64], ['O', 4.2]],
        'U' : [['T', 3.14],  ['Z1', 10.64]],
        'T' : [['G', 0.94],  ['U', 3.14],  ['Q', 2.02]],
        'X' : [['O', 3.14],  ['Z2', 2.58], ['J', 2.42], ['M', 4.20]],
        'P' : [['Q', 6.72],  ['O', 3.10],  ['Z2', 3.06]],
        'Q' : [['T', 2.02],  ['R', 3.26],  ['L', 4.23], ['P', 6.72]],
        'G' : [['T', 0.94]]
        }

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
             'T':  0.990,
             'X':  11.38,
             'P':  7.830,
             'Q':  2.400,
             'G':  00.00
             }

cost = {'S': 0}


def a_star_search():
    global tree, heuristic
    closed = []             # closed nodes
    opened = [['S', 8]]     # opened nodes

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


if __name__ == '__main__':
    visited_nodes, optimal_nodes = a_star_search()
    print('visited nodes: ' + str(visited_nodes))
    print('optimal nodes sequence: ' + str(optimal_nodes))