
class WarehouseGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def dist_calc(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
