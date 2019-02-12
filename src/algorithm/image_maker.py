from matcher import Matcher
from algorithm.tree_struct import Tree


class ImageMaker:
    def __init__(self, squares):
        self.squares = squares
        self.image_map = []
        self.matcher = Matcher()
        self.tree = None

    def create_map(self):
        for i in range(0, 20):
            self.image_map.append([])
            for j in range(0, 20):
                self.image_map[i].append(None)

    def create_image(self):
        for sqr in self.squares:
            if self.matcher.is_top_left_border(sqr.square_color):
                self.image_map[0][0] = sqr
                self.squares[sqr.sqr_id] = None
                break

        first_element = self.image_map[0][0]
        self.tree = Tree(first_element)
        self.find_branches(self.tree.base)
        route = self.tree.get_longest_route()
        for i in range(0, len(route)):
            self.image_map[i][0] = route[i].square

        print("termino")

    def find_branches(self, square):
        right_squares = self.get_right_squares(square.square)
        for i in range(0, len(right_squares)):
            square.add_branch(right_squares[i])

        if len(square.branches) == 0:
            self.tree.leaves.append(square)

        for j in range(0, len(square.branches)):
            self.find_branches(square.branches[j])

    def get_right_squares(self, element):
        elements = []
        if element is not None:
            for sqr in self.squares:
                if sqr is not None:
                    self.matcher.set_squares(element, sqr)
                    match_right = self.matcher.match_right()
                    if match_right:
                        elements.append(sqr)
        return elements
