#This file is for reading and writing colors to the lights
def readColor(color):
    if color[0] == '#':
        return hexRead(color)
    file = open("colors.txt", "r")
    content = (file.read()).split("\n")
    file.close()
    print(color)
    for i in range(len(content)):
        if content[i].find(color) != -1:
            print("in")
            x,y,z = list(map(int,content[i+1].split(" ")))
            return((x,y,z))
    return 1

def Tuple(rgb):
    return '#%02x%02x%02x' % rgb
    
def addL(x):
  return x + "\n"

def hexRead(code):
        code = code.strip("#")
        code = code.strip(" ")
        col = tuple(int(code[i:i+2], 16) for i in (0, 2, 4))
        return col
def write(name,color):
  print("writing")
  file = open("colors.txt",'r')
  content = (file.read()).split("\n")
  file.close()
  t=0
  for i in range(len(content)):
    if content[i].find(name) != -1:
      x,y,z = color
      content[i+1]=str(x)+" "+str(y)+" "+str(z)
      t=1
      break
  if t == 0:
    file = open("colors.txt", "a")
    file.write(name+"\n")
     
    x,y,z = color
    file.write(str(x)+" "+str(y)+" "+str(z))
    file.write("\n")
    file.close()
  else:
    file = open("colors.txt","w")
    file.writeLines(map(addL,content))
    file.close()




