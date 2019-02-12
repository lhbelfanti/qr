from . import Node


class Tree:
    def __init__(self, first_square):
        self.base = Node(first_square, None)
        self.leaves = []

    def get_longest_route(self):
        lengths = []
        for node in self.leaves:
            i = 0
            parent = node.parent
            while parent is not None:
                i += 1
                parent = parent.parent

            lengths.append(i)

        route_index = lengths.index(max(lengths))
        route = []

        element = self.leaves[route_index]
        while element is not None:
            route.append(element)
            element = element.parent

        return route[::-1]
