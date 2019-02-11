from subprocess import call

from algorithm import ImageMaker
from PIL import Image
from squares import Square


class Solver:
    def __init__(self):
        self.squares = []
        self.image_maker = None

    def solve(self):
        self.crop_squares()
        self.load_squares()
        self.create_map()
        self.save_map()
        self.join_squares()

    def crop_squares(self):
        call(['convert', 'res/UGY0EKrw.png', '-crop', '48x48', 'res/cropped/square_%d.png'])

    def load_squares(self):
        for i in range(0, 400):
            file_name = './res/cropped/square_' + str(i) + '.png'
            img = Image.open(file_name)
            self.squares.append(Square(i, img))

    def create_map(self):
        self.image_maker = ImageMaker(self.squares)
        self.image_maker.create_map()
        self.image_maker.create_image()

    def save_map(self):
        final_array = []
        for i in range(0, 20):
            for j in range(0, 20):
                final_array.append(self.image_maker.image_map[j][i])

        for x in range(0, len(final_array)):
            sqr = final_array[x]
            filename = './res/reordered/square_' + self.format_number(x + 1) + '.png'
            if sqr is None:
                sqr = final_array[0]

            sqr.new_file_name = filename
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
        call(['montage', '-mode', 'concatenate', '-tile', '20x20',
              'res/reordered/square_*.png', 'res/reordered/final.png'])
