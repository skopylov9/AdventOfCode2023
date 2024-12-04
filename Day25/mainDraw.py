import networkx as nx
import matplotlib.pyplot as plt

lines = [ line.split(': ') for line in open('input.txt').read().splitlines() ]
nodes = { line[0] : line[1].split(' ') for line in lines }

g = nx.Graph()

for node, dstNodes in nodes.items():
    for dstNode in dstNodes:
        g.add_edge(node, dstNode)

plt.figure(1, figsize=(128, 64), dpi=48)
nx.draw(g, with_labels = True, arrows = True)
plt.savefig("draw_full.png")
