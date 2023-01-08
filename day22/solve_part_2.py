def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

def inBounds(grid, x, y):
  return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

class Side():
  def __init__(self, num):
    self.num = num
    self.points = set()
    self.bottom = []
    self.top = []
    self.left = []
    self.right = []
    
  def contains(self, pos):
    x, y = pos
    left = self.left[0][0]
    right = self.right[0][0]
    top = self.top[0][1]
    bottom = self.bottom[0][1]
    
    return x >= left and x <= right and y <= bottom and y >= top
  
  def relativeCoords(self, pos):
    x, y = pos
    return (x - self.left[0][0], y - self.left[0][1])

  def getCoordsFromRelative(self, relPos):
    rX, rY = relPos
    return (rX+self.left[0][0], rY+self.left[0][1])
  
    
def moveInGridWithDelta(grid, steps, pos, dX, dY):
  while steps > 0:  
    x, y = pos 
    grid[y][x] = 'P'
    nextX = x+dX
    nextY = y+dY
    
    # see if i hit a wall
    if inBounds(grid, nextX, nextY) and grid[nextY][nextX] == '#':
      break
   
    # trace around
    if not inBounds(grid, nextX, nextY) or grid[nextY][nextX] == ' ':
      (nextX, nextY), newDelta = getWrappingPos(pos, (dX, dY))
      # check for if there is a wall on the other side 
      if grid[nextY][nextX] == '#':
        break
      
      dX = newDelta[0]
      dY = newDelta[1]
            
      
            
      pos = (nextX, nextY)
    else:
      pos = (nextX, nextY) 
    steps -= 1
    
  return pos, (dX, dY)

def getAnsDirection(d):
  if d == 0:
    return d
  if d == 1:
    return 3
  if d == 2: 
    return 2
  if d == 3:
    return 1

# shoot me
def getWrappingPos(pos, delta):
  global mp, sides 
  currSide = None 
  for side in sides:
    if side.contains(pos):
      currSide = side
      break
  rX, rY = currSide.relativeCoords(pos)
  if currSide.num == 1:
    if delta == (0, 1):
      newrX = rX
      return mp[3].top[newrX], delta
    if delta == (-1, 0):
      newrY = 49 - rY
      return mp[4].left[newrY], (1, 0)
    if delta == (1, 0):
      newrY = rY
      return mp[2].left[newrY], delta
    if delta == (0, -1):
      newrY = rX
      return mp[6].left[newrY], (1, 0)
  if currSide.num == 2:
    if delta == (0, 1):
      newrY = rX
      return mp[3].right[newrY], (-1, 0)
    if delta == (-1, 0):
      newrY = rY
      return mp[1].right[newrY], delta
    if delta == (1, 0):
      newrY = 49 - rY
      return mp[5].right[newrY], (-1, 0)
    if delta == (0, -1):
      newrX = rX
      return mp[6].bottom[newrX], delta
  if currSide.num == 3:
    if delta == (0, 1):
      newrX = rX
      return mp[5].top[newrX], delta
    if delta == (-1, 0):
      newrX = rY
      return mp[4].top[newrX], (0, 1)
    if delta == (1, 0):
      newX = rY
      return mp[2].bottom[newX], (0, -1)
    if delta == (0, -1):
      newrX = rX
      return mp[1].bottom[newrX], delta
  if currSide.num == 4:
    if delta == (0, 1):
      newrX = rX
      return mp[6].top[newrX], delta
    if delta == (-1, 0):
      newrY = 49 - rY
      return mp[1].left[newrY], (1, 0)
    if delta == (1, 0):
      newrY = rY
      return mp[5].left[newrY], delta
    if delta == (0, -1):
      newrY = rX
      return mp[3].left[newrY], (1, 0)
  if currSide.num == 5:
    if delta == (0, 1):
      newrY = rX 
      return mp[6].right[newrY], (-1, 0)
    if delta == (-1, 0):
      newrY = rY
      return mp[4].right[newrY], delta
    if delta == (1, 0):
      newrY = 49 - rY
      return mp[2].right[newrY], (-1, 0)
    if delta == (0, -1):
      newrX = rX
      return mp[3].bottom[newrX], delta
  if currSide.num == 6:
    if delta == (0, 1):
      newrX = rX
      return mp[2].top[newrX], delta
    if delta == (-1, 0):
      newrX = rY
      return mp[1].top[newrX], (0, 1)
    if delta == (1, 0):
      newrX = rY
      return mp[5].bottom[newrX], (0, -1)
    if delta == (0, -1):
      newrX = rX
      return mp[4].bottom[newrX], delta
  else:
    print('error')
  
