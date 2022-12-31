def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()


def inBounds(x, y):
  return x >= 0 and x <= 4000000 and y >= 0 and y <= 4000000


def checkPoint(x, y, sensors, current):
  for sensor in sensors:
    xO, yO, distOther = sensor
    if sensor != current:
      if abs(x-xO) + abs(y-yO) <= distOther:
        return False
  
  return True
def main():
  inp = getLines('input.in')
  sensors = []
  
  for line in inp:
    xS, yS, xB, yB = [int(x.strip().split('=')[1]) for x in line.replace('Sensor at ', '').replace(': closest beacon is at ', ',').split(',')]
    distance = abs(xS - xB) + abs(yS - yB)
    sensors.append((xS, yS, distance))
    
  mx = 4000000
  
  for sensor in sensors: 
    print(sensor)
    x, y, distance = sensor 
    
    beyondRim = distance+1
    
    for xR in range(max(0, x-beyondRim), min(x+beyondRim+1, mx)):
      yDelta = beyondRim - abs(xR-x)
      yPos = y+yDelta
      yNeg = y-yDelta
      
      if yPos >= 0 and yPos <= mx and checkPoint(xR, yPos, sensors, sensor):
        print('Point is: ', xR, yPos) 
        print('Answer:  ', xR*mx + yNeg)
        return
      if yNeg >= 0 and yNeg <= mx and checkPoint(xR, yNeg, sensors, sensor):
        print('Point is ', xR, yNeg)
        print('Answer:  ', xR*mx + yNeg)
        return  
if __name__ == '__main__':
  main()