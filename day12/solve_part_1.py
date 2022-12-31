def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

def height(entry, grid):
  x, y = entry
  return ord(grid[y][x])
 
def inBounds(entry, grid):
  height = len(grid)
  width = len(grid[0])
  x, y = entry
  return x >= 0 and x < width and y >= 0 and y < height

def getNeighbours(entry, grid):
  x, y = entry
  h = height(entry, grid)
  neighbours = [] 
  up = (x, y+1)
  down = (x, y-1)
  right = (x+1, y)
  left = (x-1, y)
  if inBounds(up, grid) and height(up, grid) - h <= 1:
    neighbours.append(up)
  if inBounds(down, grid) and height(down, grid) - h <= 1:
    neighbours.append(down)
  if inBounds(right, grid) and height(right, grid) - h <= 1:
    neighbours.append(right)
  if inBounds(left, grid) and height(left, grid) - h <= 1:
    neighbours.append(left)
  return neighbours

def bfs(source, target, grid):
  steps = 0
  if source == target:
    return steps 
  
  q = [source]
  visited = set()
  visited.add(source)
  distance = {}
  distance[source] = steps
 
  while q:
    entry = q.pop(0) 
    steps += 1
    for neighbor in getNeighbours(entry, grid):
      if neighbor not in visited:
        if neighbor == target:
          return distance[entry] +1
        visited.add(neighbor)
        q.append(neighbor)
        distance[neighbor] = 1 + distance[entry]
  
  return -1
  
def main():
  inp = getLines('input.in')
 
  source = (-1, -1) 
  target = (-1, -1)
  for y in range(len(inp)):
    for x in range(len(inp[0])):
      if inp[y][x] == 'S':
        source = (x, y)
        tmp = list(inp[y])
        tmp[x] = 'a'
        inp[y] = "".join(tmp)
      elif inp[y][x] == 'E':
        target = (x, y)
        tmp = list(inp[y])
        tmp[x] = 'z'
        inp[y] = "".join(tmp)
    
  res = bfs(source, target, inp)
  print(res)
   
      
if __name__ == '__main__':
  main()