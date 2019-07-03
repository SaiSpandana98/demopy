import operator

def createTupledList() :
    l=[]
    while True:
      t=tuple()
      print("Add an element for the tuple ? y/n : ")
      if input()!='y':
        break
      else:
        print("Keep adding the tuple elements : (x to break)")
        while True:
          i=input()
          if i=='x':
            break
          else:
            t+=(i,)
          print(t)
        l.append(t)
    return l

l2=createTupledList()
print(l2)


l2.sort(key = operator.itemgetter(-1))
print(l2)
