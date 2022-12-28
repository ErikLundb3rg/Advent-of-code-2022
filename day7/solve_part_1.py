class File: 
  def __init__(self):
    self.size = 0
    self.name = None
  
  def setName(self, name):
    self.name = name

  def setSize(self, size):
    self.size = size 
    
    
class Directory:
  def __init__(self, name):
    self.name = name 
    self.dirs = {}
    self.files = {}
    self.parent = None
    
  def addFile(self, file):
    self.files[file.name] = file
  
  def addDir(self, dir):
    self.dirs[dir.name] = dir
    dir.parent = self
   
  def getSize(self):
    sm = 0
    for file in self.files.values(): 
      sm += file.size
    for dir in self.dirs.values(): 
      sm += dir.getSize()
    return sm 

  def getSubDirs(self, allDirs):
    allDirs.append(self)
    for dir in self.dirs.values():
      dir.getSubDirs(allDirs)
    
      

def getLines(fileName):
   with open(fileName) as f:
    return f.read().splitlines()
  
def main():
  lines = getLines('input.in')
  
  i = 0
 
  currDir = None 
  while i < len(lines):
    line = lines[i]
    print(i, line)
    if line[0] == '$':
      if line[2] == 'c' and line[3] == 'd':
        dirName = line.split('cd ')[1]
        
        if currDir is None:
          currDir = Directory(dirName)
        elif dirName == '..':
          currDir = currDir.parent
        else:
          currDir = currDir.dirs[dirName]
        i+=1
      else:
        j = i+1 
        currLine = lines[j]
        
        while currLine[0] != '$' and j < len(lines):
          if currLine.startswith('dir'):
            dirName = currLine.split('dir ')[1]
            if not dirName in currDir.dirs:
              currDir.addDir(Directory(dirName))
          else:
            size, name = currLine.split(" ")
            if not name in currDir.files: 
              newFile = File() 
              newFile.setName(name)
              newFile.setSize(int(size))
              currDir.addFile(newFile)
          j+=1
          if j < len(lines):
            currLine = lines[j]
        i = j
        
            
  greatestParent = currDir 
  
  while greatestParent.parent is not None:
    greatestParent = greatestParent.parent
  
  total = 0  
  arr = []
  greatestParent.getSubDirs(arr)
  for dir in arr:
    am = dir.getSize()
    if am < 100000:
      total += am
  
  print(total) 
   
if __name__ == '__main__':
  main()