class Item:
  # Constructor
  def __init__(self,title,description):
    self.title = title
    self.description = description
    
  #Abstract Method to be immplemented in child classes (over-riding polymorphism) 
  def viewDescription(self):  
    return
    
class DVD(Item):
  def __init__(self,title,description,director,certificate):
    super().__init__(title,description)
    self.director = director
    self.certificate = certificate
    
  def viewDescription(self):
    print("DVD Title: " + self.title)
    print("Description: " + self.description)
    print("Director: " + self.director)
    print("Certificate: " + self.certificate)

class CD(Item):
  def __init__(self,title,description,artist,genre,numberOfTracks):
    super().__init__(title,description)
    self.artist = artist
    self.genre = genre
    self.numberOfTracks = numberOfTracks
    
  def viewDescription(self):
    print("CD Title: " + self.title)
    print("Description: " + self.description)
    print("Artist: " + self.artist)
    print("Genre: " + self.genre)
    print("Number of Tracks: " + str(self.numberOfTracks))
    
class Book(Item):
  def __init__(self,title,description,author,isbn):
    super().__init__(title,description)
    self.author = author
    self.isbn = isbn
    
  def viewDescription(self):
    print("Book Title: " + self.title)
    print("Description: " + self.description)
    print("Author: " + self.author)
    print("ISBN: " + self.isbn)
    