rows = 296
cols = 3


def initialize():
    return [[None]*cols for x in range(rows)]

def readFile():
    with open(filename) as f:
        line = rf.readline().rstrip('\n')
        