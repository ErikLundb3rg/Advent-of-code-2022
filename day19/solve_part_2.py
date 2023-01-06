from collections import defaultdict

def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

class Cost:
  def __init__(self, ore = 0, clay = 0, obsidian = 0) -> None:
    self.costArr = [ore, clay, obsidian]
  
  def canBuild(self, stat):
    return stat['ore'] >= self.ore and stat['clay'] >= self.clay and stat['obsidian'] >= self.obsidian
  
  def build(self, stat) :
    for i in range(len(self.costArr)):
      stat[i] -= self.costArr[i]
      
def hash(stat, machines, elapsed):
    return tuple([elapsed, *stat, *machines]) 
  
nameToIndex = {
  'ore': 0,
  'clay': 1,
  'obsidian': 2,
  'geode': 3,
}
    
def simulate(robotCosts, maxSpend, cache, time, bots, stats):
  if time == 0:
    return stats[3]
  
  h = hash(stats, bots, time)  
  if h in cache:
    return cache[h]
  
  mx = stats[3] + bots[3]*(time)
  
  for kind, cost in robotCosts.items():
    idx = nameToIndex[kind]
    if idx != 3 and bots[idx] >= maxSpend[idx]:
      continue
    
    waiting = 0 
    for ingredient, amount in enumerate(cost.costArr):
      if bots[ingredient] == 0 and amount > 0:
        break
      if bots[ingredient] != 0:
        waiting = max(waiting, -(-(amount-stats[ingredient]) // bots[ingredient]))
    else:
      remainingTime = time-waiting-1
      if remainingTime <= 0:
        continue
    
      botsCpy = bots.copy()
      statCpy = [x + y*(waiting+1) for x, y in zip(stats, bots)] 
      cost.build(statCpy)
      botsCpy[idx] += 1
    
      for i in range(3):
        statCpy[i] = min(statCpy[i], maxSpend[i] * remainingTime)
      mx = max(mx, simulate(robotCosts, maxSpend, cache, remainingTime, botsCpy, statCpy))
  
  cache[h] = mx
  return mx

lines = getLines('input.in')
  
 
total = 1
for num in range(3):
  line = lines[num]
  # maps 
  robotCosts = {
    'ore': Cost(ore = int(line.split('ore robot costs ')[1].split()[0])),
    'clay': Cost(ore = int(line.split('clay robot costs ')[1].split()[0])),
    'obsidian': Cost(ore = int(line.split('obsidian robot costs ')[1].split()[0]), clay = int(line.split(' clay. Each geode')[0].split()[-1])),
    'geode': Cost(ore = int(line.split('geode robot costs ')[1].split()[0]), obsidian = int(line.replace(' obsidian.', '').split()[-1])),
  }
    
  maxSpend = [
    max([x.costArr[0] for x in robotCosts.values()]),
    max([x.costArr[1] for x in robotCosts.values()]),
    max([x.costArr[2] for x in robotCosts.values()])
  ]
  
  res = simulate(robotCosts, maxSpend, {}, 32, [1, 0, 0, 0], [0, 0, 0, 0])
  total *= res

print(total)