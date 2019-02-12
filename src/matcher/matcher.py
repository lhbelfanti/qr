class Matcher:

    def __init__(self):
        self.sqr1 = None
        self.sqr2 = None

    def set_squares(self, sqr1, sqr2):
        self.sqr1 = sqr1.square_color
        self.sqr2 = sqr2.square_color

    def match_top(self):
        if self.sqr1.top_left_color.is_black() and self.sqr1.top_right_color.is_black():
            return False

        if self.sqr1.top_left_color.matches(self.sqr2.bottom_left_color) and \
                self.sqr1.top_right_color.matches(self.sqr2.bottom_right_color):
            return True

        return False

    def match_bottom(self):
        if self.sqr1.bottom_left_color.is_black() and self.sqr1.bottom_right_color.is_black():
            return False

        if self.sqr1.bottom_left_color.matches(self.sqr2.top_left_color) and \
                self.sqr1.bottom_right_color.matches(self.sqr2.top_right_color):
            return True

        return False

    def match_left(self):
        if self.sqr1.bottom_left_color.is_black() and self.sqr1.top_left_color.is_black():
            return False

        if self.sqr1.bottom_left_color.matches(self.sqr2.bottom_right_color) and \
                self.sqr1.top_left_color.matches(self.sqr2.top_right_color):
            return True

        return False

    def match_right(self):
        if self.sqr1.bottom_right_color.is_black() and self.sqr1.top_right_color.is_black():
            return False

        if self.sqr1.bottom_right_color.matches(self.sqr2.bottom_left_color) and \
                self.sqr1.top_right_color.matches(self.sqr2.top_left_color):
            return True

        return False

    def is_top_left_border(self, sqr):
        if sqr.top_left_color.is_black() and \
                sqr.bottom_left_color.is_black() and \
                sqr.top_right_color.is_black():
            return True
        return False

    def is_top_right_border(self, sqr):
        if sqr.top_left_color.is_black() and \
                sqr.bottom_right_color.is_black() and \
                sqr.top_right_color.is_black():
            return True
        return False

    def is_bottom_left_border(self, sqr):
        if sqr.bottom_right_color.is_black() and \
                sqr.bottom_left_color.is_black() and \
                sqr.top_left_color.is_black():
            return True
        return False

    def is_bottom_right_border(self, sqr):
        if sqr.bottom_right_color.is_white() and \
                sqr.bottom_left_color.is_white() and \
                sqr.top_right_color.is_white():
            return True
        return False
