def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()
  
  
def getValue(mp, yeller):
  yelling = mp[yeller]
  try:
    val = int(yelling)
    return val
  except:
    a, operand, b = yelling.split(' ')
    aVal, bVal = (getValue(mp, a), getValue(mp, b))
    
    if operand == '*':
      return aVal * bVal
    elif operand == '/':
      return aVal // bVal
    elif operand == '+':
      return aVal + bVal
    else: 
      return aVal - bVal
    
def main():
  lines = getLines('input.in')
  
  mp = {}
 
  for line in lines:
    yeller, yelling = line.split(': ')
    mp[yeller] = yelling
    
  print(getValue(mp, 'root')) 
  
if __name__ == '__main__':
  main()