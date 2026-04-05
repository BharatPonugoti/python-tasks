#Library Management System (Constructor & Inheritance)#
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, size):
        super().__init__(title, author)
        self.size = size

    def display(self):
        print(self.title, self.author, self.size)

b = EBook("Python", "John", "5MB")
b.display()