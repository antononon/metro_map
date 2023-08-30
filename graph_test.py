import networkx as nx
import matplotlib.pyplot as plt
import station_graph

metro_graph = nx.Graph()

stations = station_graph.green_line_graph_stations + station_graph.red_line_graph_stations + station_graph.blue_line_graph_stations

metro_graph.add_nodes_from(stations)

edges = station_graph.blue_line_graph_edges + station_graph.red_line_graph_edges + station_graph.green_line_graph_edges + station_graph.conn_green_blue + station_graph.conn_green_red + station_graph.conn_red_blue

metro_graph.add_edges_from(edges)

firstPoint = input("1")
secondPoint = input("2")

path = nx.dijkstra_path(metro_graph, firstPoint, secondPoint)

print(" -> ".join(path))
