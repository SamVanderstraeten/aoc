class Printer:
    
    def __init__(self):
        self._p = False
        
    @staticmethod
    def print_grid(grid):
        for row in grid:
            for e in row:
                print(e + " ", end='')
            print()