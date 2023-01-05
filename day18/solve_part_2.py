def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

from collections import defaultdict

def getNeighbors(point):
  x, y, z = point
  return [
    (x+1, y, z),
    (x-1, y, z),
    (x, y+1, z),
    (x, y-1, z),
    (x, y, z+1),
    (x, y, z-1),
  ]   
  
def sides(air, point):
  count = 0
  
  for n in getNeighbors(point):
    if n in air:
      count += 1
      
  return count 

def main():
  inp = getLines('input.in')
  points = set()
  total = 0
  maximas = (0, 0, 0) 
  minimas = (10e9, 10e9, 10e9) 

  for line in inp:
    (x, y, z) = [int(x) for x  in line.split(',')]
    point = (x, y, z)
    points.add(point)
    a, b, c = maximas
    am, bm, cm = minimas 
    maximas = (max(a, x), max(y, b), max(z, c)) 
    minimas = (min(am, x), min(y, bm), min(z, cm)) 
  
  # Need to check outside maximas and minimas as otherwise a droplet point is 
  # treated as air :D 
  maximas = (1+maximas[0], 1+maximas[1], 1+maximas[2])
  minimas = (minimas[0]-1, minimas[1]-1, minimas[2]-1)
  
  q = [minimas] 
  air = set()
  
  while q:
    point = q.pop(0)
    
    for neighbor in getNeighbors(point):
      x, y, z = neighbor
      if neighbor not in points and neighbor not in air and x >= minimas[0] and x <= maximas[0] and y >= minimas[1] and y <= maximas[1] and z >= minimas[2] and z <= maximas[2]:
        air.add(neighbor)       
        q.append(neighbor) 
  
  extension = set() 
  
  for point in air:
    for neighbor in getNeighbors(point):
      extension.add(point)
      
  for point in points:
    total += sides(air, point)
 
  print(total) 
     
if __name__ == '__main__':
  main()