class Block:

    def __init__(self,bl):
        self.width = bl[0]
        self.length = bl[1]
        self.height = bl[2]

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        return 2*(self.width * self.length + self.length*self.height + self.height*self.width )