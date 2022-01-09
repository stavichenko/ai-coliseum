class AbstractPlayer:
    def get_setup(self):
        raise NotImplementedError()

    def get_move(self):
        raise NotImplementedError()

    def notify(self, x, y, status):
        raise NotImplementedError()