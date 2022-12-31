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
  
  smaller6 = 0
  smaller2 = 0
  for i in range(len(inp)) :
    if len(inp[i]) == 0:
      continue
    curr = json.loads(inp[i])
    if compareLists(curr, [[2]]) == 1:
      smaller2 += 1
    if compareLists(curr, [[6]]) == 1:
      smaller6 += 1
  
  smaller2 += 1
  smaller6 += 2
  answer = smaller2 * smaller6
  print(answer)
      
if __name__ == '__main__':
  main()