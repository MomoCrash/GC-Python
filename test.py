slots: list = {"sdfg": (0,1), 0:(0,2)}

def swap(i, j):
    slots[0] = slots[-1]
    
swap(0, 1)
print(slots)

l: list[tuple[int]] = [ [0, 0], [0, 1], [0, 2] ]
random_index: int = random.randint(0, len(l))

pair_index: tuple[int, int] = l[random_index] 

l[random_index] = l[len(l) - 1]
l.pop()