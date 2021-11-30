import networkx as nx   
from generate_graph import generate_arr

# Create a graph
G = nx.Graph()

# distances
D = generate_arr()

labels = {}
for n in range(len(D)):
    for m in range(len(D)-(n+1)):
        if D[n][m]:
            G.add_edge(n,n+m+1)
            #labels[ (n,n+m+1) ] = str(D[n][n+m+1])

pos=nx.spring_layout(G)

nx.draw(G, pos)

import pylab as plt
plt.show()