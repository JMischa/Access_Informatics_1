class Canvas:
    def __init__(self, width, height):
        # A canvas consists of *height* number of rows, so for example,
        # ... self.rows[0][0] refers to the top-left pixel
        # ... self.rows[3][5] refers to the 6th pixel on the fourth row
        self.rows = []
        for row in range(height):
            self.rows.append([" "] * width)
        # print(self.rows) given width=5 and height=2 would show:
        # [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
        # and __str__ would return:
        #  -----
        # |     |
        # |     |
        #  -----
        # showing a canvas with two rows and 5 pixels in each row.
        # the border added by __str__ is decorative and not part of the canvas
    def __str__(self):
        # returns the canvas surrounded by a border
        return " " + "-" * len(self.rows[0]) + " \n|" + \
               "|\n|".join(''.join(row) for row in self.rows) + \
               "|\n " + "-" * len(self.rows[0]) + " "
    def draw(self, x, y, path="", char="â–ˆ"):
        # implement this method
        
        if not isinstance(x, int) or not isinstance(y, int):
            raise Exception
        if not isinstance(path, str):
            raise Exception
        if not isinstance(char, str) and len(char) != 1:
            raise Exception
        
        y %= len(self.rows)
        x %= len(self.rows[0])

        self.rows[y][x] = char
        for m in path.lower():
            if m not in "lrud":
                continue
            if m == "r":
                try:
                    self.rows[y][x + 1] = char
                    x += 1
                except IndexError:
                    self.rows[y][0] = char
                    x = 0
            if m == "l":
                try:
                    self.rows[y][x - 1] = char
                    x-= 1
                except IndexError:
                    self.rows[y][-1] = char
                    x = len(self.rows[0])
            if m == "u":
                try:
                    self.rows[y -1][x] = char
                    y-= 1
                except IndexError:
                    self.rows[-1][x] = char
                    y = len(self.rows)
            if m == "d":
                try:
                    self.rows[y + 1][x] = char
                    y+= 1
                except IndexError:
                    self.rows[0][x] = char
                    y = 0

c = Canvas(10, 6)
c.draw(0, 0, "rdr", "+")
print(c)
# ignore non-movement characters; the following path is equivalent to "rd"
# overwrites three of the + signs drawn before
c.draw(0, 0, "weird!")
# draw U shape in the top-right corner
c.draw(7, 0)
c.draw(9, 0)
c.draw(9, 1, "ll")
print(c)
# start in bottom right corner and wrap around the right border
c.draw(9, 5, "RRUR", ">")
# wrap around the left border
c.draw(2, 3, "LLLLL", "<")
# starting coordinates can also wrap around: (25, 25) is the same as (5, 1)
c.draw(25, 25, "uu", "^")
print(c)

