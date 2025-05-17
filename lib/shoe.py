class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = None  # Optional attribute to be set later

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, (int, float)):
            self._size = value
        else:
            print("size must be a number")

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        self._condition = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
