class ElementDuplicationError(Exception):
    pass

class MyList(list):
    def append (self,item):
      if item in self:
         raise ElementDuplicationError ("Error is duplicated")
      super ().append (item)
    
try:  
  lst = MyList()
  lst.append(1)
  print(lst)

  lst.append(2)
  print(lst)

  lst.append(1)
  print(lst)

  lst.append(3)
  print(lst)
   
except ElementDuplicationError as e: 
  print(e) 