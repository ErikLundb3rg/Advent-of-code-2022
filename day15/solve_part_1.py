def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

def main():
  inp = getLines('input.in')
  interestingY = 2000000 
  xPoints = set()
  beacons = []
  
  for line in inp:
    xS, yS, xB, yB = [int(x.strip().split('=')[1]) for x in line.replace('Sensor at ', '').replace(': closest beacon is at ', ',').split(',')]
    beacons.append((xB, yB)) 
    distance = abs(xS - xB) + abs(yS - yB)
    distanceToInterestingY = abs(interestingY - yS)
    
    if distanceToInterestingY < distance:
      deltaX = distance - distanceToInterestingY
      for x in range(xS - deltaX, xS + deltaX+1):
        xPoints.add(x)

  for beacon in beacons:
    x, y = beacon
    if y == interestingY:
      if x in xPoints:
        xPoints.remove(x)
      
  print(len(xPoints))      
     
if __name__ == '__main__':
  main()