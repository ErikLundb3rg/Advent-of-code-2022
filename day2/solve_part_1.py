def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()
   
def main():
  lines = getLines('input.in')
  
  possibilities = {
    'A X': 3,
    'B X': 0,
    'C X': 6,
    'A Y': 6,
    'B Y': 3,
    'C Y': 0,
    'A Z': 0,
    'B Z': 6,
    'C Z': 3,
  }
  
  optionScore = {
    'X': 1,
    'Y': 2,
    'Z': 3,
  }
 
  score = 0  
  for line in lines:
    score += possibilities[line]
    dontCare, option = line.split()
    score += optionScore[option]
    
  print(score)
  
if __name__ == '__main__':
  main()