import itertools
import math

import networkx as nx
from scipy.sparse.csgraph import connected_components
import random 
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 02:45:18 2020

@author: makigondesk
"""

def gnm_connected_random_graph(n, m, seed=None, directed=False):
    """Returns a $G_{n,m}$ connected random graph.

    In the $G_{n,m}$ model, a graph is chosen uniformly at random from the set
    of all graphs with $n$ nodes and $m$ edges.


    Parameters
    ----------
    n : int
        The number of nodes.
    m : int
        The number of edges.
    seed : integer, random_state, or None (default)
        Indicator of random number generation state.
        See :ref:`Randomness<randomness>`.
    directed : bool, optional (default=False)
        If True return a directed graph

    See also
    --------
    dense_gnm_random_graph

    """
    if directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    G.add_nodes_from(range(n))

    if n == 1:
        return G
    max_edges = n * (n - 1)
    if not directed:
        max_edges /= 2.0
    if m >= max_edges:
        return complete_graph(n, create_using=G)

    nlist = list(G)
    mlist = list(G)
    edge_count = 0
    connect_li = []
    
    while edge_count < 1:
        # generate random edge,u,v
        u = random.choice(nlist)
        v = random.choice(nlist)
        if u == v or G.has_edge(u, v):
            continue
        else:
            G.add_edge(u, v)
            edge_count = edge_count + 1
            connect_li.append(u)
            connect_li.append(v)
            mlist.remove(u)
            mlist.remove(v)
    while len(mlist) != 0:
        # generate random edge,u,v
        u = random.choice(connect_li)
        v = random.choice(mlist)
        if u == v or G.has_edge(u, v):
            continue
        else:
            G.add_edge(u, v)
            edge_count = edge_count + 1
            connect_li.append(v)
            mlist.remove(v)
    while edge_count < m:
        # generate random edge,u,v
        u = random.choice(nlist)
        v = random.choice(nlist)
        if u == v or G.has_edge(u, v):
            continue
        else:
            G.add_edge(u, v)
            edge_count = edge_count + 1
    return G
            
            
            

num = 200
n = 0
cnt = 0

while n!=1:
    G = gnm_connected_random_graph(num, ((num*(num-1))/2)*0.03)
    a = nx.to_numpy_matrix(G)
    n, label = connected_components(a)
    cnt += 1
print(cnt)

nx.draw_networkx(G)
