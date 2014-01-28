# Graph Theory Project - Quentin Lautischer and Joshua White
"""
    Assignment 3 - Directions 
    DRIVING ROUTE FINDER
    Part 1: Server

    Part 2: Client
"""
import graph_module
import sys
import string

# How to use imported modules.
def howto():
    """
    >>> g_mod = graph_module
    >>> g = g_mod.Graph({1,2,3,4,5,6}, [(1,2), (2,1), (3,4), (4,3), (3,5), (5,3), (4,5), (5,4)])
    >>> g.neighbours(3)
    [4, 5]
    >>> g.add_vertex(7)
    >>> g.neighbours(7)
    []
    >>> g_mod.count_components(g)
    4
    """
    pass

# LOAD EDMONTON MAP DATA INTO DIGRAPH OBJECT

"""
Your server on start-up will need to load the Edmonton map data into a digraph object,
and store the ancillary information about street names and vertex locations. 
"""

# Receive and process request
"""
For Part I, your server will be receiving and processing requests from the keyboard, by 
reading and writing to stdin and stdout. All requests will be made by simply providing
a latitude and longitude (in 100,000ths of degrees) of the start and end points in ASCII,
separated by spaces and terminated by a newline. For example,

5365488 -11333914 5364727 -11335890

The server will process this request by computing a shortest path along Edmonton streets and then re- turning the waypoints
(i.e., locations of the vertices along the path). The path will be returned by first printing the length of the path,
followed by a new line. The latitude and longitude of each waypoint along the path is then printed, separated by a space,
and terminated with a new line. For example,

8
5365488 -11333914
5365238 -11334423
5365157 -11334634
5365035 -11335026
5364789 -11335776
5364774 -11335815
5364756 -11335849
5364727 -11335890

After printing the path, the server should listen again for another route finding request.
"""
def cost_distance(e):
    """
    cost_distance returns the straight-line distance between the two
    vertices at the endpoints of the edge e.
    If you compute the straight-line distance directly using lat and long,
    then the distance will be in units of 100,000ths of a degree.
    """
    pass

def translate_input():
    # Sample Input: 5365488 -11333914 5364727 -11335890
    for line in sys.stdin:
        inputs = str.split(line)
        return inputs

# MAIN LOOP
if __name__ == "__main__":
    # Code for processing route finding requests here
    print(translate_input())









