def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

from collections import defaultdict


def addShape():
  global directions, shapes, points, nrOfStackedShapes, currentShapeIndex, directionIndex, heightOffset, tallestPoint, actualHeight
  shape = shapes[currentShapeIndex]
   
  # let shape start at y+heightOffset
  increaseInY = abs(min(y for _, y in shape)) +heightOffset
  shape = [(x, y+increaseInY) for (x, y) in shape]
   
  stuck = False 
  placedShapeIndex = currentShapeIndex
  while not stuck:
    increase = 1 if directions[directionIndex] == '>' else -1
      
    canMoveHorizontally = True 
    for (x, y) in shape:
      if x+increase == 7 or x+increase == -1 or (x+increase, y) in points:
        canMoveHorizontally = False
        break
          
    if canMoveHorizontally:
      shape = [(x+increase, y) for (x, y) in shape]
      
    directionIndex = (directionIndex+1) % len(directions)
    canMoveVertically = True
    for (x, y) in shape:
      if (x, y-1) in points:
        canMoveVertically = False
          
    if canMoveVertically:
      shape = [(x, y-1) for (x, y) in shape] 
    else:
      for point in shape:
        points.add(point) 
      tallestPoint = max(tallestPoint, max([y for (_, y) in shape]))
      
      stuck = True 
      heightOffset = 4+tallestPoint
  nrOfStackedShapes += 1 
  currentShapeIndex = (currentShapeIndex+1) % len(shapes)
  return placedShapeIndex
    
def getSkyline():
  global points, tallestPoint
  num = 0 
  for x in range(7):
    for y in range(3):
      pX, pY = (x, tallestPoint-y)
      if (pX, pY) in points:
        num = num | (1<<(pX+(y*7))) 
  
  return num
      
def signature(R):
  maxY = max([y for (_,y) in R])
  return frozenset([(x,maxY-y) for (x,y) in R if maxY-y<=30])
    
def main():
  inp = getLines('input.in')
  global directions, shapes, points, nrOfStackedShapes, currentShapeIndex, directionIndex, heightOffset, tallestPoint, actualHeight
  
  directions = inp[0]
 
  xS = 2
  yS = 0
  shapes = [
    [
      (xS, yS), (xS+1, yS), (xS+2, yS), (xS+3, yS)
    ],
    [
      (xS+1, yS), (xS, yS-1), (xS+1, yS-1), (xS+2, yS-1), (xS+1, yS-2)
    ],
    [
      (xS+2, yS), (xS+2, yS-1), (xS, yS-2), (xS+1, yS-2), (xS+2, yS-2)
    ],
    [
      (xS, yS), (xS, yS-1), (xS, yS-2), (xS, yS-3)
    ],
    [
      (xS, yS), (xS+1, yS), (xS, yS-1), (xS+1, yS-1)
    ]
  ]
  
  points = set([(i, 0) for i in range(7)])
  
  nrOfStackedShapes = 0 
  currentShapeIndex = 0
  directionIndex = 0
    
  tallestPoint = 0
  heightOffset = 4
  actualHeight = 0
 
  mp = {}
 
 
  total_rocks = int(1e12) 
  addedRocks = 0 

  while addedRocks < total_rocks:
    shape = addShape()
    
    addedRocks += 1
    
    state = (signature(points), shape, directionIndex)
    if state in mp:
      (prevRocks, prevHeight) = mp[state]
      between = addedRocks - prevRocks
      repetitions = (total_rocks - addedRocks) // between
      actualHeight += repetitions*(tallestPoint-prevHeight)
      addedRocks += between*(repetitions)
      print('addedrocks', addedRocks)
      mp = {}
      continue
      
    mp[state] = (addedRocks, tallestPoint)
      
  print(actualHeight+tallestPoint)
    
     
if __name__ == '__main__':
  main()