#!/usr/bin/python

from nltk.corpus import wordnet as wn
import networkx as nx
import matplotlib.pyplot as plt
import sys

def closure_graph(synset, fn):
    seen = set()
    graph = nx.DiGraph()

    def recurse(s):
        if not s in seen:
            seen.add(s)
            graph.add_node(s.name)
            for s1 in fn(s):
                graph.add_node(s1.name)
                graph.add_edge(s.name, s1.name)
                recurse(s1)

    recurse(synset)
    return graph


# In[12]:

#label = 'kit_fox'
label = str(sys.argv[1])

graph = closure_graph(wn.synset(label + '.n.01'), lambda s: s.hypernyms())
nx.draw_graphviz(graph, with_labels = True)


# In[10]:

plt.show()
#plt.savefig("plot.png")


# In[ ]:



