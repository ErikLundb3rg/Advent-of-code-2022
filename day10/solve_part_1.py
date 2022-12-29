def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()


def checkCycle(register, cycle, interestingCycles, values):
  if cycle in interestingCycles:
    values.append(cycle*register)
def main():
  inp = getLines('input.in')
  
  cycle = 1
  register = 1
  interestingCycles = set([20, 60, 100, 140, 180, 220])
  interestingValues = []
  
  for line in inp:
    # check cycle 
    checkCycle(register, cycle, interestingCycles, interestingValues)
    if line == 'noop':
      cycle += 1

    else:
      instruction, value = line.split()
      cycle += 1
      checkCycle(register, cycle, interestingCycles, interestingValues)
      cycle += 1
      register += int(value)
  
  print(cycle)
  print(sum(interestingValues))
      
      
if __name__ == '__main__':
  main()