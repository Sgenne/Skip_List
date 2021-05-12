class SkipNode:
    def __init__(self, height, key, value):
        self.forward = [None] * height
        self.key = key
        self.value = value

    