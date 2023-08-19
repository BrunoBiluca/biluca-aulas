class CelulaParte:
    pass


class Gride:
    def __init__(self) -> None:
        self.height = 3
        self.width = 3

    def is_inside(self, x, y):
        if x > 0 and x < self.width and y > 0 and y < self.height:
            return True
        else:
            return False

    def get_value(self, x, y):
        pass

    def set_value(self, x, y):
        pass


if __name__ == "__main__":
    gride = Gride()
    a = gride.is_inside(0, -1)
    print(a)
