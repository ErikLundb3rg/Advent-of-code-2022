def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()


def matchOperand(a, b, operand):
  if operand == '*':
    return a*b
  elif operand == '/':
    return a // b 
  elif operand == '+':
    return a + b
  else: 
    return a - b
 
def getValue(mp, yeller, mustEqual = None):
  if yeller == 'humn':
    return mustEqual
  
  yelling = mp[yeller]
  try:
    val = int(yelling)
    return val
  except:
    a, operand, b = yelling.split(' ')
    aStatus, bStatus = (valueOrHumn(mp, a), valueOrHumn(mp, b))
    known = None
    unknown = None
    
    if aStatus is None:
      known = bStatus
      unknown = a
    elif bStatus is None:
      known = aStatus
      unknown = b
    else:
      return matchOperand(aStatus, bStatus, operand)
      
    if operand == '*':
      return getValue(mp, unknown, mustEqual // known)
    elif operand == '/':
      res = known * mustEqual if aStatus is None else known // mustEqual
      return getValue(mp, unknown, res)
    elif operand == '+':
      return getValue(mp, unknown, mustEqual-known)
    else: 
      res = mustEqual + known if aStatus is None else known - mustEqual
      return getValue(mp, unknown, res)
    
def willYellFromHumn(mp, yeller):
  if yeller == 'humn':
      return True
  yelling = mp[yeller]
  try:
    _ = int(yelling)
    return False
  except: 
    a, _, b = yelling.split(' ')
    return willYellFromHumn(mp, a) or willYellFromHumn(mp, b)

def valueOrHumn(mp, yeller):
  return getValue(mp, yeller) if not willYellFromHumn(mp, yeller) else None


def run(mp, root):
  yelling = mp[root]
  a, _, b = yelling.split(' ')
  if (willYellFromHumn(mp, a)):
    target = getValue(mp, b)
    return getValue(mp, a, target)
  elif (willYellFromHumn(mp, b)):
    target = getValue(mp, a)
    return getValue(mp, b, target)
  
  
def main():
  lines = getLines('input.in')
  
  mp = {}
 
  for line in lines:
    yeller, yelling = line.split(': ')
    mp[yeller] = yelling
    
  print(run(mp, 'root')) 
  
if __name__ == '__main__':
  main()