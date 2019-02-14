class QrCode:

    SIZE = 0

    def get_correct_first_row(self, routes):
        qr_squares_length = int(QrCode.SIZE / 4)

        for route in routes:
            first_blacks = self.check_blacks(route, 0, qr_squares_length)
            route_len = len(route)
            last_blacks = self.check_blacks(route, route_len - qr_squares_length, route_len)
            if first_blacks and last_blacks:
                return route

        return None

    def check_blacks(self, route, start, end):
        for i in range(start, end):
            if not route[i].square.square_color.has_two_top_blacks():
                return False

        return True




