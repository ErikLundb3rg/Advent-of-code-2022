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

def dfs(node, minutes, flow, visited):
  if minutes == 0:
    return flow
  
  global neighbours, rateOfValve, interestingNodes
  mx = flow + (30-minutes)*rateOfValve[node]
  print(interestingNodes)
  print('hi')
  for valve in interestingNodes:
    if valve in visited:
      continue
    
    time = distance[node][valve]+1
    if time + minutes > 30:
      continue
      
    newFlow = flow + rateOfValve[valve]*time
    copy = visited.copy()
    copy.add(node)
    mx = max(mx, dfs(valve, minutes-1, newFlow,copy))
  return mx 
      
  
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
  
  print(dfs(start, 0, 0, set()))
     
     
if __name__ == '__main__':
  main()