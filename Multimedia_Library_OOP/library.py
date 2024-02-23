from items import CD, DVD, Book

class Library:
  
  # Constructor
  def __init__(self):
    self.items = [] #A list of all the items in the library 
    
  # A method to add an item to the library  
  def addItem(self,item):
    self.items.append(item)
      
  # A method to remove an item from the library  
  def removeItem(self,item):
    self.items.remove(item)
          
  # A method to view all items.
  def listItems(self,fullDescription = True):
    if fullDescription:
      print("---------------------")
      for item in self.items:
        item.viewDescription()
        print("---------------------")
    else:
      print("---------------------")
      for item in self.items:
        item.name
      print("---------------------")
      
  # A method to return the number of items in the library
  def numberOfItems(self):
    return len(self.items)
  
  # A method to empty the content of the library
  def reset(self):
    self.items = []
    
  # A method to return whether the library is empty or not:
  def isEmpty(self):
    return len(self.items)==0
    
  