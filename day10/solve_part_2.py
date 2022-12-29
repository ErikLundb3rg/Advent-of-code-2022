def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()
from pprint import pprint

def checkCycle(register, cycle, drawing):
  col = cycle // 40
  row = (cycle-1) - (col*40)
  if row >= register -1 and row <= register+1:
    print('cycle', cycle)
    print('col', col)
    print('row', row)
    drawing[col][row] = '#'
  
def main():
  inp = getLines('input.in')
  
  cycle = 1
  register = 1
  drawing = [['.' for _ in range(40)] for _ in range(6)]
  
  for line in inp:
    checkCycle(register, cycle, drawing)
    # check cycle 
    if line == 'noop':
      cycle += 1

    else:
      instruction, value = line.split()
      cycle += 1
      checkCycle(register, cycle, drawing)
      cycle += 1
      register += int(value)
  
  for row in drawing:
    print("".join(row)) 
if __name__ == '__main__':
  main()
  