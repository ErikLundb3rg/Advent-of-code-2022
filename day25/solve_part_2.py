def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()
    
def main():
  lines = getLines('input.in')
  
  cals = []
  sm = 0 
  
  for line in lines:
    if line == '':
      cals.append(sm)
      sm = 0
      continue
    
    sm += int(line) 
  
    
  calsSorted = sorted(cals)  
  
  i = len(calsSorted)-1 
  total = 0
  while (i > len(calsSorted)-4):
    total += (calsSorted[i])
    i -= 1
    
  print(total)
  
if __name__ == '__main__':
  main()

  
    
    
    
  