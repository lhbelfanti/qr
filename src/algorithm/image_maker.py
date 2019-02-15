from matcher import Matcher
from algorithm import QrCode
from algorithm.tree_struct import Tree


class ImageMaker:
    def __init__(self, squares):
        self.squares = squares
        self.image_map = []
        self.matcher = Matcher()
        self.qr_code = QrCode()
        self.trees = []

    def create_map(self):
        for i in range(0, 20):
            self.image_map.append([])
            for j in range(0, 20):
                self.image_map[i].append(None)

    def create_image(self):
        self.create_first_row()

        for i in range(0, QrCode.SIZE - 1):
            self.create_row(i + 1)

        print("Finish")

    def save_to_image_map(self, route, row_index):
        if route is not None:
            for i in range(0, len(route)):
                square = route[i].square
                self.image_map[i][row_index] = square
                self.squares[square.sqr_id] = None

    def create_first_row(self):
        for sqr in self.squares:
            if self.matcher.is_top_left_border(sqr.square_color):
                self.image_map[0][0] = sqr
                self.squares[sqr.sqr_id] = None
                break

        first_element = self.image_map[0][0]
        self.trees.append(Tree(first_element))
        self.find_branches(self.trees[0].base, 0, 0)
        routes = self.trees[0].get_longest_routes()
        route = self.qr_code.get_correct_first_row(routes)

        self.save_to_image_map(route, 0)
        print("--- Row 0 found")

    def create_row(self, index):
        self.trees = []
        routes = []
        first_elements = self.find_first_element(index)
        for i in range(0, len(first_elements)):
            element = first_elements[i]
            self.trees.append(Tree(element))
            self.find_branches(self.trees[i].base, i, index, True)
            route = self.trees[i].get_longest_routes()
            print("Tree " + str(i))
            print("Route length " + str(len(route)))
            if route is not None and len(route) > 0:
                routes.append(route[0])

        if len(routes) > 0:
            self.save_to_image_map(routes[0], index)
            print("--- Row " + str(index) + " found")

    def find_first_element(self, index):
        previous_element = self.image_map[0][index - 1]
        bottom_squares = self.get_squares(previous_element, Matcher.BOTTOM_FIRST)
        return bottom_squares

    def find_branches(self, node, tree_index, row_index, match_top=False):
        if node.get_distance_to_base() >= (QrCode.SIZE - 1):
            self.trees[tree_index].leaves.append(node)
            return

        position = Matcher.RIGHT
        if row_index == (QrCode.SIZE - 1):
            position = Matcher.RIGHT_LAST

        possible_squares = self.get_squares(node.square, position)
        for i in range(0, len(possible_squares)):
            if match_top:
                if self.match_second_position(row_index, possible_squares[i], node):
                    node.add_branch(possible_squares[i])
            else:
                node.add_branch(possible_squares[i])

        if len(node.branches) == 0:
            self.trees[tree_index].leaves.append(node)

        for j in range(0, len(node.branches)):
            self.find_branches(node.branches[j], tree_index, row_index, match_top)

    def match_second_position(self, row_index, square, parent):
        distance = parent.get_distance_to_base() + 1
        match_with = self.image_map[distance][row_index - 1]
        self.matcher.set_squares(square, match_with)

        position = Matcher.TOP
        if distance == (QrCode.SIZE - 1):
            position = Matcher.TOP_LAST

        if self.matcher.matches(position):
            return True

        return False

    def get_squares(self, element, position):
        elements = []
        if element is not None:
            for sqr in self.squares:
                if sqr is not None:
                    self.matcher.set_squares(element, sqr)
                    if self.matcher.matches(position):
                        elements.append(sqr)
        return elements
