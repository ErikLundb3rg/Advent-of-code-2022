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
    
  print(max(cals))
  
if __name__ == '__main__':
  main()