from subprocess import call
import os

from algorithm import ImageMaker
from PIL import Image
from squares import Square
from algorithm import QrCode
from algorithm import Recolorer


class Solver:
    def __init__(self, size):
        self.squares = []
        self.image_maker = None
        QrCode.SIZE = size

    def solve(self):
        self.crop_squares()
        self.load_squares()
        self.create_map()
        self.recolor_map()
        self.save_map()
        self.join_squares()

    def crop_squares(self):
        if not os.path.exists('./res/cropped'):
            os.makedirs('./res/cropped')
        call(['convert', 'res/qr.png', '-crop', '48x48', 'res/cropped/square_%d.png'])

    def load_squares(self):
        for i in range(0, 400):
            file_name = './res/cropped/square_' + str(i) + '.png'
            img = Image.open(file_name)
            self.squares.append(Square(i, img))

    def create_map(self):
        self.image_maker = ImageMaker(self.squares)
        self.image_maker.create_map()
        self.image_maker.create_image()

    def recolor_map(self):
        recolorer = Recolorer(self.image_maker.image_map)
        #recolorer.recolor_map()  # The result is not the expected
        recolorer.invert_map()
        self.image_maker.image_map = recolorer.sqr_map

    def save_map(self):
        final_array = []
        for i in range(0, QrCode.SIZE):
            for j in range(0, QrCode.SIZE):
                final_array.append(self.image_maker.image_map[i][j])

        if not os.path.exists('./res/reordered'):
            os.makedirs('./res/reordered')
        for x in range(0, len(final_array)):
            sqr = final_array[x]
            filename = './res/reordered/square_' + self.format_number(x + 1) + '.png'
            if sqr is None:
                sqr = final_array[0]

            sqr.new_file_name = filename
            sqr.delete_red_lines()
            sqr.image.save(sqr.new_file_name, "PNG")

    def format_number(self, x):
        if x < 10:
            image_num = '00' + str(x)
        elif x < 100:
            image_num = '0' + str(x)
        else:
            image_num = str(x)

        return image_num

    def join_squares(self):
        if not os.path.exists('./res/final'):
            os.makedirs('./res/final')
        call(['montage', '-mode', 'concatenate', '-tile', '20x20',
              'res/reordered/square_*.png', 'res/final/final.png'])
