def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

import json

def compareLists(left, right):
  isLeftInt = isinstance(left, int) 
  isRightInt = isinstance(right, int) 
  
  if isLeftInt and isRightInt: 
    if left < right:
      return 1
    elif left > right: 
      return -1 
    else:
      return 0
  if isLeftInt:
    left = [left]
  if isRightInt:
    right = [right]
 
  iterationLength = max(len(left), len(right)) 
  for i in range(iterationLength):
    if i == len(left) and i < len(right):
      return 1
    elif i < len(left) and i == len(right):
      return -1
    itemLeft = left[i]
    itemRight = right[i]
    
    res = compareLists(itemLeft, itemRight)
    if res != 0:
      return res
  return 0
    
def main():
  inp = getLines('input.in')
  
  i = 0
  answer = 0
  currentPair = 1
  while i < len(inp):
    left, right = map(json.loads, [inp[i], inp[i+1]])
    
    res = compareLists(left, right) 
    if res == 1:
      answer += currentPair
    i += 3
    currentPair += 1
  
  print(answer)
      
if __name__ == '__main__':
  main()