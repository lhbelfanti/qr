from .square_color import SquareColor

class Square:
    def __init__(self, sqr_id, image):
        self.sqr_id = sqr_id
        self.image = image
        self.square_color = SquareColor(self.image)
        self.new_file_name = ""

    def delete_colors(self):
        rgb_im = self.image.convert('RGB')
        rgb_im = self.clear_colors(rgb_im)
        rgb_im = self.crop_image(rgb_im)
        self.image = rgb_im

    def clear_colors(self, rgb_im):
        # Top Left
        for i in range(0, 11):
            for j in range(0, 11):
                rgb_im.putpixel((i, j), (0, 0, 0))

        # Top Right
        for i in range(0, 11):
            for j in range(38, 48):
                rgb_im.putpixel((i, j), (0, 0, 0))


        # Bottom Left
        for i in range(38, 48):
            for j in range(0, 11):
                rgb_im.putpixel((i, j), (0, 0, 0))

        # Bottom Left
        for i in range(38, 48):
            for j in range(38, 48):
                rgb_im.putpixel((i, j), (0, 0, 0))

        return rgb_im

    def crop_image(self, rgb_im):
        area = (1, 1, 48, 48)
        return rgb_im.crop(area)
