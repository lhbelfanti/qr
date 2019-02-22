from algorithm import QrCode
from squares import Quadrant


class Processor:
    def __init__(self, squares_map):
        self.sqr_map = squares_map

    def process_top_right_neighbour(self, x, y):
        neighbours = []
        neighbours.extend(self.get_square_data((x, y), Quadrant.TOP_RIGHT,
                            [Quadrant.TOP_LEFT, Quadrant.BOTTOM_LEFT, Quadrant.BOTTOM_RIGHT]))
        neighbours.extend(self.get_square_data((x, y - 1), Quadrant.BOTTOM_RIGHT,
                            [Quadrant.BOTTOM_LEFT, Quadrant.BOTTOM_RIGHT]))
        neighbours.extend(self.get_square_data((x + 1, y - 1), Quadrant.BOTTOM_LEFT,
                            [Quadrant.BOTTOM_LEFT]))
        neighbours.extend(self.get_square_data((x + 1, y), Quadrant.TOP_LEFT,
                            [Quadrant.TOP_RIGHT, Quadrant.BOTTOM_LEFT, Quadrant.BOTTOM_RIGHT]))
        return neighbours

    def process_top_left_neighbour(self, x, y):
        neighbours = []
        neighbours.extend(self.get_square_data((x, y), Quadrant.TOP_LEFT,
                            [Quadrant.TOP_RIGHT, Quadrant.BOTTOM_RIGHT, Quadrant.BOTTOM_LEFT]))
        neighbours.extend(self.get_square_data((x, y - 1), Quadrant.BOTTOM_LEFT,
                            [Quadrant.BOTTOM_LEFT, Quadrant.BOTTOM_RIGHT]))
        neighbours.extend(self.get_square_data((x - 1, y - 1), Quadrant.BOTTOM_RIGHT,
                            [Quadrant.BOTTOM_RIGHT]))
        neighbours.extend(self.get_square_data((x - 1, y), Quadrant.TOP_RIGHT,
                            [Quadrant.TOP_RIGHT, Quadrant.BOTTOM_RIGHT]))
        return neighbours

    def process_bottom_left_neighbour(self, x, y):
        neighbours = []
        neighbours.extend(self.get_square_data((x, y), Quadrant.BOTTOM_LEFT,
                            [Quadrant.TOP_RIGHT, Quadrant.TOP_LEFT, Quadrant.BOTTOM_RIGHT]))
        neighbours.extend(self.get_square_data((x - 1, y), Quadrant.BOTTOM_RIGHT,
                            [Quadrant.TOP_RIGHT, Quadrant.BOTTOM_RIGHT]))
        neighbours.extend(self.get_square_data((x - 1, y + 1), Quadrant.TOP_RIGHT,
                            [Quadrant.TOP_LEFT, Quadrant.BOTTOM_LEFT, Quadrant.BOTTOM_RIGHT]))
        neighbours.extend(self.get_square_data((x, y + 1), Quadrant.TOP_LEFT,
                            [Quadrant.BOTTOM_LEFT, Quadrant.BOTTOM_RIGHT, Quadrant.TOP_RIGHT]))
        return neighbours

    def process_bottom_right_neighbour(self, x, y):
        neighbours = []
        neighbours.extend(self.get_square_data((x, y), Quadrant.BOTTOM_RIGHT,
                            [Quadrant.TOP_LEFT, Quadrant.TOP_RIGHT, Quadrant.BOTTOM_LEFT]))
        neighbours.extend(self.get_square_data((x + 1, y), Quadrant.BOTTOM_LEFT,
                            [Quadrant.TOP_LEFT, Quadrant.TOP_RIGHT, Quadrant.BOTTOM_RIGHT]))
        neighbours.extend(self.get_square_data((x + 1, y + 1), Quadrant.TOP_LEFT,
                            [Quadrant.TOP_RIGHT, Quadrant.BOTTOM_RIGHT, Quadrant.BOTTOM_LEFT]))
        neighbours.extend(self.get_square_data((x, y + 1), Quadrant.TOP_RIGHT,
                            [Quadrant.TOP_LEFT, Quadrant.BOTTOM_LEFT, Quadrant.BOTTOM_RIGHT]))
        return neighbours

    def get_square_data(self, pos, quadrant, corners):
        square = None
        x, y = pos
        if (0 <= x < QrCode.SIZE) and (0 <= y < QrCode.SIZE):
            square = self.sqr_map[x][y]

        return self.get_quadrant(square, quadrant, corners)

    def get_quadrant(self, square, quadrant_id, corners):
        if square is None:
            return []

        quadrant = None
        if quadrant_id == Quadrant.TOP_RIGHT:
            quadrant = square.square_color.first_quadrant
        elif quadrant_id == Quadrant.TOP_LEFT:
            quadrant = square.square_color.second_quadrant
        elif quadrant_id == Quadrant.BOTTOM_LEFT:
            quadrant = square.square_color.third_quadrant
        elif quadrant_id == Quadrant.BOTTOM_RIGHT:
            quadrant = square.square_color.fourth_quadrant

        if quadrant is None:
            return []

        neighbours = []
        for corner in corners:
            neighbours.append(quadrant.get_corner_by_id(corner))

        return neighbours
