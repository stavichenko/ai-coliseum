class AbstractPlayer:
    config = {
        "shape": "horizontal",
        "values": [[1, 4], [2, 3], [3, 2], [4, 1]],
    }

    def get_setup(self):
        raise NotImplementedError()

    def get_move(self):
        raise NotImplementedError()

    def notify(self, x, y, status):
        raise NotImplementedError()