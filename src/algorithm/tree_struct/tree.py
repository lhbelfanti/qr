from . import Node
from algorithm import QrCode


class Tree:
    def __init__(self, first_square):
        self.base = Node(first_square, None)
        self.leaves = []

    def get_longest_routes(self):
        lengths = []
        for node in self.leaves:
            i = 0
            parent = node.parent
            while parent is not None:
                i += 1
                parent = parent.parent

            lengths.append(i)

        # size required = QrCode.SIZE - 1
        possible_routes = []
        for i in range(0, len(lengths)):
            size = lengths[i]
            if size == (QrCode.SIZE - 1):
                possible_routes.append(i)

        routes = []
        for route_index in possible_routes:
            route = []

            element = self.leaves[route_index]
            while element is not None:
                route.append(element)
                element = element.parent

            route = route[::-1]
            routes.append(route)

        return routes
