from matcher import Matcher
from algorithm import Corners


class ImageMaker:
    def __init__(self, squares):
        self.squares = squares
        self.image_map = []
        self.matcher = Matcher()

    def create_map(self):
        for i in range(0, 20):
            self.image_map.append([])
            for j in range(0, 20):
                self.image_map[i].append(None)

    def create_image(self):
        corners = Corners(self.image_map, self.squares, self.matcher)
        corners.define_corners()

        self.make_bases(0, 0)

    def make_bases(self, x, y):
        self.make_right_side(x, y)
        self.make_bottom_side(x, y)

    def make_right_side(self, x, y):
        if (x + 1) < 19:
            self.find_right_element(x, y)
            self.make_right_side(x + 1, y)

    def make_bottom_side(self, x, y):
        if (y + 1) < 19:
            self.find_bottom_element(x, y)
            self.make_bottom_side(x, y + 1)

    def find_right_element(self, x, y):
        element = self.image_map[x][y]
        if element is not None:
            for sqr in self.squares:
                if sqr is not None and not sqr.square_color.has_three_black():
                    self.matcher.set_squares(element, sqr)
                    match_right = self.matcher.match_right()
                    if match_right:
                        self.image_map[x + 1][y] = sqr
                        self.squares[sqr.sqr_id] = None
                        break

    def find_bottom_element(self, x, y):
        element = self.image_map[x][y]
        if element is not None:
            for sqr in self.squares:
                if sqr is not None and not sqr.square_color.has_three_black():
                    self.matcher.set_squares(element, sqr)
                    match_bottom = self.matcher.match_bottom()
                    if match_bottom:
                        self.image_map[x][y + 1] = sqr
                        self.squares[sqr.sqr_id] = None
                        break
