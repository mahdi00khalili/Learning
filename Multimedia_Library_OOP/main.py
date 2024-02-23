#Multimedia Library - www.101computing.net/multimedia-libary-oop-concepts/
from items import CD, DVD, Book
from library import Library

myLibrary = Library()
book1 = Book("Enigma","A fiction book taking place at Bletchley Park in 1943.","Robert Harris","978-0099527923")
book2 = Book("Life 3.0","Being Human in the Age of Artificial Intelligence.","Max Tegmark","978-0141981802")
book3 = Book("The Code Book","The Science of Secrecy from Ancient Egypt to Quantum Cryptography.","Simon Singh","978-1857028898")
dvd1 = DVD("The Imitation Game","A historical drama film, based on the 1983 biography Alan Turing: The Enigma by Andrew Hodges.","Morten Tyldum","12")
cd1 = CD("Divide","Released in March 2017.","Ed Sheeran","Pop/Rock",12)

myLibrary.addItem(book1)
myLibrary.addItem(book2)
myLibrary.addItem(book3)
myLibrary.addItem(dvd1)
myLibrary.addItem(cd1)

myLibrary.listItems()