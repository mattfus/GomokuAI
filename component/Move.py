class Move:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    def __str__(self):
        return "move(" + str(self.row) + "," + str(self.column) + ")."