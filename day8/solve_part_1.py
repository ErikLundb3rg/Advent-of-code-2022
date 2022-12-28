def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

def main():
  lines = getLines('input.in')
  
  total = 0
  
  total += len(lines)*2 + len(lines[0]*2) - 4
  for y in range(1, len(lines)-1):
    for x in range(1, len(lines[0])-1):
      currTree = lines[y][x]
      isVisible = False
      
      visible = True 
      for col in range(0, y):
        if lines[col][x] >= currTree:
          visible = False
      isVisible = isVisible or visible
      
      visible = True    
      for col in range(y+1, len(lines)):
        if lines[col][x] >= currTree:
          visible = False
      isVisible = isVisible or visible
        
      visible = True 
      for row in range(0, x):
        if lines[y][row] >= currTree:
          visible = False
      isVisible = isVisible or visible
          
      visible = True 
      for row in range(x+1, len(lines[0])):
        if lines[y][row] >= currTree:
          visible = False
      isVisible = isVisible or visible

      if isVisible:
        total += 1
        
  print(total)

if __name__ == '__main__':
  main()