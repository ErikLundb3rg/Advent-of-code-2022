def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

def main():
  inp = getLines('input.in')
  
  nonAir = set() 
  floorY = -1
  for line in inp:
    cords = [eval(x) for x in line.split(' -> ')]
    floorY = max(floorY, max([cord[1] for cord in cords]))
    
    start = cords[0]
    for i in range(1, len(cords)):
      end = cords[i]
      
      traversal = start 
      nonAir.add(traversal)
      
      while traversal != end:
        dx = 0 if end[0] == start[0] else 1 if end[0] > start[0] else -1
        dy = 0 if end[1] == start[1] else 1 if end[1] > start[1] else -1
        newCords = (traversal[0]+dx, traversal[1]+dy)
        traversal = newCords
        nonAir.add(newCords)
      start = end
  
  floorY += 2
  sandBlocks = 0 
  runSimulation = True
  startingPoint = (500, 0)
  while runSimulation:
    pos = startingPoint 
  
    continueDown = True 
    
    while continueDown:
      x, y = pos
      nextDown = (x, y+1)
      nextDownLeft = (x-1, y+1)
      nextDownRight = (x+1, y+1)
   
      if nextDown not in nonAir and nextDown[1] != floorY:
        pos = nextDown
      elif nextDownLeft not in nonAir and nextDownLeft[1] != floorY:
        pos = nextDownLeft
      elif nextDownRight not in nonAir and nextDownRight[1] != floorY:
        pos = nextDownRight
      else:
        nonAir.add(pos)
        sandBlocks += 1 
        continueDown = False
        
        if pos == startingPoint:
          runSimulation = False
        
  print(sandBlocks) 
      
if __name__ == '__main__':
  main()