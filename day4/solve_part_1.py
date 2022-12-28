def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

def contains(a, b, c, d):
  return c <= a and d >= b

def main():
  lines = getLines('input.in')

  total = 0
  
  
  for line in lines: 
    arr = line.split(",")
    a, b = map(int, arr[0].split("-"))
    x, y = map(int, arr[1].split("-"))
    
    if contains(a, b, x, y) or contains(x, y, a, b):
      total += 1
    
  print(total)
       
if __name__ == '__main__':
  main()