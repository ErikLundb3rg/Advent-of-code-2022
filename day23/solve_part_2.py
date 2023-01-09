def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

from collections import defaultdict

def getIntention(pos, deltaDirections, elfSet):
  x, y = pos 
 
  validDirections = []
  for deltas in deltaDirections:
    validDirection = True 
    for (dX, dY) in deltas:
      nX, nY = (x+dX, y+dY)
      
      if (nX, nY) in elfSet:
        validDirection = False
        break 
    
    validDirections.append(validDirection)
    
  if all(validDirections) or all([not valid for valid in validDirections]):
    return pos
  
  for index, valid in enumerate(validDirections):
    if valid:
      dX, dY = deltaDirections[index][1]
      return (x+dX, y+dY)     
  
  print('impossible')

def doRound(elfs, deltaDirections):
  wantToGo = defaultdict(int)
  
  intentions = []
  elfSet = set(elfs)
  for elfPos in elfs:
    intention = getIntention(elfPos, deltaDirections, elfSet)
    wantToGo[intention] += 1
    intentions.append(intention)
  
  for i in range(len(intentions)):
    if wantToGo[intentions[i]] == 1:
      elfs[i] = intentions[i]

def getCount(elfs):
  minX = min([x for x, _ in elfs])
  maxX = max([x for x, _ in elfs])+1
  minY = min([y for _, y in elfs])
  maxY = max([y for _, y in elfs])+1
  totalSpaces = (maxX-minX) * (maxY-minY)
  
  return totalSpaces - len(elfs)
  
  
def shiftDirectionPriority(directions):
  front = directions.pop(0)
  directions.append(front)

def printGrid(elfs):
  grid = [['.' for _ in range(40)] for _ in range(40)]
  
  for (x, y) in elfs:
    grid[y+10][x+10] = '#'
    
  for row in grid:
    print("".join(row))

def elfsPosChanged(prev, current):
  for a, b in zip(prev, current):
    if a != b:
      return True

  return False

def main():
  lines = getLines('input.in')
  global grid 
  grid = lines
  
  
  deltaDirections = [
    [(-1, -1), (0, -1), (1, -1)],
    [(-1, 1), (0, 1), (1, 1)],
    [(-1, -1), (-1, 0), (-1, 1)],
    [(1, -1), (1, 0), (1, 1)]
  ]
  
  elfs = []
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == '#':
        elfs.append((x, y))
  
  previousElfs = []
  changed = True
  rnd = 1
  while changed:
    previousElfs = elfs.copy()
    doRound(elfs, deltaDirections)
    shiftDirectionPriority(deltaDirections)
    changed = elfsPosChanged(previousElfs, elfs)
    rnd += 1
    
  print(rnd)
     
if __name__ == '__main__':
  main()