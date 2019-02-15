class Matcher:

    TOP = 'top'
    TOP_LAST = 'top_last'
    BOTTOM_FIRST = 'bottom_first'
    RIGHT = 'right'
    RIGHT_LAST = 'right_last'

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

    def match_right(self):
        if self.sqr1.bottom_right_color.is_black() and self.sqr1.top_right_color.is_black():
            return False

        if self.sqr1.bottom_right_color.matches(self.sqr2.bottom_left_color) and \
                self.sqr1.top_right_color.matches(self.sqr2.top_left_color):
            return True

        return False

    def match_bottom_first(self):
        if self.sqr1.bottom_left_color.is_black() and self.sqr1.bottom_right_color.is_black():
            return False

        if self.sqr1.bottom_right_color.matches(self.sqr2.top_right_color) and \
                self.sqr2.top_left_color.is_black_or_white():
            return True

        return False

    def match_top_last(self):
        if self.sqr1.top_left_color.is_black() and self.sqr1.top_right_color.is_black():
            return False

        if self.sqr1.top_left_color.matches(self.sqr2.bottom_left_color) and \
                self.sqr1.top_right_color.is_black_or_white():
            return True

        return False

    def match_right_last(self):
        if self.sqr1.bottom_right_color.is_black() and self.sqr1.top_right_color.is_black():
            return False

        if self.sqr1.top_right_color.matches(self.sqr2.top_left_color):
            return True

        return False

    def is_top_left_border(self, sqr):
        if sqr.top_left_color.is_black() and \
                sqr.bottom_left_color.is_black() and \
                sqr.top_right_color.is_black():
            return True
        return False

    def matches(self, position):
        matches = False
        if position == Matcher.TOP:
            matches = self.match_top()
        elif position == Matcher.RIGHT:
            matches = self.match_right()
        elif position == Matcher.BOTTOM_FIRST:
            matches = self.match_bottom_first()
        elif position == Matcher.TOP_LAST:
            matches = self.match_top_last()
        elif position == Matcher.RIGHT_LAST:
            matches = self.match_right_last()

        return matches
