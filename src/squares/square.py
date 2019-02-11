from .square_color import SquareColor


class Square:
    def __init__(self, sqr_id, image):
        self.sqr_id = sqr_id
        self.image = image
        self.square_color = SquareColor(self.image)
        self.new_file_name = ""
