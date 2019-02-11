class Corners:
    def __init__(self, image_map, squares, matcher):
        self.image_map = image_map
        self.squares = squares
        self.matcher = matcher

    def define_corners(self):
        self.find_top_left_corner()
        self.find_top_right_corner()
        self.find_bottom_left_corner()
        self.find_bottom_right_corner()

    def find_top_left_corner(self):
        for sqr in self.squares:
            if sqr is not None and self.matcher.is_top_left_border(sqr.square_color):
                self.image_map[0][0] = sqr
                self.squares[sqr.sqr_id] = None

    def find_top_right_corner(self):
        for sqr in self.squares:
            if sqr is not None and self.matcher.is_top_right_border(sqr.square_color):
                self.image_map[19][0] = sqr
                self.squares[sqr.sqr_id] = None

    def find_bottom_left_corner(self):
        for sqr in self.squares:
            if sqr is not None and self.matcher.is_bottom_left_border(sqr.square_color):
                self.image_map[0][19] = sqr
                self.squares[sqr.sqr_id] = None

    def find_bottom_right_corner(self):
        for sqr in self.squares:
            if sqr is not None and self.matcher.is_bottom_right_border(sqr.square_color):
                self.image_map[19][19] = sqr
                self.squares[sqr.sqr_id] = None
