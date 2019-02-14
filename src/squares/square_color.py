from .RGB import RGB


class SquareColor:
    def __init__(self, image):
        self.top_left_color = None
        self.top_right_color = None
        self.bottom_left_color = None
        self.bottom_right_color = None
        self.set_colors(image)

    def set_colors(self, image):
        rgb_im = image.convert('RGB')

        # Top Left
        r, g, b = rgb_im.getpixel((6, 5))
        self.top_left_color = RGB(r, g, b)

        # Top Right
        r, g, b = rgb_im.getpixel((44, 5))
        self.top_right_color = RGB(r, g, b)

        # Bottom Left
        r, g, b = rgb_im.getpixel((6, 44))
        self.bottom_left_color = RGB(r, g, b)

        # Bottom Left
        r, g, b = rgb_im.getpixel((44, 44))
        self.bottom_right_color = RGB(r, g, b)

    def has_two_top_blacks(self):
        blacks = 0
        if self.top_left_color.is_black():
            blacks += 1
        if self.top_right_color.is_black():
            blacks += 1

        return blacks == 2
