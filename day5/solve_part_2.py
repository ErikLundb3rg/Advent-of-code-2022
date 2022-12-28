def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

def contains(a, b, c, d):
  return c <= a and d >= b

def main():
  lines = getLines('input.in')
  crates = [
    ['S', 'C', 'V', 'N'],
    ['Z', 'M', 'J', 'H', 'N', 'S'],
    ['M', 'C', 'T', 'G', 'J', 'N', 'D'],
    ['T', 'D', 'F', 'J', 'W', 'R', 'M'],
    ['P', 'F', 'H'],
    ['C', 'T', 'Z', 'H', 'J'],
    ['D', 'P', 'R', 'Q', 'F', 'S', 'L', 'Z'],
    ['C', 'S', 'L', 'H', 'D', 'F', 'P', 'W'],
    ['D', 'S', 'M', 'P', 'F', 'N', 'G', 'Z'],
  ]
  
  
  for i in range(len(lines)):
    if i >= 10:
      part = lines[i].split(' from ')
      amount = int(part[0].split('move ')[1])
      frm, to = map(int, part[1].split(' to ')) 
      frm -= 1 
      to -= 1
     
      toMove = [] 
      for _ in range(amount):
        toMove.append(crates[frm].pop())
        
      toMove.reverse()
      for move in toMove:
        crates[to].append(move)

  res = [] 
  for crate in crates:
    res.append(crate[-1])
    
  print("".join(res))
       
if __name__ == '__main__':
  main()