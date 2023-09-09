class CelulaParte:
    pass


class Gride:
    def __init__(self) -> None:
        self.height = 3
        self.width = 3
        self.salas = {
        "0_0": "vazia",
        "0_1": "vazia",
        "0_2": "humano",
        "1_0": "vazia",
        "1_1": "vazia",
        "1_2": "vazia",
        "2_0": "vazia",
        "2_1": "saida",
        "2_2": "vazia",
        }
        

    def is_inside(self, x, y):
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            return True
        else:
            return False

    def get_tipo_sala(self, x, y):
        chave = str(x) + "_" + str(y)
        print(self.salas[chave])
        return self.salas[chave]

    def set_value(self, x, y):
        pass


if __name__ == "__main__":
    gride = Gride()
    a = gride.is_inside(0, 1)
    print("Está dentro: "+ str(a))

    b = gride.get_tipo_sala(0,2)
    print("Tipo da sala:" + str(b))