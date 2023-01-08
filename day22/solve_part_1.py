def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

def inBounds(grid, x, y):
  return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def moveInGridWithDelta(grid, steps, pos, dX, dY):
  while steps > 0:  
    # see if i hit a wall
    x, y = pos 
    grid[y][x] = 'P'
    nextX = x+dX
    nextY = y+dY
    
    # Trace around
    if inBounds(grid, nextX, nextY) and grid[nextY][nextX] == '#':
      break
    
    
    if not inBounds(grid, nextX, nextY) or grid[nextY][nextX] == ' ':
      oX, oY = (x, y)
      nox, noy = (oX-dX, oY-dY) 
      
      while inBounds(grid, nox, noy) and not grid[noy][nox] == ' ':
        oX, oY = (nox, noy)
        nox -= dX
        noy -= dY
            
      # check for if there is a wall on the other side 
      if grid[oY][oX] == '#':
        break
            
      pos = (oX, oY)
    
    
    else:
      pos = (nextX, nextY) 
    steps -= 1
  return pos

def getAnsDirection(d):
  if d == 0:
    return d
  if d == 1:
    return 3
  if d == 2: 
    return 2
  if d == 3:
    return 1

def main():
  lines = getLines('input.in')
  grid = [] 
  start = (None, None)
  mxRow = max([len(row) for row in lines])
  for i in range(200):
    row = list(lines[i])
    if len(row) < mxRow:
      toAdd = mxRow-len(row)
      for _ in range(toAdd):
        row.append(' ')
    grid.append(row)
    
    if i == 0:
      x = 0
      while row[x] != '.':
        x += 1
      start = (x, i) 
    
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
        pos = moveInGridWithDelta(grid, instruction, pos, 1, 0)
      elif direction == 1:
        pos = moveInGridWithDelta(grid, instruction, pos, 0, -1)
      elif direction == 2:
        pos = moveInGridWithDelta(grid, instruction, pos, -1, 0)
      elif direction == 3:
          pos = moveInGridWithDelta(grid, instruction, pos, 0, 1)
    else:
      if instruction == 'L':
        direction = (direction+1)%4
      elif instruction == 'R':
        direction = 3 if direction-1 == -1 else direction-1

  grid[pos[1]][pos[0]] = 'F'
  col, row = pos 
  ansDirection = getAnsDirection(direction)
  ans = 1000*(row+1) + 4*(col+1) + ansDirection 
  print("".join(grid[0]).strip())
  print(ans)
      
      
if __name__ == '__main__':
  main()