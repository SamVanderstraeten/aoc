from stepmachine import Machine

file = open("input/day25.txt", "r")
lines = file.readlines()
fields = [int(x) for x in lines[0].split(",")]

game = Machine("Game", fields, [])

while not game.halted:
    o = game.run()
    print(chr(o), end='')

    if chr(o) == '?':
        print()
        game.add_instruction(input("Your command:").strip())