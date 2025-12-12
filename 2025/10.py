from collections import deque

class Machine:
    def __init__(self, data):
        self.numberOfLights = len(data[0][1:-1])
        self.lights = "." * self.numberOfLights
        
        self.target = 0
        for i, c in enumerate(data[0][1:-1]):
            if c == "#":
                self.target |= (1 << i)        
        self.buttons = []
        for i in range(1, len(data[1:])):
            self.buttons.append([int(x) for x in data[i][1:-1].split(",")])

        # create bin_buttons to represent buttons as bits
        self.bin_buttons = []
        for button in self.buttons:
            bin_button = 0
            for index in button:
                bin_button |= (1 << index)
            self.bin_buttons.append(bin_button)

        self.power_target = [int(x) for x in data[-1][1:-1].split(",")]

    def print_binary_value(self, value):
        print("{:03b}".format(value))

    def press_button(self, current, buttonIndex):
        # Use XOR to toggle bits
        return current ^ self.bin_buttons[buttonIndex]

    def minimumSteps(self):
        # Calculate minimum steps to reach target using BFS
        initial = 0
        queue = deque([(initial, 0)])  # (current_state, steps)
        visited = set()
        while queue:
            current, steps = queue.popleft()
            if current == self.target:
                return steps
            if current in visited:
                continue
            visited.add(current)
            for i in range(len(self.bin_buttons)):
                next_state = self.press_button(current, i)
                if next_state not in visited:
                    queue.append((next_state, steps + 1))

    def press_power_button(self, current, buttonIndex):
        button = self.buttons[buttonIndex]
        for index in button:
            current[index] += 1
        return current
    
    def minimumPowerSteps(self):
        # Trying the same method but I guess this will take forever
        initial = [0] * self.numberOfLights
        queue = deque([(initial, 0)])  # (current_state, steps)
        visited = set()
        while queue:
            current, steps = queue.popleft()
            if any(c > t for c, t in zip(current, self.power_target)):
                continue
            if current == self.power_target:
                return steps
            state_tuple = tuple(current)
            if state_tuple in visited:
                continue
            visited.add(state_tuple)
            for i in range(len(self.buttons)):
                next_state = self.press_power_button(current[:], i)
                state_tuple_next = tuple(next_state)
                if state_tuple_next not in visited:
                    queue.append((next_state, steps + 1))

def part1(machines):
    sum = 0
    for machine in machines:
        sum += machine.minimumSteps()
    return sum

def part2(machines):
    sum = 0
    for machine in machines:
        m = machine.minimumPowerSteps()
        print("Machine power steps:", m)
        sum += m
    return sum

def main():
    input = open("inputs/10.sam").readlines()

    machines = [Machine(line.strip().split(" ")) for line in input if line.strip() != '']

    print("I: \t", part1(machines))
    print("II: \t", part2(machines))

if __name__ == "__main__":
    main()