def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

def getAlternatives(pos):
  x, y = pos
  return [
    (x, y-1),
    (x, y+1),
    (x-1, y),
    (x+1, y),
    (x, y)
  ]
  
def nextBlizzardsState(blizzards):
  global grid
  newBlizzards = [] 
  
  for b in blizzards:
    x, y, dX, dY = b
    nX, nY = (x+dX, y+dY)
    
    if nY == 0:
      nY = len(grid)-2
    elif nY == len(grid)-1:
      nY = 1
    if nX == 0:
      nX = len(grid[0])-2
    elif nX == len(grid[0])-1:
      nX = 1
    newBlizzards.append((nX, nY, dX, dY))
 
  return newBlizzards

def printBlizzards(xs):
  grid = [['.' for _ in range(10)] for _ in range(10)]
  
  for a in xs:
    x, y, _ , _ = a
    grid[y-1][x-1] = 'B'
  
  for row in grid:
    print("".join(row))
  
def inBounds(neighbor):
  global grid
  x, y = neighbor
  return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)
  
  
def simulate(start, finish, blizzards):
  possiblePositions = [start]
  finished = False 
  minutes = 0
  
  while not finished:
    blizzards = nextBlizzardsState(blizzards)
    blizzardSet = set([(x, y) for x, y, _, _ in blizzards])
    nextMinutePositions = []
    currentMinutePositions = set()
  
    for pos in possiblePositions:
      if pos == finish:
        return minutes 
      
      for alternative in getAlternatives(pos):
        if inBounds(alternative) and alternative not in currentMinutePositions and grid[alternative[1]][alternative[0]] != '#' and not alternative in blizzardSet:
          nextMinutePositions.append(alternative)
          currentMinutePositions.add(alternative)

    possiblePositions = nextMinutePositions 
    minutes += 1
  
  return -1 
    
    
def main():
  lines = getLines('input.in')
  
  global grid
  grid = lines
  
  blizzards = [] 
  
  signToDirection = {
    '<': (-1, 0),
    '>': (1, 0),
    'v': (0, 1),
    '^': (0, -1)
  }
 
  start = (1, 0)
  for y in range(len(lines)):
    for x in range(len(lines[0])):
      c = lines[y][x]
    
      if c == 'E':
        continue
      if c == '#':
        continue
      if not (c == '.'):
        dX, dY = signToDirection[c]
        blizzards.append((x, y, dX, dY))
        continue

  finish = (len(grid[0])-2, len(grid)-1)
 
  print(simulate(start, finish, blizzards))
    
if __name__ == '__main__':
  main()