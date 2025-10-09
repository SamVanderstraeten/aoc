from util.parser import Parser
from util.printer import Printer

file = open("input/1.sam", "r")
lines = file.readlines()

grid = Parser.parse_grid(lines)
Printer.print_grid(grid)