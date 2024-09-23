__author__ = "Mischa Jampen"

class MagicDrawingBoard:
    def __init__(self, x, y):
        if x < 1 or y < 1:
            raise Warning("Invalid board-size")
        self.x = x
        self.y = y
        self.board = []

        for i in range(self.y):
            self.board.append([0] * self.x)

    def pixel(self, pixel_coord):
        if pixel_coord[0] < 0 or pixel_coord[1] < 0:
            raise Warning("Invalid coordinates")
        elif pixel_coord[0] < self.x or pixel_coord[1] < self.y:
            raise Warning("coordinates out of bound")
        else:
            self.board[pixel_coord[1]][pixel_coord[0]] = "1"

    def rect(self, start, end):
        if start[0] < 0 or start[1] < 0 or end[0] < 0 or end[1] < 0:
            raise Warning("Invalid coordinates input")
        if end[0] < start[0] or end[1] < start[1]:
            raise Warning("Invalid rect input")
        if start[0] < self.x or start[1] < self.y or end[0] < self.x or end[1] < self.y:
            raise Warning("Coordinates out of bound")
        
        try:
            for char in range(end[1] - start[1]):
                self.board[start[1] + char][start[0]:end[0]] = "1" * (end[0] - start[0])
        except:
            raise Warning("rect out of boarders")
     
    def reset(self):
        self.board = []
        for i in range(self.y):
            self.board.append([0] * self.x)
        
    def img(self):
        res = ""
        for i in self.board:
            res += "".join(map(str, i)) + '\n'
        res = res[:-1]
        return res
        
# Uncomment the following code to start using your implementation
if __name__ == "__main__":

    db = MagicDrawingBoard(6,4)
    db.pixel((1,1))
    img = db.img()
    print(img)
    db.rect((2,2), (2,2))
    img = db.img()
    print(img)