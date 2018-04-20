"""
Fourmiam

Algorithmes des colonies de fourmis

But : Monter une entreprise de livraison en utilisant des robots qui suivront les itinéraires trouvés par notre
algorithmes, il faut donc optimiser les trajets

Fichiers : Fourmiam.py
"""

import pandas
import networkx as nx
import matplotlib.pyplot as plt

map = pandas.read_csv('VOIES_NM.csv', nrows=5300, sep=",", encoding='latin-1')

for i in range(0, len(map)):
    # Check NaN
    if pandas.isna(map['TENANT'][i]) is True and pandas.isna(map['ABOUTISSANT'][i]) is False:
        map.loc[map.index[i], 'TENANT'] = i

    if pandas.isna(map['TENANT'][i]) is False and pandas.isna(map['ABOUTISSANT'][i]) is True:
        map.loc[map.index[i], 'ABOUTISSANT'] = i

    if pandas.isna(map['BI_MIN'][i]) is False:
        bi_min = map['BI_MIN'][i]
    else:
        bi_min = 1

    if pandas.isna(map['BP_MIN'][i]) is False:
        bp_min = map['BP_MIN'][i]
    else:
        bp_min = 1

    if pandas.isna(map['BI_MAX'][i]) is False:
        bi_max = map['BI_MAX'][i]
    else:
        bi_max = 2

    if pandas.isna(map['BP_MAX'][i]) is False:
        bp_max = map['BP_MAX'][i]
    else:
        bp_max = 2

    if bi_min <= bp_min:
        b_min = bi_min
    else:
        b_min = bp_min

    if bi_max >= bp_max:
        b_max = bi_max
    else:
        b_max = bp_max

    weight = (b_max - b_min)
    map.loc[map.index[i], 'WEIGHT'] = weight

pathways = nx.from_pandas_edgelist(map, 'TENANT', 'ABOUTISSANT', 'WEIGHT')

path = nx.shortest_path(pathways, "SAUTRON Rue de la Bastille", "SAUTRON Rue de Bretagne", "WEIGHT")
path_edges = zip(path, path[1:])

print(path)
print(nx.shortest_path_length(pathways, "SAUTRON Rue de la Bastille", "SAUTRON Rue de Bretagne", "WEIGHT"))

# Coloration du chemin le plus court sur le graph (nécessite plus de mémoire)
# pos = nx.spring_layout(pathways)
# nx.draw(pathways, pos, node_color='k')
# nx.draw_networkx_nodes(pathways, pos, nodelist=path, node_color='r')
# nx.draw_networkx_edges(pathways, pos, edgelist=path_edges, edge_color='r', width=10)

nx.draw_circular(pathways)
plt.axis('equal')
plt.show()
