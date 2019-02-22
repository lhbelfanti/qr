from .quadrant import Quadrant
from .RGB import RGB


class SquareColor:
    def __init__(self, image):
        self.rgb_img = image
        self.first_quadrant = None
        self.second_quadrant = None
        self.third_quadrant = None
        self.fourth_quadrant = None
        self.set_quadrants()

    def set_quadrants(self):
        self.first_quadrant = Quadrant(self.rgb_img)
        self.first_quadrant.setup_quadrant(Quadrant.TOP_RIGHT)

        self.second_quadrant = Quadrant(self.rgb_img)
        self.second_quadrant.setup_quadrant(Quadrant.TOP_LEFT)

        self.third_quadrant = Quadrant(self.rgb_img)
        self.third_quadrant.setup_quadrant(Quadrant.BOTTOM_LEFT)

        self.fourth_quadrant = Quadrant(self.rgb_img)
        self.fourth_quadrant.setup_quadrant(Quadrant.BOTTOM_RIGHT)

    def has_two_top_blacks(self):
        return self.top_left_color.is_black() and self.top_right_color.is_black()

    def paint_corner(self, corner, color):
        if corner == Quadrant.TOP_RIGHT:
            r, g, b = self.rgb_img.getpixel((44, 5))
            rgb = RGB(r, g, b)
            if not rgb.is_white() and not rgb.is_black():
                self.paint(color, (38, 48), (0, 11))
        elif corner == Quadrant.TOP_LEFT:
            r, g, b = self.rgb_img.getpixel((6, 5))
            rgb = RGB(r, g, b)
            if not rgb.is_white() and not rgb.is_black():
                self.paint(color, (0, 11), (0, 11))
        elif corner == Quadrant.BOTTOM_LEFT:
            r, g, b = self.rgb_img.getpixel((6, 44))
            rgb = RGB(r, g, b)
            if not rgb.is_white() and not rgb.is_black():
                self.paint(color, (0, 11), (38, 48))
        elif corner == Quadrant.BOTTOM_RIGHT:
            r, g, b = self.rgb_img.getpixel((44, 44))
            rgb = RGB(r, g, b)
            if not rgb.is_white() and not rgb.is_black():
                self.paint(color, (38, 48), (38, 48))

    def paint(self, color, pos_x, pos_y):
        a, b = pos_x
        c, d = pos_y
        for i in range(a, b):
            for j in range(c, d):
                self.rgb_img.putpixel((i, j), color)

    @property
    def top_right_color(self):
        return self.first_quadrant.top_right

    @property
    def top_left_color(self):
        return self.second_quadrant.top_left

    @property
    def bottom_left_color(self):
        return self.third_quadrant.bottom_left

    @property
    def bottom_right_color(self):
        return self.fourth_quadrant.bottom_right
