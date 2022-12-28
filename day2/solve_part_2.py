def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()
   
def main():
  lines = getLines('input.in')
  
  
  winner = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
  } 
  
  loser = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
  }
  
  score = {
    'A': 1,
    'B': 2,
    'C': 3,
  }
 
  optionScore = {
    'X': 1,
    'Y': 2,
    'Z': 3,
  }
 
  total = 0 
  for line in lines: 
    inp, response = line.split()
    
    
    if response == 'X':
      total += score[loser[inp]]
    elif response == 'Z':
      total += 6
      total += score[winner[inp]]
    else: 
      total += 3
      total += score[inp]
    
  print(total)
  
if __name__ == '__main__':
  main()