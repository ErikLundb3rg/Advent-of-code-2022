def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()


class Monkey:
  def __init__(self, id, startingItems, testDivisibleBy, trueMonkey, falseMonkey):
    self.id = id 
    self.items = startingItems
    self.testDivisibleBy = testDivisibleBy
    self.trueMonkey = trueMonkey
    self.falseMonkey = falseMonkey
    self.activityLvl = 0
  
  def run(self, monkeys):
    for item in self.items:
      lvl = self.operate(item) // 3
      if lvl % self.testDivisibleBy == 0:
        monkeys[self.trueMonkey].addItem(lvl)
      else:
        monkeys[self.falseMonkey].addItem(lvl)
    self.activityLvl += len(self.items)
    self.items = []
         
  def addItem(self, item):
    self.items.append(item)
    
  def operate(self, number):
    if self.id == 0:
      return number*13
    elif self.id == 1:
      return number+7
    elif self.id == 2:
      return number+2
    elif self.id == 3:
      return number*2
    elif self.id == 4:
      return number**2
    elif self.id == 5:
      return number+6
    elif self.id == 6:
      return number+1
    elif self.id == 7:
      return number+8
  
def main():
  inp = getLines('input.in')
  

  i = 0 
  monkeys = []
  
  while i < len(inp):
    monkeyNumber = int(inp[i].replace('Monkey ', '').replace(':', ''))
    items = [int(x) for x in (inp[i+1]).strip().replace('Starting items: ', '').split(',')]
    operation = inp[i+2].strip().replace('Operation: new = old ', '')
    divisibleBy = int(inp[i+3].strip().replace('Test: divisible by ', ''))
    trueMonkey = int(inp[i+4].strip().replace('If true: throw to monkey ', ''))
    falseMonkey = int(inp[i+5].strip().replace('If false: throw to monkey ', ''))
    monkeys.append(Monkey(monkeyNumber, items, divisibleBy, trueMonkey, falseMonkey))
    i+= 7
    
  
  for roundId in range(20):
    print('round ', roundId)
    for monkey in monkeys:
      monkey.run(monkeys)
  
  monkeys.sort(key = lambda x : x.activityLvl)
  res = monkeys[-1].activityLvl * monkeys[-2].activityLvl
  print(res)
  
     
      
if __name__ == '__main__':
  main()