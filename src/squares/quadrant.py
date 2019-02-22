from .RGB import RGB


class Quadrant:
    TOP_LEFT = "top_left"
    TOP_RIGHT = "top_right"
    BOTTOM_LEFT = "bottom_left"
    BOTTOM_RIGHT = "bottom_right"

    def __init__(self, square_image):
        self.image = square_image
        self.top_left = None
        self.top_right = None
        self.bottom_left = None
        self.bottom_right = None

    def setup_quadrant(self, main_corner):
        if main_corner == Quadrant.TOP_RIGHT:
            self.set_squares((44, 5), (34, 5), (34, 15), (44, 15))
        elif main_corner == Quadrant.TOP_LEFT:
            self.set_squares((16, 5), (6, 5), (6, 15), (16, 15))
        elif main_corner == Quadrant.BOTTOM_LEFT:
            self.set_squares((16, 34), (6, 34), (6, 44), (16, 44))
        elif main_corner == Quadrant.BOTTOM_RIGHT:
            self.set_squares((44, 34), (34, 34), (34, 44), (44, 44))

    def set_squares(self, top_right, top_left, bottom_left, bottom_right):
        r, g, b = self.image.getpixel(top_right)
        self.top_right = RGB(r, g, b)
        r, g, b = self.image.getpixel(top_left)
        self.top_left = RGB(r, g, b)
        r, g, b = self.image.getpixel(bottom_left)
        self.bottom_left = RGB(r, g, b)
        r, g, b = self.image.getpixel(bottom_right)
        self.bottom_right = RGB(r, g, b)

    def get_corner_by_id(self, corner):
        if corner == Quadrant.TOP_RIGHT:
            return self.top_right
        elif corner == Quadrant.TOP_LEFT:
            return self.top_left
        elif corner == Quadrant.BOTTOM_LEFT:
            return self.bottom_left
        elif corner == Quadrant.BOTTOM_RIGHT:
            return self.bottom_right
