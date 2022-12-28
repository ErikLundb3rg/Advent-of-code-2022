def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

def main():
  lines = getLines('input.in')
  
  mx = 0
  
  for y in range(0, len(lines)):
    for x in range(0, len(lines[0])):
      currTree = lines[y][x]
     
      down = 0
      col = y-1
      while col >= 0: 
        down += 1
        if lines[col][x] >= currTree:
          break
        col -= 1
     
      top = 0
      col = y+1
      while col < len(lines): 
        top += 1
        if lines[col][x] >= currTree:
          break
        col += 1
      
      left = 0
      row = x-1 
      while row >= 0:
        left += 1
        if lines[y][row] >= currTree:
          break
        row -= 1
      
      right = 0
      row = x+1
      while row < len(lines[0]):
        right +=1 
        if lines[y][row] >= currTree:
          break
        row += 1
      
      scenicScore = down*top*left*right 
      mx = max(mx, scenicScore) 
        
  print(mx)

if __name__ == '__main__':
  main()