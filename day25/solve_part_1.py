def getLines(fileName):
 with open(fileName) as f:
    return f.read().splitlines()
  
def decimalFromSNAFU(row):
  mp = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    "=": -2
  }
  
  sm = 0
  for power in range(len(row)):
    sign = row[power]
    sm += mp[sign]* (5**power) 
  return sm 

def toSNAFU(num):
  e = 1
  sm = 0 
  while e*2 + sm < num:
    sm += e
    e *= 5
  
  ans = ''
  while e != 0 or sm != 0:
    cap = sm*2
    if 2*e - cap <= num:
      ans += '2'
      num -= 2*e
    elif e - cap <= num:
      ans += '1'
      num -= e
    elif -cap <= num:
      ans += '0'
    elif -e -cap <= num:
      ans += '-'
      num += e
    elif -2*e -cap <= num:
      ans += '='
      num += 2*e
    e = e // 5
    if sm != 0:
      sm -= e
  return ans
  
 
def main():
  lines = getLines('input.in')
  sm = 0 
  
  for line in lines:
    sm += decimalFromSNAFU(line[::-1])
 
  print('sum', sm) 
  print(toSNAFU(sm)) 
if __name__ == '__main__':
  main()