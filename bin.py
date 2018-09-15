class Bin:
    def __init__(self):
        self.list = []
        self.filled = 0

    def addItem(self, item):
        self.list.append(item)
        self.filled += item

    def show(self):
        return self.list

    def length(self):
        return len(self.list)
