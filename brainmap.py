# Brain map mind-map by tranquility

import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist("brain_hemispheres.txt", delimiter=',',data=False)
pos=nx.spring_layout(G)
nx.draw(G,pos,node_size=100,alpha=0.2,edge_color='b',font_size=11,linewidths=0,width=5)
plt.show()
