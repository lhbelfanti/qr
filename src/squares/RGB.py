class RGB:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def matches(self, rgb):
        if self.r == rgb.r and self.g == rgb.g and self.b == rgb.b:
            return True

        return False

    def is_black(self):
        if self.r == 0 and self.g == 0 and self.g == 0:
            return True

        return False

    def is_white(self):
        if self.r == 255 and self.g == 255 and self.g == 255:
            return True

        return False

    def is_black_or_white(self):
        return self.is_black() or self.is_white()
