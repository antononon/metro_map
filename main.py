import networkx as nx
from colorama import Back, Style


import station_list # импортируем список станций
import station_graph

def main():
    metro_graph = nx.Graph()
    stations = station_graph.green_line_graph_stations + station_graph.red_line_graph_stations + station_graph.blue_line_graph_stations
    metro_graph.add_nodes_from(stations)
    edges = station_graph.blue_line_graph_edges + station_graph.red_line_graph_edges + station_graph.green_line_graph_edges + station_graph.conn_green_blue + station_graph.conn_green_red + station_graph.conn_red_blue
    metro_graph.add_edges_from(edges)

    print(Back.WHITE + "Введите название первой станции:" + Style.RESET_ALL)
    first_station_data = station_check()


    print(Back.WHITE + "Введите название второй станции:" + Style.RESET_ALL)
    second_station_data = station_check()

    print()

    line_check(first_station_data, second_station_data, metro_graph)

def station_check():
    while True:
        station = input()
        if station in station_list.blue_line:
            line = "blue"
            return station, line
        elif station in station_list.green_line:
            line = "green"
            return station, line            
        elif station in station_list.red_line:
            line = "red"
            return station, line
        else:
            print(Back.RED + "Такой станции нету" + Style.RESET_ALL)
            print(Back.RED + "Введите название еще раз" + Style.RESET_ALL)

def line_check(a, b, metro_graph):
    while True:
        if a[0] == b[0]:
            print(Back.WHITE + "Вы и так на нужной станции))" + Style.RESET_ALL)
            break
        elif a[1] == b[1]:
            route = equal_lines(a,b, metro_graph)
            return route
        elif a[1] == "green":
            route = green_to_line(a,b, metro_graph)
            
            return route
        elif a[1] == "blue":
            route = blue_to_line(a,b, metro_graph)
            return route
        elif a[1] == "red":
            route = red_to_line(a,b, metro_graph)
            return route

def route_generator(first_point, second_point, metro_graph):
    path = nx.dijkstra_path(metro_graph, first_point, second_point)
    route = (" -> ".join(path))
    return route

def equal_lines(a, b, metro_graph):
    route = route_generator(a[0], b[0], metro_graph)
    color = color_check(a[1])
    print(Back.WHITE + "Ваш маршрут:" + Style.RESET_ALL)
    print(color + route + Style.RESET_ALL)

def green_to_line(a, b, metro_graph):
    while True:
        if b[1] == "blue":
            first_point = a[0]
            second_point = b[0]
            route = route_generator(first_point, "Дворец Спорта", metro_graph)
            print(Back.GREEN + route + Style.RESET_ALL)
            print()
            print(Back.WHITE + "Перейдите на станцию Площадь Льва Толстого" + Style.RESET_ALL)
            route = route_generator("Площадь Льва Толстого", second_point, metro_graph)
            print()
            print(Back.BLUE + route + Style.RESET_ALL)
            break
        elif b[1] == "red":
            first_point = a[0]
            second_point = b[0]
            route = route_generator(first_point, "Золотые Ворота", metro_graph)
            print(Back.GREEN + route + Style.RESET_ALL)
            print()
            print(Back.WHITE + "Перейдите на станцию Театральная" + Style.RESET_ALL)
            route = route_generator("Театральная", second_point, metro_graph)
            print()
            print(Back.RED + route + Style.RESET_ALL)
            break

def blue_to_line(a, b, metro_graph):
    while True:
        if b[1] == "green":
            first_point = a[0]
            second_point = b[0]
            route = route_generator(first_point, "Площадь Льва Толстого", metro_graph)
            print(Back.BLUE + route + Style.RESET_ALL)
            print()
            print(Back.WHITE + "Перейдите на станцию Дворец Спорта" + Style.RESET_ALL)
            route = route_generator("Дворец Спорта", second_point, metro_graph)
            print()
            print(Back.GREEN + route + Style.RESET_ALL)
            break
        elif b[1] == "red":
            first_point = a[0]
            second_point = b[0]
            route = route_generator(first_point, "Майдан Независимости", metro_graph)
            print(Back.BLUE + route + Style.RESET_ALL)
            print()
            print(Back.WHITE + "Перейдите на станцию Крещатик" + Style.RESET_ALL)
            route = route_generator("Крещатик", second_point, metro_graph)
            print()
            print(Back.RED + route + Style.RESET_ALL)
            break


def red_to_line(a, b, metro_graph):
    while True:
        if b[1] == "green":
            first_point = a[0]
            second_point = b[0]
            route = route_generator(first_point, "Театральная", metro_graph)
            print(Back.RED + route + Style.RESET_ALL)
            print()
            print(Back.WHITE + "Перейдите на станцию Золотые Ворота" + Style.RESET_ALL)
            route = route_generator("Золотые Ворота", second_point, metro_graph)
            print()
            print(Back.GREEN + route + Style.RESET_ALL)
            break
        elif b[1] == "blue":
            first_point = a[0]
            second_point = b[0]
            route = route_generator(first_point, "Крещатик", metro_graph)
            print(Back.RED + route + Style.RESET_ALL)
            print()
            print(Back.WHITE + "Перейдите на станцию Майдан Независимости" + Style.RESET_ALL)
            route = route_generator("Майдан Независимости", second_point, metro_graph)
            print()
            print(Back.BLUE + route + Style.RESET_ALL)
            break


def color_check(line):
    while True:
        if line == "red":
            color = Back.RED
            return color
        elif line == "blue":
            color = Back.BLUE
            return color
        elif line == "green":
            color = Back.GREEN
            return color
        

if __name__ == "__main__":
    main()


