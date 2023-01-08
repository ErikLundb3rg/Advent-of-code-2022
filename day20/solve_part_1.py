def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()
  
class Node:
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right


def main():
  numbers = [int(x) for x in getLines('input.in')]
 
  nodes = []
  for num in numbers:
    nodes.append(Node(num))
    
  modRef = len(nodes)-1
    
  for i in range(len(nodes)):
    nodes[i].right = nodes[(i+1)%len(nodes)]
    nodes[i].left = nodes[(i-1)%len(nodes)]
 
  zero = -1 
  for node in nodes:
    if node.value == 0:
      zero = node 
      continue
      
    if node.value > 0:
      times = node.value % modRef
      curr = node
      for _ in range(times):
        curr = curr.right
      if curr == node:
        continue
      
      node.right.left = node.left
      node.left.right = node.right
      curr.right.left = node
      node.right = curr.right
      curr.right = node
      node.left = curr
    else:
      times = -node.value % modRef
      curr = node
      for _ in range(times):
        curr = curr.left
        
      if curr == node:
        continue
      
      node.right.left = node.left 
      node.left.right = node.right
      curr.left.right = node
      node.left = curr.left
      curr.left = node
      node.right = curr

  ans = 0
  for i in range(3):
    for _ in range(1000):
      zero = zero.right
    ans += zero.value 
  print(ans)

       
     
    
 

        
         
    
  
if __name__ == '__main__':
  main()






