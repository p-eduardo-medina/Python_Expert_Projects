def josephus(people):
    positions = [n for n in range(1, people + 1)]
    index = 0
    while len(positions) > 1:
        index = (index + 1) % len(positions)
        positions.pop(index)
    return positions[0]


print(josephus(1))
print(josephus(8))
print(josephus(41))