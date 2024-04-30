from ast import literal_eval as make_tuple


class Graph:

    class Node:
        def __init__(self, coordinate):
            self.coordinate = coordinate
            self.neighbors = set()

        def add_neighbor(self, neighbor):
            self.neighbors.add(neighbor)

        def __repr__(self):
            return f'{self.coordinate} -> {self.neighbors}'

    def __init__(self):
        self.nodes = set()

    def add_node(self, coordinate, previous_coordinate=None):
        node = self._get_node(coordinate)
        if previous_coordinate is not None:
            node.add_neighbor(previous_coordinate)

    def _get_node(self, coordinate):
        for node in self.nodes:
            if node.coordinate == coordinate:
                return node
        new_node = self.Node(coordinate)
        self.nodes.add(new_node)
        return new_node

    def find_walls(self):
        walls = set()
        for node in self.nodes:
            c = node.coordinate
            possible_neighbors = {(c[0]+1, c[1]), (c[0]-1, c[1]), (c[0], c[1]+1), (c[0], c[1]-1)}
            missing_neighbors = possible_neighbors - node.neighbors
            walls.update({(c, m) for m in missing_neighbors})
        return walls


def read_coordinates(filename):
    g = Graph()
    with open(filename) as file:
        previous_coordinate = None
        coordinate = None
        for line in file:
            coordinate = make_tuple(line)
            g.add_node(coordinate, previous_coordinate)
            previous_coordinate = coordinate
    return g


if __name__ == "__main__":
    graph = read_coordinates("examples/coordinates1.txt")
    print(graph.nodes)
    print(graph.find_walls())
