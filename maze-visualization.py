from mqttclient import get_coordinates
from path_to_walls import Graph
from draw_maze import draw_maze


if __name__ == '__main__':
    coordinates = get_coordinates()
    print("Finished receiving coordinates")

    graph = Graph()
    previous_coordinate = None
    for coordinate in coordinates:
        graph.add_node(coordinate, previous_coordinate)
        previous_coordinate = coordinate

    walls = graph.find_walls()
    draw_maze(walls)
