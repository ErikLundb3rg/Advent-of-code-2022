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
  
  snake = [(0, 0) for _ in range(10)]
  positions.add((0, 0))
  
  for line in lines:
    direction, times = line.split(' ')
    for _ in range(int(times)):
      snake[0] = move(snake[0], direction)
      for i in range(1, len(snake)):
        tail = snake[i]
        head = snake[i-1]
       
        if not touching(head, tail):
          if tail[0] == head[0]:
            if tail[1] > head[1]:
              snake[i] = (snake[i][0], snake[i][1]-1)
            if tail[1] < head[1]:
              snake[i] = (snake[i][0], snake[i][1]+1)
          elif tail[1] == head[1]:
            if tail[0] > head[0]:
              snake[i] = (snake[i][0]-1, snake[i][1])
            if tail[0] < head[0]:
              snake[i] = (snake[i][0]+1, snake[i][1])
          # move diagonally
          else:
            if head[1] > snake[i][1]:
              snake[i] = move(snake[i], 'U')
            if head[1] < snake[i][1]:
              snake[i] = move(snake[i], 'D')
            if head[0] > snake[i][0]:
              snake[i] = move(snake[i], 'R')
            if head[0] < snake[i][0]:
              snake[i] = move(snake[i], 'L')
              
        positions.add(snake[-1])
  print(len(positions))
       
if __name__ == '__main__':
  main()