import networkx as nx
import matplotlib.pyplot as plt

lines = [ line.split(' -> ') for line in open('input.txt').read().splitlines() ]
modules = { srcModule[1:] : (srcModule[0], dstModules.split(', ')) for srcModule, dstModules in lines }
modules['broadcaster'] = modules.pop('roadcaster')

g = nx.DiGraph()

for module, (mType, dstModules) in modules.items():
    for dstModule in dstModules:
        g.add_edge(module, dstModule)

plt.figure(1, figsize=(128, 64), dpi=128)
nx.draw_planar(g, with_labels = True, arrows = True)
plt.savefig("draw_planar_full.png")
