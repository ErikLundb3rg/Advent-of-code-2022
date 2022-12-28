def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()


def move(pos, direction):
  x, y = pos
  if direction == 'U':
    y += 1
  elif direction == 'D':
    y  -= 1
  elif direction == 'L':
    x -= 1
  elif direction == 'R':
    x += 1
  return (x, y)
 
 
def touching(head, tail):
  a, b = head
  x, y = tail 
  
  return abs(a-x) <= 1 and abs(b-y) <= 1

def main():
  lines = getLines('input.in')
  
  positions = set()
  
  tail = (0, 0)  
  head = (0, 0)
  lastHeadPos = (0, 0) 
  positions.add(tail)
  for line in lines:
    direction, times = line.split(' ')
    for _ in range(int(times)):
      head = move(head, direction)
      if not touching(head, tail):
        if tail[0] == head[0] or tail[1] == head[1]:
          tail = move(tail, direction)
          positions.add(tail)
        # move diagonally
        else:
          tail = lastHeadPos 
          positions.add(tail)
      lastHeadPos = head
      
  print(len(positions))
       
if __name__ == '__main__':
  main()