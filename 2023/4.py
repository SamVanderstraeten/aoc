file = open("input/4.sam", "r")
lines = [l.strip() for l in file.readlines()]

class Card:
    def __init__(self, id, str):
        self.id = id
        self.parse(str)

    def parse(self, str):        
        numbers = str.replace("  ", " ").split(": ")[1]
        [winning_numbers, card_numbers] = numbers.split(" | ")

        self.winning_numbers = [int(n) for n in winning_numbers.split(" ")]
        self.card_numbers = [int(n) for n in card_numbers.split(" ")]

    def get_score(self):
        score = 0
        for n in self.winning_numbers:
            if n in self.card_numbers:
                score = 1 if score == 0 else score * 2
        return score
    
    def get_matches(self):
        matches = []
        for n in self.winning_numbers:
            if n in self.card_numbers:
                matches.append(n)
        return len(matches)

# Parse
cards = []
for i, line in enumerate(lines):
    cards.append(Card(i+1, line))

# Part I
total = 0
for card in cards:
    total += card.get_score()
print("Part I:",total)

# Part II
copies = {}
instances = 0
for card in cards:
    num_this_card = 1 + (copies[card.id] if card.id in copies else 0)
    instances = instances + num_this_card
    matches = card.get_matches()
    for i in range(0, matches):
        copy = card.id + i + 1
        copies[copy] = num_this_card if copy not in copies else copies[copy] + num_this_card
print("Part II:",instances)