def findSide(x, y, SIDE_SZ, num):
  s = Side(num)
  s.top = [(x+delta, y) for delta in range(SIDE_SZ)]
  s.bottom = [(x+delta, y+(SIDE_SZ-1)) for delta in range(SIDE_SZ)]
  s.left = [(x, y+delta) for delta in range(SIDE_SZ)]
  s.right = [(x+(SIDE_SZ-1), y+delta) for delta in range(SIDE_SZ)]
  return s
  
def matchDelta(delta):
  if delta == (1, 0):
    return 0
  if delta == (-1, 0):
    return 2
  if delta == (0, 1):
    return 3
  return  1
def main():
  lines = getLines('input.in')
  grid = [] 
  start = (None, None)
  mxRow = max([len(row) for row in lines])
  global mp, sides
  
  prevRowSz = -1
  SIDE_SZ = 50
  sides = []
  for i in range(200):
    row = list(lines[i])
    
    x = 0
    while row[x] == ' ':
      x += 1
    whitespace = x 
    if (len(row)-whitespace) != prevRowSz:
      times = (len(row)-x) // SIDE_SZ 
      for _ in range(times):
        s = findSide(x, i, SIDE_SZ, len(sides)+1)
        sides.append(s)
        x += SIDE_SZ
    
    prevRowSz = len(row)-whitespace
    
    if len(row) < mxRow:
      toAdd = mxRow-len(row)
      for _ in range(toAdd):
        row.append(' ')
        
    if i == 0:
      x = 0
      while row[x] != '.':
        x += 1
      start = (x, i) 
    grid.append(row)
   
  mp = {}
  for s in sides:
    mp[s.num] = s 
  xs = lines[201]
  instructions = []
  num = []
  for x in xs:
    if x.isnumeric():
      num.append(x)
    else:
      instructions.append(int("".join(num)))
      num = []
      instructions.append(x)
  if num:
    instructions.append(int("".join(num))) 
   
  pos = start 
  direction = 0 
  for instruction in instructions:
    if type(instruction) == int:
      if direction == 0:
        pos, delta = moveInGridWithDelta(grid, instruction, pos, 1, 0)
        direction = matchDelta(delta) 
      elif direction == 1:
        pos, delta = moveInGridWithDelta(grid, instruction, pos, 0, -1)
        direction = matchDelta(delta) 
      elif direction == 2:
        pos, delta = moveInGridWithDelta(grid, instruction, pos, -1, 0)
        direction = matchDelta(delta) 
      elif direction == 3:
        pos, delta = moveInGridWithDelta(grid, instruction, pos, 0, 1)
        direction = matchDelta(delta) 
    else:
      if instruction == 'L':
        direction = (direction+1)%4
      elif instruction == 'R':
        direction = 3 if direction-1 == -1 else direction-1

  grid[pos[1]][pos[0]] = 'F'
  
  
  
  f = open('output.out', 'w')
  
  col, row = pos 
  ansDirection = getAnsDirection(direction)
  ans = 1000*(row+1) + 4*(col+1) + ansDirection 
  print(ans)
      
      
if __name__ == '__main__':
  main()