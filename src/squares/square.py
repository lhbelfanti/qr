from .square_color import SquareColor


class Square:
    def __init__(self, sqr_id, image):
        self.sqr_id = sqr_id
        self.image = image.convert('RGB')
        self.square_color = SquareColor(self.image)
        self.new_file_name = ""

    def delete_red_lines(self):
        # Remove red lines
        self.image = self.image.crop((1, 1, 48, 48))
