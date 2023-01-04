def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()

from collections import defaultdict

def floydMarshall(nodes):
  global neighbours, distance
  distance = defaultdict(dict)
  
  for node in nodes:
    for other in nodes:
      distance[node][other] = 10e5
      
  for node in nodes:
    distance[node][node] = 0
    for neighbour in neighbours[node]:
      distance[node][neighbour] = 1
  
  for through in nodes:
    for source in nodes: 
      for target in nodes:
        route = distance[source][through] + distance[through][target]
        if distance[source][target] > route:
          distance[source][target] = route

def dfs(node, elapsed, flow, isElephant, opened, useful):
  global neighbours, rateOfValve, interestingNodes
  mx = flow + getFlow(opened)*(26-elapsed)
  
  if not isElephant:
    newCandidates = useful.copy()
    for entry in opened:
      newCandidates.remove(entry)
    mx = flow + getFlow(opened)*(26-elapsed) + dfs('AA', 0, 0, True, set(), newCandidates)
  
  
  for nxt in useful:
    if nxt in opened:
      continue
    
    delta = distance[node][nxt]+1
    if delta + elapsed >= 26:
      continue
      
    newFlow = flow + getFlow(opened)*delta
    opened.add(nxt)
    mx = max(mx, dfs(nxt, elapsed+delta, newFlow, isElephant, opened, useful))
    opened.remove(nxt)
    
  return mx 
      
def getFlow(opened):
  global rateOfValve
  x = 0
  for o in opened:
    x += rateOfValve[o]
  return x

def main():
  inp = getLines('input.in')
  
  start = 'AA' 
  global rateOfValve, neighbours
  rateOfValve = {}
  neighbours = defaultdict(list)
  nodes = []
  for line in inp:
    idx = line.replace('Valve ', '').split(' has ')[0]
    rate = int(line.split(';')[0].split('rate=')[1])
    neighboringValves = []
    try:
      neighboringValves = line.split(' valves ')[1].split(', ')
    except:
      neighboringValves = line.split(' valve ')[1].split(', ')
    nodes.append(idx)
    rateOfValve[idx] = rate
    neighbours[idx] = neighboringValves
 
  floydMarshall(nodes) 
  
  global interestingNodes
  interestingNodes = []
  for node in nodes:
    if rateOfValve[node] > 0:
      interestingNodes.append(node)
 
  useful = set(interestingNodes) 
  print(dfs(start, 0, 0, False, set(), useful))
     
     
if __name__ == '__main__':
  main()