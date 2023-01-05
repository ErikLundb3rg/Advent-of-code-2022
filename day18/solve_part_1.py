def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

from collections import defaultdict

def deduct(points, line):
  x, y, z = line
  deduction = 0
  neighbors = [
    (x+1, y, z),
    (x-1, y, z),
    (x, y+1, z),
    (x, y-1, z),
    (x, y, z+1),
    (x, y, z-1),
  ] 
  
  for n in neighbors:
    if n in points:
      deduction += 1
      
  return deduction
  
def main():
  inp = getLines('input.in')
  
  points = set()
  total = 0
  
  for line in inp:
    (x, y, z) = [int(x) for x  in line.split(',')]
    points.add((x, y, z))
  
  for line in inp:
    (x, y, z) = [int(x) for x  in line.split(',')]
    total += 6 
    total -= deduct(points, (x, y, z))
   
  print(total) 
     
if __name__ == '__main__':
  main()