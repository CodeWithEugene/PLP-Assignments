# Define a class representing a Book
class Book:
    # Constructor to initialize the book object with unique values
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Method to display book details
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

# Define a class representing an EBook that inherits from Book
class EBook(Book):
    # Constructor to initialize the ebook object with unique values
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size

    # Method to display ebook details, overriding the display_info method
    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, File Size: {self.file_size}MB"

# Create instances of Book and EBook
book = Book("1984", "George Orwell", 328)
ebook = EBook("Digital Fortress", "Dan Brown", 356, 2)

# Display information of the book and ebook
print(book.display_info())
print(ebook.display_info())

# Activity 2: Polymorphism Challenge! 🎭

# Define a base class representing a Vehicle
class Vehicle:
    # Method to be overridden by subclasses
    def move(self):
        pass

# Define a class representing a Car that inherits from Vehicle
class Car(Vehicle):
    # Override the move method
    def move(self):
        print("Driving 🚗")

# Define a class representing a Plane that inherits from Vehicle
class Plane(Vehicle):
    # Override the move method
    def move(self):
        print("Flying ✈️")

# Create instances of Car and Plane
car = Car()
plane = Plane()

# Call the move method on each instance
car.move()
plane.move()