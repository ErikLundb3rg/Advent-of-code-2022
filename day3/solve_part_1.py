def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()


def main():
  lines = getLines('input.in')


  total = 0
  for line in lines:
    firstHalf = [line[i] for i in range(len(line)//2)]
    secondHalf = [line[i] for i in range(len(line)//2, len(line))]

    shared = []
    for item in firstHalf:
      if item in secondHalf:
        toAdd = ord(item)-38 if item.isupper() else ord(item)-96
        total += toAdd
        break
  print(total)
        
        
   
  
if __name__ == '__main__':
  main()