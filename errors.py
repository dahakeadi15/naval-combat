class PlaceNotEmptyError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.message = "Place Not Empty"

    def __str__(self):
        return self.message
