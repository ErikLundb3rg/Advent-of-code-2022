def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

def contains(a, b, c, d):
  return c <= a and d >= b

def main():
  line = getLines('input.in')[0]

  for i in range(len(line)):
    same = True 
    for j in range(i, i+4):
      character = line[j] 
      for k in range(i, i+4):
        if k != j and line[k] == character:
          same = False
    
    if same: 
      print(i+4)
      return
   
if __name__ == '__main__':
  main()