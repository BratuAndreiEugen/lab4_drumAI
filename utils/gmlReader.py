import networkx as nx
import scipy as sp
import numpy as np

def converter(path): # returns adjecency matrix
    graph = nx.read_gml(path)
    m = nx.adjacency_matrix(graph)
    matrix = m.todense() # matricea de adiacenta
    return matrix

def reader_gml(path): # returns networkx graph
    graph = nx.read_gml(path)
    return graph

def input_modifier(network):
    nodes1 = nx.nodes(network)
    edges1 = nx.edges(network)
    map_nodes = {}
    start = 0
    edges = []
    nodes = []
    for nod in nodes1:
        map_nodes[nod] = start
        nodes.append([start])
        start+=1

    for edge in edges1:
        edges.append([map_nodes[edge[0]], map_nodes[edge[1]]])

    return [nodes, edges]
