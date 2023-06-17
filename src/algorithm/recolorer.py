from squares import Quadrant
from squares import RGB
from algorithm import Processor
from algorithm import QrCode


class Recolorer:
    def __init__(self, squares_map):
        self.sqr_map = squares_map
        self.processor = None

    def recolor_map(self):
        self.invert_map()
        self.recolor()

    def invert_map(self):
        inverted_map = []
        for i in range(0, QrCode.SIZE):
            inverted_map.append([])
            for j in range(0, QrCode.SIZE):
                inverted_map[i].append(None)

        for i in range(0, QrCode.SIZE):
            for j in range(0, QrCode.SIZE):
                inverted_map[i][j] = self.sqr_map[j][i]

        self.sqr_map = inverted_map

    def recolor(self):
        self.processor = Processor(self.sqr_map)
        for i in range(0, QrCode.SIZE):
            for j in range(0, QrCode.SIZE):
                self.process_square((i, j))

    def process_square(self, pos):
        self.processor.sqr_map = self.sqr_map
        self.calculate_and_paint(pos, Quadrant.TOP_RIGHT)
        self.calculate_and_paint(pos, Quadrant.TOP_LEFT)
        self.calculate_and_paint(pos, Quadrant.BOTTOM_LEFT)
        self.calculate_and_paint(pos, Quadrant.BOTTOM_RIGHT)

    def calculate_and_paint(self, pos, corner):
        x, y = pos
        square = self.sqr_map[x][y]
        neighbours = self.get_neighbours(pos, corner)
        color = self.process_neighbours_color(neighbours)
        if color is not None:
            square.square_color.paint_corner(corner, color)
            self.sqr_map[x][y] = square

    def get_neighbours(self, pos, corner):
        x, y = pos
        if corner == Quadrant.TOP_RIGHT:
            return self.processor.process_top_right_neighbour(x, y)
        elif corner == Quadrant.TOP_LEFT:
            return self.processor.process_bottom_left_neighbour(x, y)
        elif corner == Quadrant.BOTTOM_LEFT:
            return self.processor.process_bottom_left_neighbour(x, y)
        elif corner == Quadrant.BOTTOM_RIGHT:
            return self.processor.process_bottom_right_neighbour(x, y)

        return None

    def process_neighbours_color(self, neighbours):
        blacks = 0
        whites = 0

        if neighbours is None or len(neighbours) <= 0:
            return None

        i = 0
        for neighbour in neighbours:
            i += 1
            if neighbour.is_black():
                blacks += 1
            if neighbour.is_white():
                whites += 1

        if blacks > whites or blacks == whites:
            return RGB.BLACK
        else:
            return RGB.WHITE

