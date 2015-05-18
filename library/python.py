#!/usr/bin/python
class Book:
	#initialize a book with a title
	def __init__(self, title):
		self.title = title
		self.shelf = None
	
	#moves book to specified shelf
	def enshelf(self, shelf):
		#ensure book is not in two places at once
		if self.shelf != None:
			Book.deshelf(self)
		#keep track of what shelf the book is in
		self.shelf = shelf
		#shelf book
		shelf.enshelf(self)
	
	#removes book from existing shelf
	def deshelf(self):
		self.shelf.deshelf(self)
		self.shelf = None
		
class Shelf:	
	#add shelf to library
	def __init__(self, shelf, library):
		self.shelf = shelf
		self.books = []
		library.addShelf(self)
	
	#add book to own shelf
	def enshelf(self, book):
		self.books.append(book)
	
	#removes book from own shelf
	def deshelf(self, book):
		self.books.remove(book)

class Library:
	#initialize an array of all shelves
	def __init__(self):
		self.shelves = []
	
	#add shelves to the library
	def addShelf(self, shelf):
		self.shelves.append(shelf)

	#print all books
	def printBooks(self):
		for shelf in self.shelves:
			for books in shelf.books:
				print (books.title)
		
		
#sample code
lib1 = Library()
shelf1 = Shelf("num1", lib1)
book1 = Book("sample1")
book1.enshelf(shelf1)
book2 = Book("sample2")
book2.enshelf(shelf1)
book3 = Book("sample3")
book3.enshelf(shelf1)
book1.deshelf()
shelf2 = Shelf("num2", lib1)
book4 = Book("daveosucks")
book4.enshelf(shelf2)
lib1.printBooks()
book4.deshelf()
print("")
lib1.printBooks()