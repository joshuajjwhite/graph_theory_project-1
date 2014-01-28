# Graph Theory Project - Quentin Lautischer and Joshua White
"""
    Assignment 3 - Directions 
    DRIVING ROUTE FINDER
    Part 1: Server

    Part 2: Client
"""
import graph_module


# How to use imported modules.
g_mod = graph_module
g = g_mod.Graph({1,2,3,4,5,6}, [(1,2), (2,1), (3,4), (4,3), (3,5), (5,3), (4,5), (5,4)])
print(g.neighbours(3))
g.add_vertex(7) # methods don't need dot notation
print(g.neighbours(7))
print(g_mod.count_components(g)) #include <Module Name>.function
##############################