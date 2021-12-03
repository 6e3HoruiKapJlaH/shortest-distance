import networkx as nx   
from generate_graph import generate_arr


def plot(graph, start, finish, scouts, foragers):
    # Create a graph
    G = nx.Graph()

    # distances
    D = graph

    labels = {}
    for n in range(len(D)):
        for m in range(len(D)-(n+1)):
            if D[n][m]:
                G.add_edge(n,n+m+1)
                
    values = []
    
    for edge in G:
        if edge in start:
            values.append('red')
        elif edge in finish:
            values.append('orange')
        elif edge in scouts:
            values.append('green')
        elif edge in foragers:
            values.append('yellow')
        else:
            values.append('blue')

    pos=nx.spring_layout(G)
    nx.draw(G, pos, node_color = values)
    
    import pylab as plt
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.show()

